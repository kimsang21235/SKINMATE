
from __future__ import annotations

from flask import Flask

from skinmate.auth import init_auth_routes
from skinmate.config import Config
from skinmate.db import close_db, ensure_runtime_files
from skinmate.routes import init_main_routes
from skinmate.utils.template_filters import fromjson, get_face_icon_for_score


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=Config.TEMPLATE_FOLDER,
        static_folder=Config.STATIC_FOLDER,
    )
    app.config.from_object(Config)

    with app.app_context():
        ensure_runtime_files()

    app.teardown_appcontext(close_db)
    app.jinja_env.filters['fromjson'] = fromjson
    app.jinja_env.globals['get_face_icon'] = get_face_icon_for_score

    init_auth_routes(app)
    init_main_routes(app)

    return app
