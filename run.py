from app import create_app, db
from app.models import User, Post
from flask.cli import with_appcontext
import click

app = create_app()

@click.command("init-db")
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo("Database initialized.")

app.cli.add_command(init_db_command)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
