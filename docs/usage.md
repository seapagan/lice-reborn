# Usage

## Basic Usage

At its simplest, `lice` will generate a license header for you to the standard
output. If you don't specify a license, `lice` will default to the BSD-3
license.

```console
$ lice

 Copyright (c) 2024, Grant Ramsay

 All rights reserved.

 Redistribution and use in source and binary forms, with or without modification,
 ...
```

It will fill in the current year and your name as the copyright holder.

## Specifying a License

You can specify a license as the first option. For example, to generate a MIT
license:

```console
$ lice mit

The MIT License (MIT)
Copyright (c) 2024 Grant Ramsay

Permission is hereby granted, free of charge, to any person obtaining a copy
...
```

This can be used with any of the options below. Run `lice --licenses` to see a
list of all available licenses.

## Command Line Options

`lice` has a number of command line options to customize the output. For a full
list of options, run `lice --help`.

### `--header` option

This will generate a brief license header that can be used in source files.

```console
lice --header
```

Again, you can specify a license:

```console
lice --header apache
```

!!! note
    The `--header` option is not available for all licenses. If it is not
    available, there will be a message to that effect.

### `--org` / `-o` option

This will allow you to specify an organization name to be used in the license,
and can be set in the configuration file under the `organization` key.

```console
lice -o "Awesome Co."
```

### `--proj` / `-p` option

This will allow you to specify a project name to be used in the license.

```console
lice -p "My Awesome Project"
```

!!! note
    Not all licenses support the `--proj` option. Run `lice --licences` to see
    which licenses support this option.

### `--template` / `-t` option

This will allow you to specify a custom template to be used as the license.

```console
lice -t "./path/to/template.txt"
```

### `--year` / `-y` option

This will allow you to specify a year to be used in the license.

```console
lice -y 2024
```

### `--language` / `-l` option

This will allow you to specify a **programming** language to be used in the
license. Specify the **extension** of the file you are creating the license for.

```console

lice -l py
```

Currently supported languages are:

agda, c, cc, clj, cpp, css, el, erl, f, f90, h, hpp, hs, html, idr, java, js,
lisp, lua, m, ml, php, pl, py, ps, rb, scm, sh, txt, rs

### `--file` / `-f` option

This will allow you to specify a file name to be used in the license, and so the
license will be written to that file instead of the standard output.

```console
lice mit -f "LICENSE.txt"
```

!!! note
    If you specify a language with the `-l` option, the extension will be
    automatically added to the file name so you don't need to include it.

### `--vars` option

This will list the variables that can be used in the specified license.

```console
lice --vars mit
```

### `--licenses` option

This will list all the available licenses and their parameters.

```console
lice --licenses
```

### `--languages` option

This will list all the available source code formatting languages.

```console
lice --languages
```

### `--install-completion` option

This will install tab-completion for the current shell.

```console
lice --install-completion
```

### `--show-completion` option

This will show the tab-completion for the current shell, so you can copy it or
customize the installation.

```console
lice --show-completion
```

### `--help` / `-h` option

Displays help for the application and it's options.

```console
lice --help
```