import mysql.connector

def create_student_table():
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
            
            # Create table query
            create_table_query = """
            CREATE TABLE IF NOT EXISTS student (
                srollno INT PRIMARY KEY,
                sname VARCHAR(20),
                class VARCHAR(20)
            """
            
            cursor.execute(create_table_query)
            con.commit()
            print("Student table created successfully")
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    create_student_table()
