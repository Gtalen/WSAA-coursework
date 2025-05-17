"""
MySQL Queries Script
---------------------------
Author: Ebelechukwu Igwagu
---------------------------
This script contains various functions for executing MySQL queries related
to the actors, directors, and other data stored in the appDBproj database.
"""

# Import dependencies
from dateutil import parser
import datetime
import pymysql
import sql_connect


# FUNCTION TO VIEW FILMS BY DIRECTOR
# This function connects to the MySQL database and retrieves films directed by a specific director

def view_directors_films():
    director = input("Enter part or full name of the director: ")

# Call the function to connect to MySQL database
    conn = sql_connect.connect_mysql()  
    
    if conn:
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT d.DirectorName, f.FilmName, s.StudioName
                    FROM director d
                    INNER JOIN film f ON f.FilmDirectorID = d.DirectorID
                    INNER JOIN studio s ON f.FilmStudioID = s.StudioID
                    WHERE d.DirectorName LIKE %s
                    ORDER BY d.DirectorName, f.FilmName;                """
                
                cursor.execute(query, ('%' + director + '%',))
                results = cursor.fetchall()

                #print("Query executed. Rows returned:", len(results))
                print("\nFilm Details For : ", director)
                print("-" * 100) # Print a separator line
                print(f"{'Director':<30} | {'Film':40} | {'Studio':<20}") # Column headers
                print("-" * 100) 
                
                if results:
                    for row in results:
                        print(f"{row['DirectorName']:<30} | {row['FilmName']:<40} | {row['StudioName']}")
                else:
                    print("No directors found of that name.")
        except Exception as e:
            print("An error occurred during query execution:", e)
        finally:
            conn.close()
    else:
        print("Database connection failed.")

# FUNCTION TO VIEW ACTORS BORN IN A SPECIFIC MONTH
# Function to get month from user input
# This function prompts the user to enter a month as a number (1-12) or a 3-letter abbreviation (e.g., Jan, Feb, etc.)

def get_month():
    while True:
        month = input("Please enter a number (1–12) or a 3-letter month abbreviation: ").strip()

        # If user input is a number
        if month.isdigit():
            month_num = int(month)
            if 1 <= month_num <= 12:
                return month_num
            else:
                print("Invalid month. Please enter a number between 1 and 12.")

        # If user input is a 3-letter month abbreviation
        elif len(month) == 3:
            month_abbr = month.lower()
            month_dict = {
                'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
                'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
                'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
            }
            if month_abbr in month_dict:
                return month_dict[month_abbr]
            else:
                print("Invalid month name abbreviation. Please use Jan, Feb, Mar, etc.")

        else:
            print("Invalid input. Please enter a number (1–12) or a 3-letter month abbreviation.")


# Function to view actors born in a specific month
# This function connects to the MySQL database and retrieves actors born in the specified month
# It uses the get_month function to get the month from user input

def view_actors_month_dob():     
    month_dob= get_month()  # Get month from user input  

    # Call the function to connect to MySQL database
    conn = sql_connect.connect_mysql()  # Connect to MySQL database

    if conn:
        try:
            with conn.cursor() as cursor:
                query = """
                SELECT ActorName, DATE_FORMAT(ActorDOB, '%%Y-%%m-%%d') AS ActorDOB, ActorGender
                FROM actor
                WHERE MONTH(ActorDOB) = %s;
                """
                #print("Running query...")
                cursor.execute(query, (month_dob,))
                results = cursor.fetchall()

                #print("Query executed. Rows returned:", len(results))
                print(f"\nActors born in month: {month_dob}")
                print("-" * 80) # Print a separator line
                print(f"{'ActorName':<40} | {'ActorDOB':<20} | {'ActorGender':<20}") # Column headers
                print("-" * 80)
                
                if results:
                    for row in results:
                        print(f"{row['ActorName']:<40} | {row['ActorDOB']:<20} | {row['ActorGender']:<20}")
                else:
                    print("No actor born in that month.")
        except Exception as e:
            print("An error occurred during query execution:", e)
        finally:
            conn.close()
    else:
        print("Database connection failed.")




# ADD NEW ACTOR TO MYSQL DATABASE
# This function connects to the MySQL database and adds a new actor based on user input
def add_new_actor():
    conn = sql_connect.connect_mysql()
    if not conn: # Check if connection to MySQL was successful
        print("Connection to MYSQL failed.")
        return

    try:
        # Get and validate user inputs
        try:
            actor_id = int(input("Enter Actor ID: "))
        except ValueError:
            print("Invalid Actor ID; Please enter as digits eg 1,2,3...")
            return

        actor_name = input("Enter Actor Name: ").strip()
        
        # Get Actor DOB and standardizes the date format
        dob = input("Enter Actor DOB (YYYY-MM-DD): ")
        try:
            dob_parse = parser.parse(dob, dayfirst=True).date() # Convert to date object
            actor_dob = dob_parse.strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD  e.g., 2000-07-25.")
            return

        # Normalize input
        gender = input("Enter Actor Gender (Male/Female): ").strip().lower() # Convert to lowercase for consistency
        if gender in ("male", "m"):
            actor_gender = "Male"
        elif gender in ("female", "f"):
            actor_gender = "Female"
        else:
            print("Invalid gender. Please enter 'Male' or 'Female'.")
            return


        try:
            actor_country_id = int(input("Enter Actor Country ID: "))
        except ValueError:
            print("Invalid Country ID.")
            return

        # Check if Actor ID already exists
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM Actor WHERE ActorID = %s", (actor_id,))
            if cursor.fetchone():
                print(f"*** ERROR *** Actor ID: {actor_id} already exists")
                return

            # Check if Country ID exists
            cursor.execute("SELECT 1 FROM Country WHERE CountryID = %s", (actor_country_id,))
            if not cursor.fetchone():
                print(f"*** ERROR *** Country ID: {actor_country_id} does not exist")
                return

            # Add New Actor from the user input to MySQL database
            query = """
            INSERT INTO Actor (ActorID, ActorName, ActorDOB, ActorGender, ActorCountryID)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (actor_id, actor_name, actor_dob, actor_gender, actor_country_id))
            conn.commit() # Commit the transaction      
            print("Actor successfully added.")

    except Exception as e:
        print("ERROR:", e)
    finally:
        conn.close()

# FUNCTION TO VIEW STUDIOS
def view_studios():
    # Connect to MySQL database
    conn = sql_connect.connect_mysql()
    
    if conn:
        try:
            with conn.cursor() as cursor:
                query = """
                SELECT StudioID, StudioName
                FROM Studio
                ORDER BY StudioID;
                """
                cursor.execute(query)
                results = cursor.fetchall()
                
                print("-" * 50)
                print(f"{'Studio ID':<10} | {'Studio Name':40}")
                print("-" * 50)

                if results:
                    for row in results:
                        print(f"{row['StudioID']:<10} | {row['StudioName']:<40}")
                else:
                    print("No studios found.")
        except Exception as e:
            print("An error occurred during query execution:", e)
        finally:
            conn.close()
    else:
        print("Database connection failed.")




# Main function to run the script

def main():
    view_directors_films() # Call the function to view films by director
    view_actors_month_dob() # Call the function to view actors born in a specific month
    add_new_actor() # Call the function to add a new actor
    view_studios()  # Call the function to view studios

if __name__ == "__main__":
    main()




# References:
# •	Jchris (no date) portable-google-app-engine-sdk/lib/django/django/utils/dates.py at e2cabe70d1210dc2f6a8f20f4046ef3c394f6cac · jchris/portable-google-app-engine-sdk. https://github.com/jchris/portable-google-app-engine-sdk/blob/e2cabe70d1210dc2f6a8f20f4046ef3c394f6cac/lib/django/django/utils/dates.py.
















































