from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

blog_posts = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is my first post.",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Second Post",
        "content": "This is another post.",
    },
]


@app.route("/")
def index():
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        author = request.form.get("author", default="").strip()
        title = request.form.get("title", default="").strip()
        content = request.form.get("content", default="").strip()

        new_id = max(post["id"] for post in blog_posts) + 1 if blog_posts else 1

        if len(author) > 0 and len(title) > 0 and len(content) > 0:
            blog_posts.append(
                {
                    "id": new_id,
                    "author": author,
                    "title": title,
                    "content": content,
                }
            )
        else:
            return render_template(
                "add.html",
                error="All fields are required.",
                author=author,
                title=title,
                content=content,
            )
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:post_id>")
def delete(post_id):
    found_post = next((post for post in blog_posts if post_id == post["id"]), None)

    if found_post is not None:
        blog_posts.remove(found_post)
        return redirect(url_for("index"))
    else:
        flash("Post not found.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
