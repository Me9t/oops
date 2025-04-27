class InvalidMarks(Exception):
    """Raised when marks are not between 0 and 100"""
    pass

def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarks("Marks must be between 0 and 100")
    return True

if __name__ == "__main__":
    try:
        marks = int(input("Enter marks (0-100): "))
        validate_marks(marks)
        print("Valid marks entered")
    except InvalidMarks as e:
        print(f"Error: {e}")
    except ValueError:
        print("Please enter a valid number")
