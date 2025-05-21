from pathlib import Path
import pymysql
import sql_connect
import json




def load_stocks_json():
    file_path = Path(__file__).parent / "stocks.json"
    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
        return data["finance"]["result"][0]["quotes"]

def generate_stocks_data():
    stocks = load_stocks_json()
    conn = sql_connect.connect_mysql()
    if conn:
        try:
            stocks_data = []
            for stock in stocks:
                symbol = stock.get("symbol")
                short_name = stock.get("displayName")
                company_name = stock.get("longName")
                stocks_data.append((symbol, short_name, company_name))

            with conn.cursor() as cursor:
                query = """
                INSERT IGNORE INTO stocks (stock_symbol, stock_short_name, stock_company_name)
                VALUES (%s, %s, %s)
                """
                cursor.executemany(query, stocks_data)
                conn.commit()
                print("Stock data inserted successfully and duplicates were ignored.")
        except pymysql.MySQLError as e:
            print(f"Error inserting stock data: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")




