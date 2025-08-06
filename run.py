from app import create_app, db
from flask_login import LoginManager
from app.models import User

# Esta variable 'app' DEBE existir en el nivel global
app = create_app()

# Crea las tablas de la base de datos si no existen
with app.app_context():
    db.create_all()

# Solo para desarrollo local, NO se usa en producción con Gunicorn
if __name__ == '__main__':
    app.run(debug=True)