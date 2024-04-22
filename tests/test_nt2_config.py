from click.testing import CliRunner
from nt2_config.cli import cli

from nt2_config import config


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_config():
    config.load_environment_variables()
    config_loader = config.config_loader()
