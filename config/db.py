from sqlalchemy import create_engine, MetaData
from config.settings import settings
from sqlalchemy_utils import database_exists, create_database


connection = None

try:
    # need to intall pymysql to interact with sqlalchemy
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}:3306/{}".format(
            settings.database_user,
            settings.database_password,
            settings.database_host,
            settings.database_name)
    )

    if not database_exists(engine.url):
        create_database(engine.url)

    connection = engine.connect()
except:
    print(f"Error connecting to MariaDB Platform")


metadata = MetaData()
