"""
This is a sample script showing how you can utilize the Result package
"""
from pyresult import Result, ErrType, Err



"""""""""""""""""""""""""""""""""""""""""""""""""""
EXMPLE 1: simple example showcasing the Result type
"""""""""""""""""""""""""""""""""""""""""""""""""""
class User:
    def __init__(self, firstname:str, lastname: str, age: int):
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.age: int = age

def create_user(firstname: str, lastname: str, age: int) -> Result[User]:
    if firstname == "" or lastname == "":
        return Result(
            Err("Invalid.Name", "Firstname or lastname cannot be empty", ErrType.Validation))
    if age < 0:
        return Result(
            Err("Invalid.Age", "Age cannot be null or negative", ErrType.Validation))

    return Result(User(firstname, lastname, age))

def example_one():
    FIRSTNAME = "John" # Change to "" to see the return the err path
    LASTNAME = "Doe"
    AGE = 20

    result = create_user(FIRSTNAME, LASTNAME, AGE)
    result.match(
        on_success=lambda user: 
            print(f"EXAMPLE 1: success => {user.firstname} {user.lastname} ({user.age})"),
        on_err=lambda err: 
            print(f"EXAMPLE 1: error => {err.code} - {err.description}"))



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
EXAMPLE 2: another example showcasing the Result type for safe typing
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class User:
    def __init__(self, id: int, firstname:str, lastname: str, age: int):
        self.id: int = id
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.age: int = age
    
USERS = [
    User(1, "John", "Doe", 20),
    User(2, "Jane", "Doe", 22),
    User(3, "John", "Smith", 25),
]

def get_user_by_id(id: int) -> Result[User]:
    user = next((user for user in USERS if user.id == id), None)
    if user is None:
        return Result(Err("User.NotFound", "User not found", ErrType.NotFound))
    return Result(user)

def example_two():
    result = get_user_by_id(id)
    result.match(
        on_success=lambda user: 
            print(f"EXAMPLE 2: success => {user.firstname} {user.lastname} ({user.age})"),
        on_err=lambda err: 
            print(f"EXAMPLE 2: error => {err.code} - {err.description}"))



if __name__ == "__main__":
    example_one()
    example_two()