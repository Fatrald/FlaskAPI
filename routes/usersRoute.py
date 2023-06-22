from flask import Blueprint, jsonify, request
from config import app, db
from models import Users, Trx, TrxItem, Elektronik
from datetime import datetime
import uuid

users_bp = Blueprint('users', __name__)
current_time = datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/register', methods=['POST'])
def createUser():
    try:
        data = request.get_json()
        raw_uuid = str(uuid.uuid4()).split("-")
        uuid_user = "".join(raw_uuid)
        nama = data.get('nama')
        email = data.get('email')
        password = data.get('password')
        user = Users(
                uuid_user = uuid_user,
                nama = nama.lower(),
                email = email.lower(),
                alamat = "-",
                jml_point = 0,
                no_telp = "-",
                role = "user"
            )
        validate_user_email = Users.query.filter_by(email = email).first()
        if validate_user_email:
            return jsonify({
                'result':'failed',
                'message':'email already exists'
            })
        else:
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'result':'success',
                'message':'user created successfully'
            })
    except Exception as e:
        return jsonify({
            'result':'error',
            'message':str(e)
        })

@app.route('/login', methods=['POST'])
def loginUser():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = Users.query.filter_by(email=email).first()
        if user:
            verified = user.check_password(password)
            if verified:
                return jsonify({
                    "result":"success",
                    "message":"login success",
                    "uuid":user.uuid_user
                })
            else:
                return jsonify({
                    "result":"failed",
                    "message":"password incorrect"
                })
        else:
            return jsonify({
                "result":"failed",
                "message":"user not found"
            })
    except Exception as e:
        return jsonify({
            "result":"error",
            "message":str(e)
        })

@app.route('/users', methods=['GET'])
def getUsers():
    try:
        users = Users.query.all()
        user_list = []
        for user in users:
            transaction = Trx.query.filter_by(uuid_user=user.uuid_user).all()
            user_data = {
                'uuid_user': user.uuid_user,
                'nama': user.nama,
                'email': user.email,
                'alamat': user.alamat,
                'no_telp': user.no_telp,
                'jml_point': user.jml_point,
                'jml_trx': len(transaction),
                'detail_trx': transaction
            }
            user_list.append(user_data)
        return jsonify({
            'result': 'success',
            'users': user_list
        })
    except Exception as e:
        return jsonify({
            'result': 'error',
            'message': str(e)
        })

@app.route('/users/<string:uuid>', methods=['GET'])
def getUserByUUID(uuid):
    try:
        user = Users.query.filter_by(uuid_user=uuid).first()
        transaction = Trx.query.filter_by(uuid_user=uuid).all()
        if user:
            user_data = {
                'nama':user.nama,
                'email':user.email,
                'alamat':user.alamat,
                'no_telp':user.no_telp,
                'jml_point':user.jml_point,
                'jml_trx':len(transaction),
                'detail_trx': transaction
            }
            return jsonify({
                'result':'success',
                'user':user_data
            })
        else:
            return jsonify({
                'result':'failed',
                'message':'user not found'
            })
    except Exception as e:
        return jsonify({
            'result':'error',
            'message':str(e)
        })

@app.route('/users/<string:uuid>', methods=['PUT'])
def updateUserByUUID(uuid):
    try:
        data = request.get_json()
        user = Users.query.filter_by(uuid_user=uuid).first()
        validate_user_email = Users.query.filter_by(email = data.get('email')).first()
        if not user:
            return jsonify({
                'result':'failed',
                'message':'user not found'
            })
        
        elif validate_user_email:
            return jsonify({
                'result':'failed',
                'message':'email already exists'
            })
        else:
            user.nama = data.get('nama', user.nama)
            user.alamat = data.get('alamat', user.alamat)
            user.email = data.get('email', user.email)
            user.no_telp = data.get('no_telp', user.no_telp)
            user.jml_point = data.get('jml_point',user.jml_point)
            db.session.commit()
            return jsonify({
                'result':'success',
                'message':'user updated successfully'
            })
    except Exception as e:
        return jsonify({
            'result':'error',
            'message':str(e)
        })
