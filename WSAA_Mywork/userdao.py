import pymysql
import sql_connect  # Connect to MySQL database


# ----------------------
# User DAO - CRUD Logic
# ----------------------

def create_user(user_data):
    """
    Inserts a new user into the database.
    user_data = (username, email, created_at)
    """
    conn = sql_connect.connect_mysql()
    try:
        with conn.cursor() as cursor:
            query = """
                INSERT INTO users (username, email, created_at)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, user_data)
            conn.commit()
            return cursor.lastrowid  # Return the new user's ID
    except pymysql.MySQLError as e:
        print(f"[ERROR] create_user: {e}")
        conn.rollback()
    finally:
        conn.close()


def get_user_by_id(user_id):
    """
    Fetches a user by ID.
    """
    conn = sql_connect.connect_mysql()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            return cursor.fetchone()
    except pymysql.MySQLError as e:
        print(f"[ERROR] get_user_by_id: {e}")
    finally:
        conn.close()


def update_user_email(user_id, new_email):
    """
    Updates a user's email.
    """
    conn = sql_connect.connect_mysql()
    try:
        with conn.cursor() as cursor:
            query = "UPDATE users SET email = %s WHERE user_id = %s"
            cursor.execute(query, (new_email, user_id))
            conn.commit()
            return cursor.rowcount  # Number of rows updated
    except pymysql.MySQLError as e:
        print(f"[ERROR] update_user_email: {e}")
        conn.rollback()
    finally:
        conn.close()


def delete_user(user_id):
    """
    Deletes a user from the database.
    """
    conn = sql_connect.connect_mysql()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
            return cursor.rowcount
    except pymysql.MySQLError as e:
        print(f"[ERROR] delete_user: {e}")
        conn.rollback()
    finally:
        conn.close()
