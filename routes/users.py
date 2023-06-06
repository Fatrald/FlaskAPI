from flask import Blueprint, jsonify, request
from config import db
from models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data['name'],
        email = data['email'],
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(
        {
            'message':'User Created Successfully'
        }
    )
@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'name':user.name,
            'email':user.email,
            'address':user.address,
            'no_telp':user.no_telp,
            'profile_image': user.profile_image,
            'role':user.role
        }
        user_list.append(user_data)
    return jsonify({'users':user_list})

@users_bp.route('/users/email', methods=['GET'])
def get_user_email():
    email = request.args.get('email')
    if email:
        user = User.query.filter_by(email=email).first()
        if user:
            user_data = {
                'name':user.name,
                'email':user.email,
                'address':user.address,
                'no_telp':user.no_telp,
                'profile_image': user.profile_image,
                'role':user.role
            }
            return jsonify({'user': user_data})
        else:
            return jsonify({'message': 'User not found.'}), 404
    else:
        return jsonify({'message': 'Email parameter is missing.'}), 400
    
@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully.'})
    else:
        return jsonify({'message': 'User not found.'}), 404
    
@users_bp.route('/users/edit', methods=['PUT'])
def update_user_by_email():
    email = request.args.get('email')
    if email:
        user = User.query.filter_by(email=email).first()
        if user:
            data = request.get_json()
            user.name = data.get('name', user.name)
            user.address = data.get('address', user.address)
            user.no_telp = data.get('no_telp', user.no_telp)
            user.profile_image = data.get('profile_image', user.profile_image)
            user.role = data.get('role', user.role)

            db.session.commit()
            return jsonify({'message': 'User updated successfully.'})
        else:
            return jsonify({'message': 'User not found.'}), 404
    else:
        return jsonify({'message': 'Email parameter is missing.'}), 400