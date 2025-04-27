import mysql.connector

def insert_employee_records():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rdnc",
            database="fycs"
        )
        
        if con.is_connected():
            cursor = con.cursor()
            records = [
                (101, "Ravi", "HR"),
                (102, "Sneha", "Finance")
            ]
            
            cursor.executemany("INSERT INTO employee VALUES (%s, %s, %s)", records)
            con.commit()
            print(f"{cursor.rowcount} records inserted")
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()

if __name__ == "__main__":
    insert_employee_records()
