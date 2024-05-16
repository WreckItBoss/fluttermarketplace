import os
import sqlite3

def check_database():
    try:
        # Print current working directory for verification
        print(f"Current working directory: {os.getcwd()}")
        
        # Connect to the SQLite database
        conn = sqlite3.connect('market.db')
        cursor = conn.cursor()

        # Execute a query to fetch all rows from the item table
        cursor.execute("SELECT * FROM item")
        rows = cursor.fetchall()

        # Print the rows to verify the contents
        for row in rows:
            print(row)

        # Close the database connection
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_database()