import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}"
        f"@{os.environ['MYSQL_HOST']}/{os.environ['MYSQL_DATABASE']}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False