from flask import Blueprint, render_template
from ..db import get_connection

home_bp = Blueprint("home", __name__, url_prefix="/")

@home_bp.get("/")
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM personal_info")
    result = cur.fetchone()
    data = {
        "name": result[1],
        "bio": result[2],
        "location": result[3],
        "email": result[4],
        "picture": result[5]
    }
    return render_template("home.html", data=data, name=data["name"])