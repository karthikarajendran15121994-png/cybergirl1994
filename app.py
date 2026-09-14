from flask import Flask, render_template, request
import re

app = Flask(__name__)


def check_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[@#$%!]', password))

    criteria_met = sum([
        length_ok,
        has_upper,
        has_lower,
        has_digit,
        has_special
    ])

    if criteria_met == 5:
        return "Strong 💪"
    elif criteria_met >= 3:
        return "Medium 🙂"
    else:
        return "Weak ❌"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form.get("password", "")

        if password:
            result = check_password_strength(password)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)