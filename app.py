from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "czr_secret_key"

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/services")
def services():
    return render_template("services.html", title="Services")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        print(f"New message from {name} ({email}): {message}")
        flash("Your message has been received. Thank you for contacting CZR Barbour Evolution.")
        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
