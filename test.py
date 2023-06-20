# @app.route('/register', methods=['POST'])
# def createUser():
#     try:
#         data = request.get_json()
#         raw_uuid = str(uuid.uuid4()).split("-")
#         uuid_user = "".join(raw_uuid)
#         nama = data.get('nama')
#         email = data.get('email')
#         password = data.get('password')
#         user = Users(
#                 uuid_user = uuid_user,
#                 nama = nama.lower(),
#                 email = email.lower(),
#                 alamat = "-",
#                 jml_point = 0,
#                 no_telp = "-",
#                 role = "user"
#             )
#         validate_user_email = Users.query.filter_by(email = email).first()
#         if validate_user_email:
#             return jsonify({
#                 'result':'failed',
#                 'message':'email already exists'
#             })
#         else:
#             user.set_password(password)
#             db.session.add(user)
#             db.session.commit()
#             return jsonify({
#                 'result':'success',
#                 'message':'user created successfully'
#             })
#     except Exception as e:
#         return jsonify({
#             'result':'error',
#             'message':str(e)
#         })