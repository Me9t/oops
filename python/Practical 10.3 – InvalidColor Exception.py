class InvalidColor(Exception):
    """Raised when color is not in rainbow"""
    pass

def validate_color(color):
    rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    if color.lower() not in rainbow:
        raise InvalidColor("Color must be a rainbow color")
    return True

if __name__ == "__main__":
    try:
        color = input("Enter a rainbow color: ")
        validate_color(color)
        print("Valid color entered")
    except InvalidColor as e:
        print(f"Error: {e}")
