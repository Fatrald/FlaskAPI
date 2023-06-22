from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://coco:Password123@localhost/ecotronik'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
db = SQLAlchemy(app)