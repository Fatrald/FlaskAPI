from config import app
from routes.usersRoute import users_bp

app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)


