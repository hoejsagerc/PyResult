from .err_type import ErrType

class Err:
    def __init__(self, code: str = None, 
                 desc: str = None, 
                 type: ErrType = None, 
                 ex: Exception = None):
        self.code = code
        self.exception = ex
        self.description = desc
        self.type = type


    def __repr__(self):
        """Provides a string representation of the Err object

        Returns:
            _type_: A string representation of the Err object
        """
        return f"Err(code={self.code}, description={self.description}, type={str(self.type)})"
    
    def catch(exception: Exception) -> 'Err':
        """Method for catching an exception and returning an Err object

        Args:
            exception (Exception): The exception to catch

        Returns:
            Err: An Err object
        """
        return Err(ex=exception, 
                   code=type(exception).__name__, 
                   desc=str(exception), 
                   type=ErrType.Unexpected)
    
    def failure(code: str = "General.Failure",
                 desc: str = "A failure occured") -> 'Err':
        """Method for creating a new Failure Err

        Args:
            code (str, optional): Provide an error code. Defaults to "General.Failure".
            description (str, optional): Provide an error description. Defaults to "A failure occured".

        Returns:
            Err: A new Failure Err object
        """
        return Err(code, desc, ErrType.Failure)

    def unexpected(code: str = "General.Unexpected",
                 desc: str = "An unexpected err has occured") -> 'Err':
        """Method for creating a new Unexpected Err

        Args:
            code (str, optional): Provide an error code. Defaults to "General.Unexpected".
            description (str, optional): Provide an error description. Defaults to "An unexpected err has occured".

        Returns:
            Err: A new Unexpected Err object
        """
        return Err(code, desc, ErrType.Unexpected)

    def validation(code: str = "General.Validation",
                 desc: str = "A validation err has occured") -> 'Err':
        """Method for creating a new Validation Err

        Args:
            code (str, optional): Provide an error code. Defaults to "General.Validation".
            description (str, optional): Provide an error description. Defaults to "A validation err has occured".

        Returns:
            Err: A new Validation Err object
        """
        return Err(code, desc, ErrType.Validation)

    def conflict(code: str = "General.Conflict",
                 desc: str = "An conflict err has occured") -> 'Err':
        """Method for creating a new Conflict Err

        Args:
            code (str, optional): Provide an error code. Defaults to "General.Conflict".
            description (str, optional): Provide an error description. Defaults to "An conflict err has occured".

        Returns:
            Err: A new Conflict Err object
        """
        return Err(code, desc, ErrType.Conflict)

    def not_found(code: str = "General.NotFound",
                 desc: str = "An not found err has occured") -> 'Err':
        """Method for creating a new NotFound Err

        Args:
            code (str, optional): Provide an error code. Defaults to "General.NotFound".
            description (str, optional): Provide an error description. Defaults to "An not found err has occured".

        Returns:
            Err: A new NotFound Err object
        """
        return Err(code, desc, ErrType.NotFound)

    def unauthorized(code: str = "General.UnAuthorized",
                 desc: str = "An unauthorized err has occured") -> 'Err':
        """Method for creating a new UnAuthorized Err

        Args:
            code (str, optional): Provide an error code. Defaults to "General.UnAuthorized".
            description (str, optional): Provide an error description. Defaults to "An unauthorized err has occured".

        Returns:
            Err: A new UnAuthorized Err object
        """
        return Err(code, desc, ErrType.Unauthorized)