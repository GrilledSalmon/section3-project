import csv

from flask import Blueprint, render_template
from flask_app import CSV_FILEPATH

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """
    index 함수에서는 '/' 엔드포인트로 접속했을 때 'index.html' 파일을
    렌더링 해줍니다.

    'index.html' 파일에서 'users.csv' 파일에 저장된 유저 목록을 보여줄 수 있도록
    유저들을 html 파일에 넘길 수 있어야 합니다.

    요구사항:
      - HTTP Method: `GET`
      - Endpoint: `/`

    상황별 요구사항:
      - `GET` 요청이 들어오면 `templates/index.html` 파일을 렌더해야 합니다.

    """
    with open(CSV_FILEPATH) as csv_file:
      user = csv.reader(csv_file)
      user_list = list(user)[1:]

    return render_template('index.html', user_list=user_list), 200


# with open('./mini_flask_app/users.csv') as csv_file:
#       user_list = list(csv.reader(csv_file))[1:]
#       user_dict = {}
#       for user in user_list:
#         user_dict[user[1]] = str(user[0])
# print(user_dict)
