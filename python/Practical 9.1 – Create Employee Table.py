import mysql.connector

def create_employee_table():
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
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS employee (
                empno INT PRIMARY KEY,
                ename VARCHAR(20),
                dept VARCHAR(20)
            """
            
            cursor.execute(create_table_query)
            con.commit()
            print("Employee table created successfully")
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()

if __name__ == "__main__":
    create_employee_table()
