"""This defines an API that other Python code can use to interact with LICE2."""

from lice2.api.exceptions import LanguageNotFoundError, LicenseNotFoundError
from lice2.constants import LANGS, LICENSES
from lice2.helpers import (
    format_license,
    generate_license,
    get_local_year,
    load_package_template,
)


class Lice:
    """List or Generate a License from many supported licenses."""

    def __init__(
        self,
        organization: str,
        project: str,
        year: str = get_local_year(),
    ) -> None:
        """Initialize the Lice object.

        Args:
            organization: The name of the organization that owns the project.
            project: The name of the project.
            year: The year to use in the license. Defaults to the current year.

        Note that not all licenses will use the 'project' field.

        Example:
        >>> lice = Lice(organization="Awesome Co.", project="my_project")
        """
        self.organization = organization
        self.project = project
        self.year = year

    def get_licenses(self) -> list[str]:
        """Return a list of all licenses in the system.

        This returns a list of strings, where each string is the name of a
        license that can then be used to generate or retrieve the text of that
        license.

        Example:
            >>> lice = Lice(organization="Awesome Co.", project="my_project")
            >>> lice.get_licenses()
            ['apache', 'bsd2', 'bsd3', 'gpl2', 'gpl3', ...]
        """
        return LICENSES

    def get_languages(self) -> list[str]:
        """Return a list of all supported languages.

        This returns a list of strings, where each string is the name of a
        language EXTENSION that can be used to generate a license in that
        language format.

        Example:
            >>> lice = Lice(organization="Awesome Co.", project="my_project")
            >>> lice.get_languages()
            ['py', 'js', 'c', 'cpp', 'java', 'rs', 'rb', 'sh', 'html', ...]
        """
        return list(LANGS.keys())

    def get_license(self, license_name: str, language: str = "") -> str:
        """Return the text of the given license.

        Args:
            license_name: The name of the license to retrieve.
            language: [OPTIONAL] If set, comment the license for that language.

        Examples:
            >>> lice = Lice(organization="Awesome Co.", project="my_project")
            >>> licence_txt = Lice.get_license("mit")
        """
        args = {
            "year": self.year,
            "organization": self.organization,
            "project": self.project,
        }
        try:
            template = load_package_template(license_name)
        except FileNotFoundError:
            raise LicenseNotFoundError(license_name) from None

        content = generate_license(template, args)

        try:
            out = format_license(content, language)
        except KeyError:
            raise LanguageNotFoundError(language) from None
        return out.getvalue()