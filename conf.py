from config.common import ConfigurationBuilder
from config.env import EnvVars
from config.yaml import YAMLFile


def load_configuration():
    builder = ConfigurationBuilder()

    builder.add_source(YAMLFile("cv.yml"))
    builder.add_source(EnvVars("CV_"))

    return builder.build()
