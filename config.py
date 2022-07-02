import os
from dotenv import load_dotenv


class DatabaseSettings:
    load_dotenv()
    _environ = os.environ

    db_serv: str = _environ.get("DATABASE_HOST", None)
    db_port: int = _environ.get("DATABASE_PORT", None)
    db_user: str = _environ.get("DATABASE_USER", None)
    db_pwd: str = _environ.get("DATABASE_PASSWORD", None)
    db_name: str = _environ.get("DATABASE_NAME", None)


class Config:
    DB_SETTINGS = DatabaseSettings()
