import os
import configparser

__app_name__ = "DummyApi"

CONF_PATH = os.getenv(
    "CONFIGS_FOLDER",
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)),
)

conf = configparser.ConfigParser(
    defaults={
        "env": "dev",
        "host": "0.0.0.0",
        "port": "8000",
        "debug": "false",
    },
    default_section=__app_name__,
)

conf.read(
    [os.path.join(CONF_PATH, "settings.cfg.dist")]
)

# search conf main configs in main path
LOCAL_CONF_PATH = os.path.join(
    CONF_PATH, "settings.cfg"
)

_files = [os.path.join(CONF_PATH, "settings.cfg.dist")]

for entry in os.scandir(CONF_PATH):
    if entry.name.endswith('.cfg') and entry.is_file():
        _files.append(os.path.join(CONF_PATH, entry.name))

conf.read(_files)
