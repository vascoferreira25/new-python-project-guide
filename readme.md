# How to create a new Python project

Create a Python project with `Poetry`, `Mkdocs` and `Pytest`. This will allow
you to manage environments, documentation and testing of your Python projects.

## Table of Contents

- [Steps](#steps)
- [Poetry - Virtual Environment Manager](#poetry---virtual-environment-manager)
    - [Install on Windows](#install-on-windows)
    - [Create a project](#create-a-project)
    - [Dependencies](#dependencies)
        - [Add and remove dependencies](#add-and-remove-dependencies)
        - [Install the environment](#install-the-environment)
        - [Show installed dependencies](#show-installed-dependencies)
        - [Update dependencies](#update-dependencies)
    - [Environment](#environment)
        - [Show info about environments](#show-info-about-environments)
        - [Remove the current project environment](#remove-the-current-project-environment)
        - [List all environments](#list-all-environments)
        - [Activate the environment](#activate-the-environment)
        - [Activate system environment](#activate-system-environment)
    - [Build package](#build-package)
    - [Run package](#run-package)
        - [main file](#main-file)
        - [pyproject settings](#pyproject-settings)
    - [Run tests](#run-tests)
    - [Run a single file](#run-a-single-file)
    - [Project structure](#project-structure)
- [Documentation](#documentation)
    - [Google Style](#google-style)
        - [Module documentation](#module-documentation)
        - [Function documentation](#function-documentation)
    - [Mkdocs](#mkdocs)
        - [Install](#install)
        - [Create docs](#create-docs)
        - [Themes and Extensions](#themes-and-extensions)
        - [Mkdocs Configuration](#mkdocs-configuration)
        - [Custom CSS](#custom-css)
        - [Serve docs](#serve-docs)
        - [Autodoc](#autodoc)
- [Testing](#testing)
    - [Simple usage](#simple-usage)
    - [Assert exceptions](#assert-exceptions)
    - [Group](#group)
    - [Run](#run)
    - [Detailed summary](#detailed-summary)

## Steps

The easiest way to start a new project is with Poetry, as it creates all the
necessary folders and starts a virtual environment to keep all the code
working.

Steps to a create a new Python project:

1.  Create a project with [Poetry](#create-a-project): `poetry new project-name` and `cd` into the project
    folder
2.  Init the git repository with `git init`
3.  Create a `__main__` file with a `main` function that will start the
    program (check this [main file](#main-file))
4.  Change the `pyproject.toml` file to include the `__main__` file and `main`
    function (check this [pyproject.toml](#pyproject-settings))
5.  Write functions and test them with [Pytest](#testing)
6.  Setup [Mkdocs](#mkdocs) for documentation and API documentation
7.  Check the documentation with `mkdocs serve`
8.  Run the project with `poetry run main`

## Poetry - Virtual Environment Manager

### Install on Windows

``` {.shell}
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

Check the installation by running:

``` {.shell}
poetry --version
```

Update it with:

``` {.shell}
poetry self update
```

### Create a project

Names with `-` will have the folders\' names replaced with underscores.

``` {.shell}
poetry new [project-name]
```

### Dependencies

#### Add and remove dependencies

``` {.shell}
poetry add [package-name]
```

``` {.shell}
poetry remove [package-name]
```

Some packages may need more options to be installed, for example `Pytorch`:

``` {.shell}
poetry add torch===1.6.0 --platform windows
```

#### Install the environment

``` {.shell}
poetry install
```

#### Show installed dependencies

``` {.shell}
poetry show --tree
```

#### Update dependencies

``` {.shell}
poetry update
```

### Environment

#### Show info about environments

``` {.shell}
poetry env info
```

#### Remove the current project environment

``` {.shell}
poetry env remove python
```

#### List all environments

``` {.shell}
poetry env list
```

#### Activate the environment

``` {.shell}
poetry env use ./path/to/env
```

#### Activate system environment

``` {.shell}
poetry env use system
```

### Build package

``` {.shell}
poetry build
```

### Run package

Setup the `__main__.py` and `pyproject.toml` files and then run:

Run the project:

``` {.shell}
poetry run main
```

#### main file

Create a `__main__.py` file with the code to run, for example:

``` {.python}
# Import stuff from other files
# from . import module

def main():
    print("Hello, World!")

if __name__ == '__main__':
    main()
```

#### pyproject settings

Add the following to the `pyproject.toml`, just before the `[build-system]` and
replace the `project_name` with the name of your project:

``` {.toml}
[tool.poetry.scripts]
main = "project_name.__main__:main"
```

### Run tests

``` {.shell}
poetry run pytest
```

### Run a single file

``` {.shell}
poetry run python ./path/to/file.py
```

### Project structure

The project must have the following file structure:

``` {.example}
package-name
|- README.rst
|- poetry.lock
|- pyproject.toml
|- tests
   |- ... # your test files
|- package_name
   |- package_name
      |- __init__.py
      |- __main__.py
      |- ... # your python files
      |- module
         |- __init__.py
         |- ... # module files
```

Create a file called `__main__.py` in the `package_name` folder to allow the
usage of `python -m package_name` to run the project.

You can create more folders:

-   `out` for the output of your program,
-   `resources` for files needed by your program.

**Note**: If you don\'t run the package with the `-m` arg, it will raise an
error saying it can\'t run relative imports. Don\'t use `./` either.

## Documentation

### Google Style

#### Module documentation

```` {.python}
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the `Example` or `Examples`
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

    ```python
    python example_google.py
    ```

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the `Attributes` section of the module docstring, or in an
        inline docstring immediately following the variable.
        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

!!! todo "A todo"
    Todo this

!!! bug "A note"
    A simple note

??? summary "Hidden notes"
    This is hidden

??? tip "These are all the fields"
    - note
    - summary
    - todo, info
    - tip
    - done
    - question
    - warning
    - fail
    - danger
    - bug
    - example
    - quote
"""
````

#### Function documentation

```` {.python}
def function_with_types_in_docstring(param1=1, param2=2):
    """Example function with types documented in the docstring.

    `PEP 484` type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`, they do not need to be
    included in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        tupple(str, str): ret1 description, ret2 destription.

        Examples:
        ```python
        # Run the function
        function_with_types_in_docstring(param1, param2)
        ```
    """
    pass
````

### Mkdocs

1.  Install mkdocs (if needed)
2.  Install themes and extensions ([if needed](#themes-and-extensions))
3.  Create a mkdocs site with `mkdocs new .`
4.  Edit the `mkdocs.yml` to setup themes and extensions - [like
    this](#mkdocs-configuration)
5.  Add modules to the docs with [Autodoc](#mkdocs-autodoc)
6.  Serve the docs with `mkdocs serve`


####  Install

``` {.shell}
poetry add mkdocs
```

#### Create docs

``` {.shell}
poetry run mkdocs new .
```

#### Themes and Extensions

``` {.shell}
poetry add mkdocstrings
poetry add mkdocs-material
```

#### Mkdocs Configuration

``` {.yml}
site_name: My Docs

theme:
    name: "material"
    highlightjs: true
    hljs_languages:
    - python

extra_css:
    - styles.css

extra_javascript: 
    - https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML

markdown_extensions:
    - admonition
    - codehilite
    - toc
    - def_list
    - abbr
    - attr_list
    - tables
    - pymdownx.arithmatex
    - pymdownx.details
    - pymdownx.superfences

plugins:
    - search
    - mkdocstrings:
        default_handler: python
        handlers:
        python:
            rendering:
            show_source: true 
            show_root_heading: true
            show_category_heading: true
            show_object_full_path: false
            show_if_no_docstring: true
        custom_templates: templates
        watch:
        - ./
```

#### Custom CSS

Create a file `docs/styles.css` to hold your CSS settings:

``` {.css}
.doc-heading {
    background-color: rgba(64, 81, 181, 0.15);
    padding: 8px;
    border-radius: 4px;
    border-left: 4px solid rgb(64, 81, 181);
}

.doc-heading {
    margin-top: 72px;
}

.doc-module > .doc-contents {
    padding-left: 24px;
}

.doc-class > .doc-contents, .doc-method > .doc-contents, .doc-function > .doc-contents {
    margin-bottom: 64px;
    padding-left: 24px;
    border-left: 2px solid rgba(64, 81, 181, 0.2);
}
```

#### Serve docs

``` {.shell}
poetry run mkdocs serve
```

#### Autodoc

Add this to the `.md` file to show specific modules:

``` {.markdown}
::: project_name.submodule.file
::: project_name.file
```

or this to show all the documentation of the project:

```markdown
::: project_name
```

## Testing

Steps:

1.  Create a folder called `tests` outside of the `source` folder
2.  Create a test file for each module: a `main.py` will have a
    `test_main.py`
3.  Create a `def test_function_name()` function for each function
    inside your modules
4.  Run `pytest -vv` and check for errors

**Note**: Try to split your code into pure functions (no side effects and no
global variables) to make it easier to write tests.
    
### Simple usage

``` {.python}
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

### Assert exceptions

``` {.python}
# content of test_sysexit.py
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

### Group

It might be usefull for when you have several types of tests on the same
module.

``` {.python}
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
```

### Run

``` {.shell}
poetry run pytest
```

### Detailed summary

``` {.shell}
poetry run pytest -vv [-rA --durations=0]
```
