"""
Author: Vahid Keshmiri
Email: V.Keshmiry@Gmail.com

This module demonstrates the use of Pydantic for data validation. It defines a Pydantic model for 
user input and includes a function to validate the input data.
"""

from pydantic import BaseModel, ValidationError

class UserInput(BaseModel):
    """
    A Pydantic model for validating user input data.
    """
    name: str
    age: int

def validate_user_input(data: dict):
    """
    Validates the user input data using the UserInput model.

    Parameters:
    data (dict): The user input data to validate.

    Returns:
    UserInput or str: The validated user input or an error message.
    """
    try:
        user_input = UserInput(**data)
        return user_input
    except ValidationError as e:
        return str(e)

# Example usage
if __name__ == "__main__":
    data = {"name": "Alice", "age": "25"}  # Intentionally incorrect type for age to show validation
    print(validate_user_input(data))
