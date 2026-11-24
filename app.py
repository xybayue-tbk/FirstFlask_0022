from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    nama = request.form.get("nama", "").strip()
    if nama == "":
        return render_template("index.html", error="Nama tidak boleh kosong."), 400

    return render_template("index.html", nama=nama)


@app.route("/about")
def about():
    return "About us"


@app.route("/user/<username>")
def user(username):
    return f"User: {username}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"


if __name__ == "__main__":
    app.run(debug=True)