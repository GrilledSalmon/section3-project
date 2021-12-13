import csv
import os
import pickle
import sqlite3
import warnings
from flask import Blueprint, request
from flask_app import DB_FILEPATH, MODEL_FILEPATH
warnings.filterwarnings(action='ignore')

with open(MODEL_FILEPATH, 'rb') as pickle_file:
    stock_pred_model = pickle.load(pickle_file)


pred_bp = Blueprint('pred', __name__)

@pred_bp.route('/pred')
def get_pred():
    """
    get_pred 함수는 `stockname` 을 키로 한 값을 쿼리 파라미터 값으로 넘겨주면 
    해당 값을 가진 pred결과를 리턴

      - HTTP Method: `GET`
      - Endpoint: `/api/pred`

    """
    stockname = request.args.get("stockname")
    # print('stockname :', stockname)

    conn = sqlite3.connect(DB_FILEPATH)
    cur = conn.cursor()
    cur.execute(f"""
        SELECT "12개월 간 수익률", "KOSPI대비 12개월 간 수익률" , "12개월 간 KOSPI 이김" , PER_inv , PBR_inv , "배당수익률"
        FROM stock_data sd
        WHERE sd.name = '{stockname}';
    """)
    try:
      stock_data = [list(cur.fetchone())]
    except:
      stock_data = None
    # print('stock data입니다', stock_data)

    if stockname == None:
      return "No stockname given", 400

    elif stock_data == None:
      return f"User '{ stockname }' doesn't exist", 404

    else:
      pred_res = stock_pred_model.predict_proba(stock_data)[:, 1][0]
      # pred_res = str(pred_res)
      # print(pred_res)

      message = f"""당신의 종목이 6개월 뒤 코스피보다 많이 상승할 확률은 {pred_res*100:.2f}% 입니다!"""
      print(message)
      return message, 200

