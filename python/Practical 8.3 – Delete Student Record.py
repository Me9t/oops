import mysql.connector

def delete_student_record():
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
            
            # Get roll number from user
            roll_no = input("Enter the roll number of the student to delete: ")
            
            # Delete record
            delete_query = "DELETE FROM student WHERE srollno = %s"
            cursor.execute(delete_query, (roll_no,))
            con.commit()
            
            if cursor.rowcount > 0:
                print(f"Student with roll number {roll_no} deleted successfully")
            else:
                print(f"No student found with roll number {roll_no}")
                
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    delete_student_record()
