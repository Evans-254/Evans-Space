import os
from dotenv import load_dotenv
from pathlib import Path

basedir = Path(__file__).resolve().parent
env_path = basedir / ".env"
if env_path.exists():
    load_dotenv(env_path)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{basedir / 'site.db'}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", str(basedir / "uploads"))
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 100 * 1024 * 1024))  # 100 MB
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
    ALLOWED_VIDEO_EXTENSIONS = {"mp4", "webm", "ogg", "mov", "mkv"}
    # Limit displayed file list to avoid directory traversal
