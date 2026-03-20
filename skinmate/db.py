from __future__ import annotations

import shutil
import sqlite3
from pathlib import Path
from flask import current_app, g

USER_SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    analysis_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    skin_type TEXT NOT NULL,
    recommendation_text TEXT NOT NULL,
    scores_json TEXT NOT NULL,
    concerns_json TEXT NOT NULL,
    image_filename TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""


def ensure_runtime_files() -> None:
    db_path = Path(current_app.config["DATABASE_PATH"])
    seed_db = Path(current_app.config["SEED_DATABASE_PATH"])
    db_path.parent.mkdir(parents=True, exist_ok=True)
    Path(current_app.config["UPLOAD_DIR"]).mkdir(parents=True, exist_ok=True)
    Path(current_app.config["STATIC_UPLOADS_DIR"]).mkdir(parents=True, exist_ok=True)

    if not db_path.exists() and seed_db.exists():
        shutil.copy2(seed_db, db_path)

    with sqlite3.connect(db_path) as conn:
        conn.executescript(USER_SCHEMA)
        # products table seed DB 기준으로 유지. 없으면 최소 테이블 생성
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER UNIQUE,
                name TEXT NOT NULL,
                brand TEXT NOT NULL,
                image_url TEXT,
                product_url TEXT,
                rank INTEGER NOT NULL DEFAULT 999,
                main_category TEXT NOT NULL,
                middle_category TEXT,
                sub_category TEXT NOT NULL,
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        conn = sqlite3.connect(current_app.config["DATABASE_PATH"], detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        g.db = conn
    return g.db


def close_db(_=None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()
