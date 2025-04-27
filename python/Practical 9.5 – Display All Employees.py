import mysql.connector
from tabulate import tabulate

def display_employees():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rdnc",
            database="fycs"
        )
        
        if con.is_connected():
            cursor = con.cursor()
            cursor.execute("SELECT * FROM employee")
            records = cursor.fetchall()
            
            if records:
                print(tabulate(records, headers=["EmpNo", "Name", "Dept"], 
                             tablefmt="grid"))
            else:
                print("No records found")
                
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()

if __name__ == "__main__":
    display_employees()
