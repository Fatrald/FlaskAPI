from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from config import db

current_time = datetime.now()
formatted_time = current_time.strftime('%d/%m/%Y-%H:%M:%S')
formatted_image = current_time.strftime('%Y%m%d%H%M%S%f')

class Users(db.Model):
    __tablename__ = 'users'

    uuid_user = db.Column(db.String(36), primary_key=True)
    nama = db.Column(db.String(100))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    alamat = db.Column(db.String(255))
    no_telp = db.Column(db.String(15))
    role = db.Column(db.String(5))
    jml_point = db.Column(db.Integer)

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
    
    def user_role(self):
        return "admin" if self.role else "user"
    
    
class Trx(db.Model):
    __tablename__ = 'trx'
    id_trx = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10))
    created = db.Column(db.DateTime)
    uuid_user = db.Column(db.String(32), db.ForeignKey('users.uuid_user'))

    user = db.relationship('Users', foreign_keys=[uuid_user])

class Elektronik(db.Model):
    __tablename__ = 'elektronik'
    id_elektronik = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jns_elektronik = db.Column(db.String(25))
    point = db.Column(db.Integer)

class TrxItem(db.Model):
    __tablename__ = 'trx_item'
    id_trx_item = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jmlh = db.Column(db.Integer)
    uuid_user = db.Column(db.String(32))
    path_image = db.Column(db.String(50))
    id_elektronik = db.Column(db.Integer, db.ForeignKey('elektronik.id_elektronik'))
    id_trx = db.Column(db.Integer, db.ForeignKey('trx.id_trx'))

    elektronik = db.relationship('Elektronik', foreign_keys=[id_elektronik])
    trx = db.relationship('Trx', foreign_keys=[id_trx])
