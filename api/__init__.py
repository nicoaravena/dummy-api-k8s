import os
import configparser

DEFAULTS_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), os.path.pardir, "settings.cfg.dist"
    )
)

conf = configparser.ConfigParser()

conf.read([DEFAULTS_FILE])


# search conf main configs in main path
LOCAL_CONF_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir, "settings.cfg")
)

PATHS = []

if os.path.exists(LOCAL_CONF_PATH):
    PATHS.append(LOCAL_CONF_PATH)

if conf.get("app", "name") and conf.get("app", "env"):
    # By default go to /etc/dummy.k8s.d/dev/dummy-api
    OVERRIDES_CONF_PATH = os.path.abspath(
        os.path.join(
            os.getenv("CONFIG_FOLDER", "/etc/dummy.k8s.d"),
            conf.get("app", "env"),
            "{}.cfg".format(conf.get("app", "name").lower()),
        )
    )
    if os.path.exists(OVERRIDES_CONF_PATH):
        PATHS.append(OVERRIDES_CONF_PATH)

if PATHS:
    conf.read(PATHS)
