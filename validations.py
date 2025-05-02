def validate_number(value, min_value, max_value):
    """Check if the value is a number within a specified range."""
    try:
        number = int(value)
        return min_value <= number <= max_value
    except ValueError:
        return False


def validate_float(value, min_value, max_value):
    """Check if the value is a float within a specified range."""
    try:
        number = float(value)
        return min_value <= number <= max_value
    except ValueError:
        return False


def validate_calories(value):
    """Calories should be between 0 and 2000."""
    return validate_number(value, 0, 2000)


def validate_height(value):
    """Calories should be between 0 and 2000."""
    return validate_number(value, 0, 2000)


def validate_meal_amount(value):
    """Calories should be between 0 and 2000."""
    return validate_number(value, 0, 2000)


def validate_age(value):
    """Age should be between 10 and 90."""
    return validate_number(value, 10, 90)


def validate_weight(value):
    """Weight should be between 30kg and 250kg."""
    return validate_float(value, 30.0, 250.0)


def validate_positive_float(value):
    """Ensure float input is positive."""
    return validate_float(value, 0.0, 2000.0)
    

def validate_day_number(value):
    """Validate day number input."""
    return validate_number(value, 0, 900)


def validate_gender(input):
    """Validate gender input, case-insensitive."""
    return input.lower() == "male" or input.lower() == "female"


def validate_non_empty_string(value):
    """Ensure string input is not empty or just whitespace."""
    return value.strip().lower()


def validate_daily_calories(value):
    """Validate that daily calories are between 500 and 4000."""
    return validate_number(value, 500, 4000)


def validate_positive_number(value):
    """Ensure number input is positive."""
    try:
        return float(value) > 0
    except ValueError:
        return False