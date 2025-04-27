import mysql.connector

def update_employee_name():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rdnc",
            database="fycs"
        )
        
        if con.is_connected():
            cursor = con.cursor()
            empno = input("Enter employee number: ")
            new_name = input("Enter new name: ")
            
            cursor.execute("UPDATE employee SET ename = %s WHERE empno = %s", 
                         (new_name, empno))
            con.commit()
            
            if cursor.rowcount > 0:
                print("Employee updated successfully")
            else:
                print("No employee found")
                
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()

if __name__ == "__main__":
    update_employee_name()
