class InvalidAge(Exception):
    """Raised when age is less than 1"""
    pass

def validate_age(age):
    if age < 1:
        raise InvalidAge("Age must be at least 1")
    return True

if __name__ == "__main__":
    try:
        age = int(input("Enter age: "))
        validate_age(age)
        print("Valid age entered")
    except InvalidAge as e:
        print(f"Error: {e}")
    except ValueError:
        print("Please enter a valid number")
