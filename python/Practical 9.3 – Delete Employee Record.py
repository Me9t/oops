import mysql.connector

def delete_employee():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rdnc",
            database="fycs"
        )
        
        if con.is_connected():
            cursor = con.cursor()
            empno = input("Enter employee number to delete: ")
            
            cursor.execute("DELETE FROM employee WHERE empno = %s", (empno,))
            con.commit()
            
            if cursor.rowcount > 0:
                print(f"Employee {empno} deleted")
            else:
                print("No employee found")
                
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if 'con' in locals() and con.is_connected():
            cursor.close()
            con.close()

if __name__ == "__main__":
    delete_employee()
