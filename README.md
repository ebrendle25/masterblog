# Masterblog

A small blog application built with Flask. Posts can be created, edited, deleted and liked through a simple web interface.

## Features

- List all blog posts on the start page
- Create new posts with author, title and content
- Edit existing posts
- Delete posts (with a confirmation dialog)
- Like posts and show the like count
- Form validation: empty or whitespace-only fields are rejected
- Feedback via flash messages, e.g. when a post does not exist
- Shared base template with navigation for all pages
- CSRF protection for all POST forms and state-changing actions via Flask-WTF

## Tech Stack

- Python 3
- Flask (routing, Jinja2 templates, flash messages)
- python-dotenv (configuration via `.env`)
- HTML and CSS
- Flask-WTF (CSRF protection)

## Project Structure

```
masterblog/
├── app.py              # Flask app and routes
├── requirements.txt
├── .env.example        # Template for environment variables
├── static/
│   └── style.css
└── templates/
    ├── base.html       # Shared layout and navigation
    ├── index.html      # List of posts
    ├── add.html        # Form for new posts
    └── update.html     # Form for editing a post
```

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd masterblog
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment

Copy the example file and set your own secret key:

```bash
cp .env.example .env
```

| Variable      | Description                                   | Example             |
| ------------- | --------------------------------------------- | ------------------- |
| `SECRET_KEY`  | Key Flask uses to sign the session (required) | a long random string |
| `FLASK_DEBUG` | `1` enables debug mode with auto reload       | `0`                 |

A secure key can be generated with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Start the application

```bash
python app.py
```

The blog is then available at <http://127.0.0.1:5000>.

## Routes

| Route                 | Method    | Description                  |
| --------------------- | --------- | ---------------------------- |
| `/`                   | GET       | Show all posts               |
| `/add`                | GET, POST | Show the form / create post  |
| `/update/<post_id>`   | GET, POST | Show the form / update post  |
| `/delete/<post_id>`   | POST      | Delete a post                |
| `/like/<post_id>`     | POST      | Add a like to a post         |


## Background

This project was created as part of a software engineering course to practise Flask routing, templates, form handling and template inheritance.
