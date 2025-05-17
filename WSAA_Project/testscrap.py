# Import necessary libraries
import pymysql
import sql_connect


def check_database_exists(db_name="investment_portfolio_db"):
    conn = sql_connect.connect_mysql()
    if conn:
        try:
            with conn.cursor() as cursor:
                # Query to show databases matching the name
                cursor.execute("SHOW DATABASES LIKE %s;", (db_name,))
                result = cursor.fetchone()
                if result:
                    print(f"Database '{db_name}' exists.")
                    return True
                else:
                    print(f"Database '{db_name}' does not exist.")
                    return False
        except pymysql.MySQLError as e:
            print(f"Error checking database: {e}")
            return False
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")
        return False


def main():
    check_database_exists()
if __name__ == "__main__":
    main()
   