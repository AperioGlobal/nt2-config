# nt2-config

[![PyPI](https://img.shields.io/pypi/v/nt2-config.svg)](https://pypi.org/project/nt2-config/)
[![Changelog](https://img.shields.io/github/v/release/AperioGlobal/nt2-config?include_prereleases&label=changelog)](https://github.com/AperioGlobal/nt2-config/releases)
[![Tests](https://github.com/AperioGlobal/nt2-config/actions/workflows/test.yml/badge.svg)](https://github.com/AperioGlobal/nt2-config/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/AperioGlobal/nt2-config/blob/master/LICENSE)

Standalone module for reading nt2 config files

## Installation

Install this tool using `pip`:

    pip install git+https://github.com/AperioGlobal/nt2-config

## Usage

For help, run:

    nt2-config --help

You can also use:

    python -m nt2_config --help
	
Rename and edit the example yaml config and .env files.

	$ mv nt2_config.example .nt2_config.yaml
	$ ${VISUAL:-${EDITOR:-vi}} .nt2_config.yaml
	$ mv env_nt2.example .env.nt2
	$ ${VISUAL:-${EDITOR:-vi}} .env.nt2
	$ mv env_nt2_secrets.example .env.nt2_secrets
	$ ${VISUAL:-${EDITOR:-vi}} .env.nt2_secrets
	$ nt2-config -f nt2_config.example -e env_nt2.example -s env_nt2_secrets.example config
	{'dvr': {'name': EnvVar(DVR_REPO_NAME -> nt2-dataset),
         'url': EnvVar(DVR_URL -> ),
         'path': EnvVar(DVR_PATH -> /Users/example/datasets/nt2_dataset),
         'remotes': {'git': 'dvregistry-local',
                     'git_branch': 'origin/main',
                     'data': EnvVar(DVR_REMOTE_NAME -> dvregistry-local)}},
      'dagster': {'postgres': {'db': EnvVar(DAGSTER_POSTGRES_DB -> some_db),
                               'user': EnvVar(DAGSTER_POSTGRES_USER -> some_user),
                               'password': SecretVar(DAGSTER_POSTGRES_PASSWORD -> ***** )}}}

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

	git clone https://github.com/AperioGlobal/nt2-config
    cd nt2-config
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
