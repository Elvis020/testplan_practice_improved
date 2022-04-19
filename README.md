
# Testplan Practice Project

This project, will show you how testplan can be used to test a Python API.
To learn more about testplan, please checkout the documentation. 
https://testplan.readthedocs.io/en/latest/


# Project startup.
To start this project, activate your python environement and install project dependencies in your virtual environment using the following commands.
```bash
  $ python3 -m venv venv
  $ . venv/bin/activate
  $ pip install -r requirements.txt
```

Start the flask app, using the command below.
```bash
  $ Flask run
```

To test the project, create a new shell instance and use the commands below with testplan.
```bash
  $ python flask_test.py
```

**User Beware!!**
- [x] There are some intentional mistakes in the 'flask_test.py'. find them and fix them.

# Testing ...
A simple way to test the endpoints would be to visit the following endpoints via the browser or postman.

[![Addition](https://img.shields.io/badge/Route-Addition-white)](http://127.0.0.1:5000/add?a=100&b=45 )

[![Subtraction](https://img.shields.io/badge/Route-Subtract-white)](http://127.0.0.1:5000/subtract?a=100&b=45 )


[![Multiplication](https://img.shields.io/badge/Route-Multiply-white)](http://127.0.0.1:5000/multiply?a=100&b=45 )

[![Division](https://img.shields.io/badge/Route-Division-white)](http://127.0.0.1:5000/divide?a=100&b=45 )

# Challenges completed
Create endpoints for the current Flask project, that perform the following arithmetic operations.
- [x] [Modulo Operation](https://en.wikipedia.org/wiki/Modulo_operation)
- [x] [Math Exponent](https://www.tutorialspoint.com/python/number_exp.htm)
- [x] [Natural Log](https://en.wikipedia.org/wiki/Natural_logarithm)

In accordance to Test Driven Development(TDD), please create tests to verify the validity of the various operations, before creating the endpoints.
