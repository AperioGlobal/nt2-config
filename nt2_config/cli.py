import logging
import sys

from pathlib import Path
from pprint import pprint, pformat, pp

import click

from .config import config_loader

from .logconfig import DEFAULT_LOG_FORMAT, logging_config


@click.group()
@click.version_option()
@click.option(
    "--log-format",
    type=click.STRING,
    default=DEFAULT_LOG_FORMAT,
    help="Python logging format string",
)
@click.option(
    "--log-level", default="ERROR", help="Python logging level", show_default=True
)
@click.option(
    "--log-file",
    help="Python log output file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True, path_type=Path),
    default=None,
)
@click.option(
    "-f",
    "--config-file",
    "config_file",
    default="-",
    type=click.Path(file_okay=True, dir_okay=False, path_type=Path),
    help="Location of the config YAML file",
    show_default=True,
)
@click.option(
    "-e",
    "--environment-file",
    "environment_file",
    default=".env.nt2",
    type=click.Path(file_okay=True, dir_okay=False, path_type=Path),
    help="Location of the config environment file",
    show_default=True,
)
@click.option(
    "-s",
    "--secrets-file",
    "secrets_file",
    default=".envt.nt2_secrets",
    type=click.Path(file_okay=True, dir_okay=False, path_type=Path),
    help="Location of the config secrets file",
    show_default=True,
)
@click.pass_context
def cli(
    ctx: click.Context,
    log_format: str,
    log_level: str,
    log_file: Path,
    config_file: Path,
    environment_file: Path,
    secrets_file: Path,
):
    "Standalone module for reading nt2 config files"

    logging_config(log_format, log_level, log_file)

    if str(config_file) != "-" and not config_file.exists():
        logging.error("Config file %s, does not exist", config_file)
        sys.exit(2)

    logging.info("CONFIG: %s", config_file)
    logging.info("ENV: %s", environment_file)
    logging.info("SECRETS: %s", secrets_file)

    ctx.obj = {"CONFIG": config_file, "ENV": environment_file, "SECRETS": secrets_file}


@cli.command(name="config")
@click.pass_context
def config(ctx: click.Context):

    config_path = ctx.obj["CONFIG"]
    logging.info("Reading yaml content from: %s, %s", config_path, type(config_path))

    loader = config_loader(ctx.obj["ENV"], ctx.obj["SECRETS"])
    with config_path.open() as in_yaml:
        config = loader.load(in_yaml)

        click.echo(pp(config))
        logging.debug("Environment:\n%s", pformat(list(loader.environ.items())))
