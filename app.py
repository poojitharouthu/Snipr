from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-later"

DB_NAME = "snipr.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if not os.path.exists(DB_NAME):
        conn = get_db_connection()
        conn.execute(
            """
            CREATE TABLE urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE
            )
            """
        )
        conn.commit()
        conn.close()


def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    conn = get_db_connection()
    while True:
        code = "".join(random.choice(chars) for _ in range(length))
        exists = conn.execute(
            "SELECT 1 FROM urls WHERE short_code = ?", (code,)
        ).fetchone()
        if not exists:
            conn.close()
            return code


@app.route("/", methods=["GET", "POST"])
def index():
    init_db()

    if request.method == "POST":
        long_url = request.form.get("long_url", "").strip()

        if not long_url:
            error = "Please enter a URL."
            return render_template("index.html", error=error)

        # Add protocol if missing
        if not (long_url.startswith("http://") or long_url.startswith("https://")):
            long_url = "https://" + long_url

        conn = get_db_connection()
        # Reuse same short code if URL already exists
        row = conn.execute(
            "SELECT short_code FROM urls WHERE original_url = ?", (long_url,)
        ).fetchone()

        if row:
            code = row["short_code"]
        else:
            code = generate_short_code()
            conn.execute(
                "INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
                (long_url, code),
            )
            conn.commit()

        conn.close()

        short_url = request.host_url + code
        return render_template("index.html", short_url=short_url)

    # GET -> first page state
    return render_template("index.html")


@app.route("/<short_code>")
def redirect_to_url(short_code):
    init_db()
    conn = get_db_connection()
    row = conn.execute(
        "SELECT original_url FROM urls WHERE short_code = ?", (short_code,)
    ).fetchone()
    conn.close()

    if row:
        return redirect(row["original_url"])
    else:
        return "This Snipr link does not exist.", 404


if __name__ == "__main__":
    app.run(debug=True)
