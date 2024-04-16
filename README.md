# nt2-config

[![PyPI](https://img.shields.io/pypi/v/nt2-config.svg)](https://pypi.org/project/nt2-config/)
[![Changelog](https://img.shields.io/github/v/release/bmdaperio/nt2-config?include_prereleases&label=changelog)](https://github.com/bmdaperio/nt2-config/releases)
[![Tests](https://github.com/bmdaperio/nt2-config/actions/workflows/test.yml/badge.svg)](https://github.com/bmdaperio/nt2-config/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/bmdaperio/nt2-config/blob/master/LICENSE)

Standalone module for reading nt2 config files

## Installation

Install this tool using `pip`:

    pip install nt2-config

## Usage

For help, run:

    nt2-config --help

You can also use:

    python -m nt2_config --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd nt2-config
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
