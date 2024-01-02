import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from pyresult import Err, ErrType

class TestErr(unittest.TestCase):
    def test_err_with_exception(self):
        # Arrange 
        ERR_DESCRIPTION: str = "test exception"
        
        #Act
        try:
            raise ValueError(ERR_DESCRIPTION)
        except ValueError as e:
            err = Err.catch(exception=e)

        # Assert
        self.assertEqual(err.code, "ValueError")
        self.assertEqual(err.description, ERR_DESCRIPTION)
        self.assertEqual(err.type, ErrType.Unexpected)
    
    def test_err_with_failure(self):
        # Arrange 
        ERR_CODE: str = "Test.Failure"
        ERR_DESCRIPTION: str = "test failure"
        
        #Act
        err_general = Err.failure()
        err_custom = Err.failure(code=ERR_CODE, desc=ERR_DESCRIPTION)

        # Assert Custom Properties
        self.assertEqual(err_custom.code, ERR_CODE)
        self.assertEqual(err_custom.description, ERR_DESCRIPTION)
        self.assertEqual(err_custom.type, ErrType.Failure)

        # Assert General Properties
        self.assertEqual(err_general.code, "General.Failure")
        self.assertEqual(err_general.description, "A failure occured")
        self.assertEqual(err_general.type, ErrType.Failure)

    def test_err_factory(self):
        # Arrange 
        ERR_MAP = {
            "Unexpected": Err.unexpected,
            "Validation": Err.validation,
            "Conflict": Err.conflict,
            "NotFound": Err.not_found,
            "Unauthorized": Err.unauthorized,
        }

        ERR_CODE_MAP: dict = {
            "Unexpected": ["General.Unexpected", "Error.Unexpected"],
            "Validation": ["General.Validation", "Error.Validation"],
            "Conflict": ["General.Conflict", "Error.Conflict"],
            "NotFound": ["General.NotFound", "Error.NotFound"],
            "Unauthorized": ["General.UnAuthorized", "Error.UnAuthorized"],
        }

        ERR_DESCRIPTION_MAP: dict = {
            "Unexpected": ["An unexpected err has occured", "Custom unexpected err description"],
            "Validation": ["A validation err has occured", "Custom validation err description"],
            "Conflict": ["An conflict err has occured", "Custom conflict err description"],
            "NotFound": ["An not found err has occured", "Custom not found err description"],
            "Unauthorized": ["An unauthorized err has occured", "Custom unauthorized err description"],
        }
        
        # Act
        for err_type in ERR_MAP:
            for code in ERR_CODE_MAP[err_type]:
                for description in ERR_DESCRIPTION_MAP[err_type]:
                    err_general = ERR_MAP[err_type]()
                    err_custom = ERR_MAP[err_type](code=code, desc=description)

                    # Assert Custom Properties
                    self.assertEqual(err_custom.code, code)
                    self.assertEqual(err_custom.description, description)
                    self.assertEqual(err_custom.type, ErrType[err_type])

                    # Assert General Properties
                    self.assertEqual(err_general.code, ERR_CODE_MAP[err_type][0])
                    self.assertEqual(err_general.description, ERR_DESCRIPTION_MAP[err_type][0])
                    self.assertEqual(err_general.type, ErrType[err_type])