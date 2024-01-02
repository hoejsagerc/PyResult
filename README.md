<div align=center>
  <h1 styyle="margin-bottom: 30px;">PyResult</br>Enhanced error handling for python</h1>
  
  ![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/hoejsagerc/pyresult/Deploy.yml) ![Codecov](https://img.shields.io/codecov/c/github/hoejsagerc/pyresult)
  
  ![GitHub License](https://img.shields.io/github/license/hoejsagerc/pyresult) ![GitHub contributors](https://img.shields.io/github/contributors/hoejsagerc/pyresult) ![GitHub top language](https://img.shields.io/github/languages/top/hoejsagerc/pyresult) ![GitHub Repo stars](https://img.shields.io/github/stars/hoejsagerc/pyresult)
</div>

</br>

## Table of content

- [Table of content](#table-of-content)
- [Overview](#overview)
- [Features](#features)
- [Use Cases](#use-cases)
- [Getting started](#getting-started)
- [How to use](#how-to-use)
  - [Simple Example](#simple-example)
  - [Creating Errors with the Err class](#creating-errors-with-the-err-class)
    - [Err Types](#err-types)
    - [Predefined Errors (docs not complete)](#predefined-errors-docs-not-complete)
    - [Custom Errors](#custom-errors)
    - [Handling Exceptions](#handling-exceptions)
  - [Using the Result type](#using-the-result-type)

## Overview

PyResult is a Python package designed to streamline error handling in your Python applications. 
Drawing inspiration from robust error handling libraries found in languages like C#, such as ErrorOr or FluentResult.
PyResult introduces a Result type that encapsulates either a successful outcome or an error, 
making your code more readable, maintainable, and less prone to unhandled exceptions.

</br>

## Features

- Strong Typing with Generics: Leverage Python's type hinting with Result objects, specifying what type of value they should contain on success.

- Elegant Error Handling: Replace traditional error-prone try-except blocks with a more structured approach, enhancing code readability and maintainability.

- Functional Style Pattern Matching: Utilize the match method to handle success and error cases cleanly and explicitly in a style akin to functional programming.

- Custom Error Types: Define and use custom error types with the Err class, allowing for detailed and specific error information, making debugging and error handling more straightforward.

- Intuitive Interface: A simple and intuitive API makes it easy to integrate PyResult into existing Python projects.

</br>

## Use Cases

PyResult is particularly useful in scenarios where error handling is crucial, such as:

- Web API development
- Data processing and validation
- File I/O operations
- Database interactions
- Any situation where exceptions need to be handled cleanly and predictably

</br>

## Getting started

You can install the library using:

```python
pip install pyresult
```

Then import the **Result** and **Err** class:

```python
from pyresult import Result, Err, ErrType
```

</br>

## How to use

### Simple Example

The library provides an easy way of writing type safe python methods and a match
condition for calling those methods and provide easy logic to the on_success or on_err
conditions.

here is a simple example of how you can use the lib to create a type safe and error handled method:

```python
class Password:
    def __init__(self, password: str):
        self.password = password

def create_password(password: str) -> Result[Password}:
    if len(password) < 8:
        return Err(code: "Password.Length", 
            desc: "Password must be equal to or longer than 8 characters")
    
    if not any(char in string.punctuation for char in password):
        return Err(code="Password.Symbol", 
            desc="Password must contain at least one symbol")

    return Result(Password(password: password))
```

The example aboce demonstrates the usage of the Result library in a password validation context. The Result library offers a structured approach to error handling, enhancing code readability and robustness.

**Class: _Password_**
* Represents a password.
* Contains a single attribute password, which is a string.

**Function: _create_password_**
* Signature: create_password(password: str) -> Result[Password]
* Purpose: Validates a given password string and returns a Result object.
* Validation Rules:
    1. Minimum Length: The password must be at least 8 characters long.
    2. Symbol Requirement: The password must contain at least one special character (symbol).

**Error Handling with _Result_ and _Err_**
* The function leverages the Result library for structured error handling.
* When a validation rule is violated, the function returns an Err object encapsulated in a Result.
* Each error is detailed with a specific error code and description.
    - Length Error: Returns Err with code "Password.Length" and a message indicating the password is too short.
    - Symbol Error: Returns Err with code "Password.Symbol" and a message indicating the absence of a required symbol.

This approach using the Result library allows for clear and concise handling of different error scenarios, making the function's behavior explicit and predictable. It also enhances the maintainability of the code by separating the logic of error handling from the main business logic.

</br>

### Creating Errors with the Err class

There are multiple ways you can create erros with the Result library.
This enhances you to be able to keep a structured way of handling errors in your code
an to keep an easy and maintainable way of handling errors.

#### Err Types

The library comes with a set of predefined error types which you can use or custimize as your own errors
with codes and descriptions matched to the type.

**Predefined Errors**
- Failure
- Unexpected
- Validation
- Conflict
- NotFound
- Unauthorized

The allows you to create a custom error and provide one of the above error types:

```python
from pyresult import Err, ErrType

Err(code: "Some.ErrorCode", desc: "Some description", type: ErrType.Validation)
```

If you don't provide an ErrType then it will default to: _None_

</br>

#### Predefined Errors (docs not complete)

You can also create predefined errors with the error types to be used within your system.
This way you can keep a well documented package for your application containing the errors.

```python

```

</br>

#### Custom Errors

You can create custom errors using by providing the error code, and description while writing your method:

```python
Err(code: "Custom.Error", desc: "This is a custom error", type: ErrType.Unexpected)
```

You can also create custom method using the builtin methods

The example below will create a new _no\_found_ error with the default code and description:
```python
Err.not_found()
```

you can also provide your own code and descriptions to these methods:
```python
Err.not_found(code: "Some.ErrorCode". desc: "Some description")
```
The example above will create an error with the type: ErrType.NotFound

</br>

#### Handling Exceptions

You can handle exceptions using the Err class aswell as creating your own errors.

if you use the builting method: _catch()_ you will be able to catch exceptions
and return them as result type errors. This will allow you to handle the exceptions just
like any other Err type.

The _catch()_ method will take an exception and then return an Err with a predefined
error code, description and the ErrType.Unexpected

here is an example of how i can be used:

```python
def some_method() -> Result[User]:
    try:
        raise ValueError("Some exception message")
    except ValueError as e:
        return Err.catch(ex: e)
```

The example above will return a Return type where the property _first\_error_ contains an Err object
with the code: ValueError, the description: "Some exception message" and the type: ErrType: ErrType.Unexpected

</br>

### Using the Result type


The Result class, part of a Python library designed for structured error handling, represents the outcome of an operation that can either succeed or fail. This class is generic, allowing it to handle various types of results.


**Key Features:**

* **Generic Type Support:** Utilizes Python's generics, allowing _Result_ objects to be of any type T.
* **Error Handling:** Differentiates between successful outcomes and errors, facilitating robust and clear error handling in your code.


**Attributes:**

* **value:** Holds the value of the operation if it's successful. It's _None_ if the operation resulted in an error.
* **is_error:** A boolean flag indicating whether the _Result_ object represents an error (True) or a success (False).
* **errors:** A list that contains the error(s) if _is\_error_ is _True_. It's empty for successful outcomes.
* **first_error:** The first error in the errors list if there are any errors, otherwise _None_.


**Methods:**

* **__init__(self, value: T = None):** Constructor for the Result class. Initializes a _Result_ object with a value or an error.
* **match(self, on_success: Callable[[T], None], on_err: Callable[[Err], None]):** A method that takes two callable arguments:
    - **on_success:** A function to be executed if the result is a success. It should accept a parameter of type _T_.
    - **on_err:** A function to be executed if the result is an error. It should accept a parameter of type _Err_.
    - The method executes _on\_success_ if _is\_error_ is False, passing the successful value. If _is\_error_ is _True_, it executes _on\_err_, passing the first error.


**Usage:**

The _Result_ class is particularly useful for operations where you want to handle success and failure cases distinctly and clearly.
By using _Result_, functions can return either a successful value or an error in a structured way, making the code more readable and maintainable.


**Example:**

```python
def process_data(data) -> Result[ProcessedData]:
    try:
        # Processing data...
        return Result(ProcessedData(data))
    except:
        return Result(Err(code="DataProcessing.Error",
            desc="Failed processing data", type=ErrType.Failure))

result = process_data(raw_data)
result.match(
    on_success=lambda processed_data: print("Processing succeeded"),
    on_err=lambda error: print(f"Processing failed: {error.code} - {error.description}")
)
```

**Function:** process_data(data) -> Result[ProcessedData]

* Accepts _data_ to be processed.
* Returns a _Result_ object which either contains _ProcessedData_ on successful processing or an Err object on failure.

**Success Path:**

* The data is processed successfully within a try block.
* A new _ProcessedData_ object is created with the processed data.
* The function returns a Result object encapsulating this _ProcessedData_ object.

**Error Handling:**

* If an exception occurs during data processing, the _except_ block is executed.
* It returns a _Result_ object containing an _Err_ instance with an error code (_"DataProcessing.Error"_), a description (_"Failed processing data"_), and an error type (_ErrType.Failure_).

**Result Handling:**

* The _result_ variable captures the outcome of _process\_data(raw\_data)_.
* The _match_ method of the _Result_ object is used to specify the handling for both successful and error outcomes.
* If successful, it prints "Processing succeeded".
* If an error occurred, it prints a message including the error code and description.

This example effectively showcases how the _Result_ type can be used to handle both success and error 
scenarios in a clean and structured way, making the code more robust and readable.
