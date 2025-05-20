"""
-----------------------------------------------------------------------
Data Generation for the Financial Investment Portfolio database tables
-----------------------------------------------------------------------
Author: Ebelechukwu Igwagu
--------------------------------
This script generates data using the Faker library for the user table and
data from the  stocks table.
"""
from datetime import datetime
from pathlib import Path
import random
import json
import pymysql
from faker import Faker
import sql_connect
import db_data_import


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

def generate_transaction_data():
    stocks = db_data_import.load_stocks_json()  # Load stock data from JSON file
    conn = sql_connect.connect_mysql()  # Connect to MySQL

    if not conn:
        print("Failed to connect to the database.")
        return

    try:
        with conn.cursor() as cursor:
            # Get user IDs and creation dates
            cursor.execute("SELECT user_id, created_at FROM users ORDER BY user_id;")
            user_data = cursor.fetchall()
            user_creation_dates = {row["user_id"]: row["created_at"] for row in user_data}

            # Get stock IDs
            cursor.execute("SELECT stock_id FROM stocks ORDER BY stock_id;")
            stock_ids = [row["stock_id"] for row in cursor.fetchall()]

            # Get prices from loaded json stock data
            stock_prices = [stock.get("regularMarketPrice") for stock in stocks]
            stock_price_map = dict(zip(stock_ids, stock_prices))  # Create a mapping of stock_id to price

            transactions = []

            for user_id, created_at in user_creation_dates.items():
                num_transactions = random.randint(5, 10)  # Generate 5 to 10 transactions per user

                for _ in range(num_transactions):
                    stock_id = random.choice(stock_ids)

                    # Weighted random choice: 60% buy, 40% sell
                    transaction_type = random.choices(["buy", "sell"], weights=[0.6, 0.4])[0]

                    quantity = random.randint(1, 100)

                    # Price simulation ±30%
                    base_price = stock_price_map.get(stock_id, 100)
                    price_per_share = round(base_price * random.uniform(0.7, 1.3), 2)

                    # Generate a transaction date between account creation date and now
                    transaction_date = fake.date_time_between(
                        start_date=created_at, end_date=datetime.now()
                    )

                    # Store transaction
                    transactions.append((
                        user_id,
                        stock_id,
                        transaction_type,
                        quantity,
                        price_per_share,
                        transaction_date
                    ))

            # Insert data into the transactions table
            query = """
                INSERT INTO transactions (user_id, stock_id, transaction_type, quantity, price_per_share, transaction_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.executemany(query, transactions)
            conn.commit()
            print(f"Added {len(transactions)} transactions to the transaction table successfully.")

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
    finally:
        conn.close()






def main():
    generate_user_data()  # Generate and insert user data
    generate_stocks_data()  # Generate and insert stock data
    generate_transaction_data()  # Generate and insert transaction data

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
