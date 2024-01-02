import unittest
from unittest.mock import patch, Mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from pyresult import Result, Err


class User:
    """Test class for creating a user"""
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

def create_user(firstname: str, lastname: str, age: int) -> Result[User]:
    """Test method for creating a user or returning an Err

    Args:
        firstname (str): Firstname of the user
        lastname (str): Lastname of the user
        age (int): Age of the user

    Returns:
        Result[User]: Either returns a Result type with a User object or an Err
    """
    if firstname == "" or lastname == "":
        return Result(Err(code="MissingName",
                        desc="Firstname or lastname is missing"))
    if age < 18:
        return Result(Err(code="Underage",
                        desc="The user is underage"))
    
    return Result(User(firstname=firstname, lastname=lastname, age=age))


class TestResult(unittest.TestCase):
    def test_result_error_with_firstname(self):
        # Arrange
        FIRSTNAME = ""
        LASTNAME = "Doe"
        AGE = 20

        # Act
        result = create_user(firstname=FIRSTNAME, lastname=LASTNAME, age=AGE)

        # Assert
        self.assertEqual(result.value, None)
        self.assertEqual(result.is_error, True)
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(result.first_error.code, "MissingName")
        self.assertEqual(result.first_error.description, "Firstname or lastname is missing")

    def test_result_error_with_age(self):
        # Arrange
        FIRSTNAME = "John"
        LASTNAME = "Doe"
        AGE = 16

        # Act
        result = create_user(firstname=FIRSTNAME, lastname=LASTNAME, age=AGE)

        # Assert
        self.assertEqual(result.value, None)
        self.assertEqual(result.is_error, True)
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(result.first_error.code, "Underage")
        self.assertEqual(result.first_error.description, "The user is underage")

    def test_result_with_success(self):
        # Arrange
        FIRSTNAME = "John"
        LASTNAME = "Doe"
        AGE = 22

        # Act
        result = create_user(firstname=FIRSTNAME, lastname=LASTNAME, age=AGE)

        # Assert
        self.assertTrue(isinstance(result.value, User))
        self.assertEqual(result.is_error, False)
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(result.first_error, None)
        self.assertEqual(result.value.firstname, FIRSTNAME)
        self.assertEqual(result.value.lastname, LASTNAME)
        self.assertEqual(result.value.age, AGE)

    @patch('builtins.print')
    def test_match_on_success(self, mock_print):
        # Arrange
        result = Mock()
        result.match = Mock()
        user = Mock()
        user.firstname = 'John'
        user.lastname = 'Doe'
        result.match.side_effect = lambda on_success, on_err: on_success(user)

        # Act
        result = create_user(firstname='John', lastname='Doe', age=22)
        result.match(on_success=lambda user: print(f'successfully created user: {user.firstname} {user.lastname}'),
                    on_err=lambda err: print(f'failed to create user: {err.description}'))

        # Assert
        mock_print.assert_called_once_with('successfully created user: John Doe')

    @patch('builtins.print')
    def test_match_on_err(self, mock_print):
        # Arrange
        result = Mock()
        result.match = Mock()
        err = Mock()
        err.code = 'MissingName'
        err.description = 'Firstname or lastname is missing'
        result.match.side_effect = lambda on_success, on_err: on_err(err)

        # Act
        result = create_user(firstname='', lastname='', age=22)
        result.match(on_success=lambda user: print(f'successfully created user: {user.firstname} {user.lastname}'),
                    on_err=lambda err: print(f'error: {err.code} - {err.description}'))

        # Assert
        mock_print.assert_called_once_with('error: MissingName - Firstname or lastname is missing')