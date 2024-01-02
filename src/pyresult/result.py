from typing import Generic, TypeVar, Callable
from .err import Err

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, value: T = None):
        self.value = None if isinstance(value, Err) else value
        self._is_error: bool = isinstance(value, Err)
        self._errors: list[Err] = [value] if self.is_error else []
        self._first_error: Err = self.errors[0] if self.is_error else None
    
    @property
    def is_error(self) -> bool:
        """Property to check if the result is an error

        Returns:
            bool: True if the result is an error, False otherwise
        """
        return self._is_error
    
    @property
    def errors(self) -> list[Err]:
        """Property to get the list of errors

        Returns:
            list[Err]: The list of errors
        """
        return self._errors
    
    @property
    def first_error(self) -> Err:
        """Property to get the first error

        Returns:
            Err: The first error
        """
        return self._first_error

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