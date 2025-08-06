from app import create_app, db
from flask_login import LoginManager
from app.models import User

app = create_app()  # ¡Esta línea define la variable app!

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)