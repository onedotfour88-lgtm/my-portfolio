from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

PROFILE_FILE = "profile.json"


def load_profile():

    with open(
        PROFILE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_profile(profile):

    with open(
        PROFILE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            ensure_ascii=False,
            indent=2
        )


@app.route("/")
def index():

    profile = load_profile()

    return render_template(
        "index.html",
        profile=profile
    )


@app.route("/edit", methods=["GET", "POST"])
def edit():

    profile = load_profile()

    if request.method == "POST":

        # 기본 개인정보 공개 여부

        profile["name"]["public"] = (
            "name_public" in request.form
        )

        profile["age"]["public"] = (
            "age_public" in request.form
        )

        profile["gender"]["public"] = (
            "gender_public" in request.form
        )

        profile["email"]["public"] = (
            "email_public" in request.form
        )

        profile["phone"]["public"] = (
            "phone_public" in request.form
        )

        profile["address"]["public"] = (
            "address_public" in request.form
        )

        save_profile(profile)

        return redirect("/edit?saved=1")

    return render_template(
        "edit.html",
        profile=profile
    )


if __name__ == "__main__":
    app.run(debug=True)