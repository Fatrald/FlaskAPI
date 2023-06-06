from config import app
from routes.users import users_bp
from routes.utils import error_bp

app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)


