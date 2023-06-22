from config import app
from routes.usersRoute import users_bp
from routes.transaksiRoute import transaksi_bp

app.register_blueprint(users_bp)
app.register_blueprint(transaksi_bp)

if __name__ == '__main__':
    app.run(debug=True)


