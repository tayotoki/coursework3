from pathlib import Path
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAclhemy

from sqlalchemy.sql import func


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = BASE_DIR / "templates"
STATIC = BASE_DIR / "static"

app = Flask(
    import_name="gram",
    static_folder=STATIC,
    template_folder=TEMPLATES,
)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(BASE_DIR, "database.db")
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAclhemy(app)