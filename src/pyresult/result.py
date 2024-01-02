from typing import Generic, TypeVar, Callable
from .err import Err

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, value: T = None):
        self.value = None if isinstance(value, Err) else value
        self.is_error: bool = isinstance(value, Err)
        self.errors: list[Err] = [value] if self.is_error else []
        self.first_error: Err = self.errors[0] if self.is_error else None
    
    def match(self, on_success: Callable[[T], None], on_err: Callable[[Err], None]):
        """Method to match the result and execute the corresponding function

        Args:
            on_success (callable[[T], None]): The function to execute if the result is a success
            on_err (callable[[Err], None]): The function to execute if the result is an error
        """
        if self.is_error:
            on_err(self.first_error)
        else:
            on_success(self.value)