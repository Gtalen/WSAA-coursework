"""
--------------------------------
Fake Data Generation
--------------------------------
Author: Ebelechukwu Igwagu
--------------------------------
This script generates fake data using the Faker library.
"""
from datetime import datetime, timedelta
from pathlib import Path
import random
from faker import Faker
import pymysql
import sql_connect
import json

# Initialize Faker
fake = Faker(["en_IE", "en_US", "en_GB"])
Faker.seed(10)

email_domains = ["example.com", "yahoo.com", "hotmail.com", "gmail.com", "outlook.com"]

def generate_user_data(num_users=50):
    conn = sql_connect.connect_mysql()  # Connect to MySQL
    if conn:
        try:
            users = []
            for _ in range(num_users):
                first_name = fake.unique.first_name()
                last_name = fake.unique.last_name()
                fullname = f"{first_name} {last_name}"
                username = fake.unique.user_name()
                email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(email_domains)}"
                password_hash = fake.sha256()
                dob = fake.date_of_birth(minimum_age=18, maximum_age=70)
                created_at = fake.date_time_between(start_date='-2y', end_date='now')

                users.append((fullname, username, email, password_hash, dob, created_at))

            with conn.cursor() as cursor:
                query = """
                INSERT IGNORE INTO users (fullname, username, email, password_hash, dob, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.executemany(query, users)
                conn.commit()
                print("User data inserted successfully and duplicates were ignored.")
        except pymysql.MySQLError as e:
            print(f"Error inserting user data: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")

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







def main():
    generate_user_data()  # Generate and insert user data
    generate_stocks_data()  # Generate and insert stock data

if __name__ == "__main__":
    main()

"""
---------------------------------------
References:
---------------------------------------

- DataCamp. (n.d.). *Creating Synthetic Data with Python and Faker*. [online] Available at: https://www.datacamp.com/tutorial/creating-synthetic-data-with-python-faker-tutorial [Accessed 18 May 2025].

- Faker (2025). *Using the Faker Class*. [online] Available at: https://pypi.org/project/Faker/ [Accessed 18 May 2025].

- Faker documentation. (n.d.). *Faker 37.3.0 Documentation*. [online] Available at: https://faker.readthedocs.io/en/master/fakerclass.html [Accessed 18 May 2025].
"""
