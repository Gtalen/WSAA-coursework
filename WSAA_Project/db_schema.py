"""
---------------------------------------------------------------
Database Schema for the Investment Portfolio Management System
---------------------------------------------------------------
Author: Ebelechukwu Igwagu
---------------------------------------------------------------
This module defines the database schema for the Investment Portfolio Management System.
"""

# Import necessary libraries
import pymysql
import sql_connect

# Function to create the database schema

def create_database_schema():
    conn = sql_connect.connect_mysql()  # Connect to MySQL
    if conn:
        try:
            with conn.cursor() as cursor:
                # Create database if it doesn't exist
                query = "CREATE DATABASE IF NOT EXISTS investment_portfolio_db;"
                cursor.execute(query)
                print("Database created successfully.")
            
            conn.commit()
        except pymysql.MySQLError as e:
            print(f"Error creating database: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")

def main():
    create_database_schema()  # Call your schema creation function

if __name__ == "__main__":
    main()
