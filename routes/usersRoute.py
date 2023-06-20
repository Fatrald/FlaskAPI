from flask import Blueprint, jsonify, request
from config import app, db
from models import Users, Trx, TrxItem
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



# @app.route('/users/<int:id_card>', methods=['PUT'])
# def updateUser(id_card):
#     try:
#         data = request.get_json()
#         user = UserModel.query.filter_by(id_card=id_card).first()
#         validate_user_email = UserModel.query.filter_by(email=data.get('email')).first()
#         if not user:
#             return jsonify({
#                 'result': 'error',
#                 'message': 'User Not Found'
#             })
    
#         if validate_user_email:
#             return jsonify({
#                 'result': 'error',
#                 'message': 'Email Already Exists'
#             })
#         user.name = data.get('name', user.name)
#         user.email = data.get('email', user.email)
#         user.set_password(data.get('password', user.password))
#         user.telp = data.get('telp', user.telp)
#         user.company = data.get('company', user.company)
#         db.session.commit()
#         return jsonify({
#             'result': 'success',
#             'message': 'User Updated Successfully'
#         })
#     except Exception as e:
#         return jsonify({
#             'result': 'error',
#             'message': str(e)
#         })

# @app.route('/login', methods=['POST'])
# def loginUser():
#     data = request.get_json()
#     user = UserModel.query.filter_by(email=data.get('email')).first()
#     passwordCheck = user.check_password(data.get('password'))
#     if not passwordCheck:
#         return jsonify({
#             'result':'error',
#             'message':'Wrong Password'
#         })
#     elif user:
#         return jsonify({
#             'result':'error',
#             'message':'Email doesn`t found'
#         })
#     else:
#         return jsonify({
#             'result':'success',
#             'message':'Login Successfuly'
#         })








