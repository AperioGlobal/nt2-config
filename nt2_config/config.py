import os

from ruamel.yaml import YAML, yaml_object

from dotenv import dotenv_values


NT2_ENV_FNAME = ".env.nt2"
NT2_ENV_SECRETS_FNAME = ".env.nt2_secrets"


def load_environment_values(
    env_fname=NT2_ENV_FNAME, secrets_fname=NT2_ENV_SECRETS_FNAME
):
    config = {
        **dotenv_values(env_fname),  # load shared development variables
        **dotenv_values(secrets_fname),  # load sensitive variables
        **os.environ,  # override loaded values with environment variables
    }
    return config


def config_loader(env_fname=NT2_ENV_FNAME, secrets_fname=NT2_ENV_SECRETS_FNAME):
    yaml_reader = YAML(typ="safe")

    environment_values = load_environment_values(env_fname, secrets_fname)

    @yaml_object(yaml_reader)
    class EnvVar:
        yaml_tag = "!ENV"
        environ = environment_values

        def __init__(self, name, value=None):
            self.varname = name
            if not value:
                self.value = self.environ.get(name, "")

        def __repr__(self):
            return f"EnvVar({self.varname } -> {self.value})"

        def __str__(self):
            if self.value:
                return str(self.value)
            else:
                return ""

        @classmethod
        def to_yaml(cls, representer, node):
            return representer.represent_scalar(cls.yaml_tag, f"{node.varname}")

        @classmethod
        def from_yaml(cls, constructor, node):
            return cls(node.value)

    @yaml_object(yaml_reader)
    class SecretVar:
        yaml_tag = "!SECRET"
        environ = environment_values

        def __init__(self, name, value=None):
            self.varname = name
            if not value:
                self.value = self.environ.get(name, "")

        def __repr__(self):
            return f"SecretVar({self.varname } -> ***** )"

        def __str__(self):
            if self.value:
                return str(self.value)
            else:
                return ""

        @classmethod
        def to_yaml(cls, representer, node):
            return representer.represent_scalar(cls.yaml_tag, f"{node.varname}")

        @classmethod
        def from_yaml(cls, constructor, node):
            return cls(node.value)

    yaml_reader.environ = environment_values
    return yaml_reader
