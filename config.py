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


class FolderSettings:
    load_dotenv()
    _environ = os.environ

    video_folder: str = _environ.get("VIDEO_STORAGE", None)
    thumbnail_folder: str = _environ.get("THUMBNAIL_STORAGE", None)


class Config:
    DB_SETTINGS = DatabaseSettings()
    STORAGE_SETTINGS = FolderSettings()
