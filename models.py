import enum
from config import db
import hashlib

class User(db.Model):
    __tablename__= 'tb_user'
    id_user = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    address = db.Column(db.String(100), default='')
    no_telp = db.Column(db.String(15), default='')
    profile_image = db.Column(db.String(100), default='')
    role = db.Column(db.String(10), default='user')

    def set_password(self, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.password = hashed_password

    def check_password(self, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return self.password == hashed_password