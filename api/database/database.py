from sqlalchemy import create_engine

from .. import conf


saas_engine = create_engine(
    "mysql+mysqldb://{user}:{password}@{hostname}:{port}/{database}".format(
        user=conf.get("saas_db", "user"),
        password=conf.get("saas_db", "password"),
        hostname=conf.get("saas_db", "hostname"),
        port=conf.get("saas_db", "port"),
        database=conf.get("saas_db", "database"),
    )
)


instance_engine = create_engine(
    "mysql+mysqldb://{user}:{password}@{hostname}:{port}/{database}".format(
        user=conf.get("instance", "user"),
        password=conf.get("instance", "password"),
        hostname=conf.get("instance", "hostname"),
        port=conf.get("instance", "port"),
        database=conf.get("instance", "database"),
    )
)
