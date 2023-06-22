from flask import Blueprint, jsonify, request
from config import app, db
from models import Users, Trx, TrxItem, Elektronik
from datetime import datetime

transaksi_bp = Blueprint('trx', __name__)
current_time = datetime.now()
format_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/transaksi', methods=['POST'])

@app.route('/transaksi', methods=['GET'])
def getAllTransaksi():
    trx = Trx.query.all()
    trx_list = []
    for trx_item in trx:
        trx_data = {
            "id_trx": trx_item.id_trx,
            "status": trx_item.status,
            "created": trx_item.created
        }
        trx_list.append(trx_data)
    return jsonify({
        "result":"success",
        "data":trx_list
        })