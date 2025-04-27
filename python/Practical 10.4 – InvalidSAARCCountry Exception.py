class InvalidSAARCCountry(Exception):
    """Raised when country is not in SAARC"""
    pass

def validate_country(country):
    saarc = ["afghanistan", "bangladesh", "bhutan", "india", 
             "maldives", "nepal", "pakistan", "sri lanka"]
    if country.lower() not in saarc:
        raise InvalidSAARCCountry("Country must be a SAARC member")
    return True

if __name__ == "__main__":
    try:
        country = input("Enter SAARC country: ")
        validate_country(country)
        print("Valid SAARC country")
    except InvalidSAARCCountry as e:
        print(f"Error: {e}")
