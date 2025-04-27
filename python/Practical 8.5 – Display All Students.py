import mysql.connector
from tabulate import tabulate

def display_all_students():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rdnc",
            database="fycs"
        )
        
        if con.is_connected():
            print("Connected to MySQL database")
            cursor = con.cursor()
            
            # Select all records
            select_query = "SELECT * FROM student"
            cursor.execute(select_query)
            records = cursor.fetchall()
            
            if records:
                # Display records in tabular format
                headers = ["Roll No", "Name", "Class"]
                print(tabulate(records, headers=headers, tablefmt="grid"))
            else:
                print("No records found in student table")
                
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    display_all_students()
