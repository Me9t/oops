import mysql.connector

def update_student_name():
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
            
            # Get input from user
            roll_no = input("Enter the roll number of the student: ")
            new_name = input("Enter the new name of the student: ")
            
            # Update record
            update_query = "UPDATE student SET sname = %s WHERE srollno = %s"
            cursor.execute(update_query, (new_name, roll_no))
            con.commit()
            
            if cursor.rowcount > 0:
                print(f"Student with roll number {roll_no} updated successfully")
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
    update_student_name()
