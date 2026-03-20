from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PACKAGE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "skinmate-dev-secret-key")
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    DATABASE_PATH = BASE_DIR / "instance" / "skinmate.sqlite"
    SEED_DATABASE_PATH = PACKAGE_DIR / "resources" / "seed" / "skinmate.sqlite"
    UPLOAD_DIR = BASE_DIR / "uploads"
    STATIC_UPLOADS_DIR = PACKAGE_DIR / "static" / "uploads_temp"
    TEMPLATE_FOLDER = str(PACKAGE_DIR / "templates")
    STATIC_FOLDER = str(PACKAGE_DIR / "static")
    MODEL_DIR = PACKAGE_DIR / "resources" / "models"
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
    DEFAULT_FALLBACK_SCORES = {
        "moisture": 55.0,
        "elasticity": 58.0,
        "wrinkle": 52.0,
    }
