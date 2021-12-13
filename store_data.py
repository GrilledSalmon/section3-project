# pull_data.py에서 가져온 데이터를 DB에 저장합니다.
import sqlite3
from pull_data import data

DB_PATH = "./flask_app/stock_DB.db"
conn = sqlite3.connect(DB_PATH)

# 데이터 db에 저장!
data.to_sql('stock_data', conn, if_exists='replace', index=False)

if __name__ == "__main__":
    print(data.head())