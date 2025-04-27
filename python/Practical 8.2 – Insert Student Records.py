import mysql.connector

def insert_student_records():
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
            
            # Insert records
            insert_query = "INSERT INTO student (srollno, sname, class) VALUES (%s, %s, %s)"
            records = [
                (1, "Riya", "FYBSc"),
                (2, "Ravi", "FYBCom")
            ]
            
            cursor.executemany(insert_query, records)
            con.commit()
            print(f"{cursor.rowcount} records inserted successfully")
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    insert_student_records()
