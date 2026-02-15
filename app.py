from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = "bioscan_secret"

# ---------------- USERS (TEMP STORAGE) ----------------
users = {}

# ---------------- LOGIN REQUIRED DECORATOR ----------------
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated

# ---------------- AUTH ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users and users[email] == password:
            session["user"] = email
            return redirect("/home")

    return render_template("auth/login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            users[email] = password
            return redirect("/")

    return render_template("auth/signup.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# ---------------- MAIN PAGES ----------------
@app.route("/home")
@login_required
def home():
    return render_template("home.html")


@app.route("/tips")
@login_required
def tips():
    return render_template("tips.html")


@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html")

# ---------------- DETECTION ----------------
@app.route("/detection", methods=["GET", "POST"])
@login_required
def detection():
    result = None

    if request.method == "POST":
        image = request.files.get("image")

        if image and image.filename != "":
            filename = secure_filename(image.filename)
            upload_dir = "static/uploads"
            os.makedirs(upload_dir, exist_ok=True)

            image_path = os.path.join(upload_dir, filename)
            image.save(image_path)

            # TEMP AI OUTPUT (replace with CNN later)
            disease = "Leaf Blight"
            disease_data = {
                "Leaf Blight": {
                    "symptoms": [
                        "Brown or yellow leaf spots",
                        "Drying from leaf edges",
                        "Reduced crop yield"
                    ],
                    "precautions": [
                        "Use resistant seed varieties",
                        "Avoid excess irrigation",
                        "Apply recommended fungicide"
                    ]
                }
            }

            result = {
                "image": image_path,
                "disease": disease,
                "symptoms": disease_data[disease]["symptoms"],
                "precautions": disease_data[disease]["precautions"]
            }

    return render_template("detection.html", result=result)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
