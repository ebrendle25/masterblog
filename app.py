"""A simple Flask blog application."""

import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)

blog_posts = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is my first post.",
        "likes": 0,
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Second Post",
        "content": "This is another post.",
        "likes": 0,
    },
    {
        "id": 3,
        "author": "Alice Smith",
        "title": "Getting Started with Flask",
        "content": "Building a small web app with Python and Flask is fast and straightforward.",
        "likes": 0,
    },
    {
        "id": 4,
        "author": "Bob Johnson",
        "title": "Clean CSS Architecture",
        "content": "Using CSS variables makes maintaining colors and spacing much easier.",
        "likes": 0,
    },
    {
        "id": 5,
        "author": "Clara Davis",
        "title": "Weekend Hiking Thoughts",
        "content": "Spent the morning on a quiet forest trail before getting back to coding.",
        "likes": 0,
    },
]


@app.route("/")
def index():
    """Render the index page with the list of blog posts."""
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Render the add post page and handle form submission."""
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
                    "likes": 0,
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


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    """Delete a blog post by its ID and redirect to the index page."""
    post = fetch_post_by_id(post_id)
    if post is None:
        flash("Post not found.", "error")
    else:
        blog_posts.remove(post)
        flash("Post deleted.", "success")
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Render the update post page and handle form submission."""
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        author = request.form.get("author", default="").strip()
        title = request.form.get("title", default="").strip()
        content = request.form.get("content", default="").strip()

        if len(author) > 0 and len(title) > 0 and len(content) > 0:
            post.update(
                {
                    "author": author,
                    "title": title,
                    "content": content,
                }
            )
        else:
            return render_template(
                "update.html",
                error="All fields are required.",
                author=author,
                title=title,
                content=content,
                post=post,
            )
        return redirect(url_for("index"))

    flash("Post updated.", "success")
    return render_template("update.html", post=post)


@app.route("/like/<int:post_id>", methods=["POST"])
def like(post_id):
    """Increment the like count for a blog post."""
    post = fetch_post_by_id(post_id)
    if post is not None:
        post["likes"] = post.get("likes", 0) + 1
        flash("Post liked.", "success")
    else:
        flash("Post not found.", "error")
    return redirect(url_for("index"))


def fetch_post_by_id(post_id):
    """Fetch a blog post by its ID."""
    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None


if __name__ == "__main__":
    # Run the Flask application
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5000)
