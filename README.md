
# News Site (Flask)

A simple, secure news website where you can post articles with images and videos. Includes admin login.

## Quick Start

1. **Download & Extract**
   - Download the ZIP from your chat, extract it.

2. **Create `.env`**
   - Copy `.env.example` to `.env` and keep/change values.
   - Default admin credentials are:
     - **Username:** `admin`
     - **Password:** `ZNMmQVw@gXhth)kj`
   - Change them after first login.

3. **Set up Python & install deps**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python run.py
   ```
   Visit http://127.0.0.1:5000

## Features

- Admin authentication (Flask-Login)
- Create, edit, delete posts
- Upload **images** (png, jpg, jpeg, gif, webp)
- Upload **videos** (mp4, webm, ogg, mov, mkv) up to 100MB each
- Bootstrap 5 responsive UI
- SQLite database (file `site.db`)
- CSRF protection

## File Structure

```
news_site_flask/
  app/
    templates/
    static/
    __init__.py
    models.py
    routes.py
    forms.py
    utils.py
  uploads/
  .env.example
  config.py
  requirements.txt
  run.py
  README.md
```

## Deployment (optional)

- On services like Render, Railway, or a VPS:
  - Set environment variables from `.env` securely.
  - Use `gunicorn run:app` as the start command.
  - Ensure a writable `UPLOAD_FOLDER` and persistent storage for uploads.
  - Put a reverse proxy (Nginx) in front to serve `/uploads` efficiently.

## Security Notes

- **Change** `SECRET_KEY`, `ADMIN_PASSWORD`, and preferably the `ADMIN_USERNAME`.
- Restrict who can access the admin URL.
- Consider using HTTPS in production.
