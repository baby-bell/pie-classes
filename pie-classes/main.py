import sqlite3
import os

from flask import Flask, g
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "pie_classes.db"),
    SECRET_KEY="secret",
    USERNAME="admin",
    PASSWORD="default"
))

def connect_db():
    db = sqlite3.connect(app.config["DATABASE"])
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    with app.open_resource("schema.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command("init_db")
def init_db_command():
    init_db()
    print("Initialized the database")

def get_db():
    if not hasattr(g, "database"):
        g.database = connect_db()
    return g.database

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "database"):
        g.database.close()
