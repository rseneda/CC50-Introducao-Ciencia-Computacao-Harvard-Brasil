import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))

        if day >31 or day < 1 or month > 12 or month < 1:
            return "Please put a valid date"
        if not name:
            return "Please put your name"

        db.execute("INSERT INTO birthdays (name, month,day) VALUES (?, ?, ?)", name, month, day)


        return redirect("/")

    else:
        births = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", births=births)
