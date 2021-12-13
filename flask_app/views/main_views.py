import sqlite3

from flask import Blueprint, render_template
from flask_app import DB_FILEPATH

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """
    index 함수에서는 '/' 엔드포인트로 접속했을 때 'index.html' 파일을 렌더

      - HTTP Method: `GET`
      - Endpoint: `/`

    """
    # 확인 가능한 stock 예시
    conn = sqlite3.connect(DB_FILEPATH)
    cur = conn.cursor()
    cur.execute("SELECT s.name FROM stock_data s;")
    stock_list = [i[0] for i in cur.fetchall()]
    # print(stock_list)

    return render_template('index.html', stock_list=stock_list), 200
