from config import Config as config
import psycopg2


def conn():
    connection = psycopg2.connect(host=config.DB_SETTINGS.db_serv,
                                  port=config.DB_SETTINGS.db_port,
                                  user=config.DB_SETTINGS.db_user,
                                  password=config.DB_SETTINGS.db_pwd,
                                  database=config.DB_SETTINGS.db_name)

    cur = connection.cursor()
    return cur
