# ********RoostGPT********
"""
Test generated by RoostGPT for test java-customannotation-test using AI Type  and AI Model 

ROOST_METHOD_HASH=calculator_9ebd2df6b3
ROOST_METHOD_SIG_HASH=calculator_ad84dc0779


### Scenario 1: Basic Addition
Details:
  TestName: test_calculator_basic_addition
  Description: Verify that the calculator correctly performs addition when the '+' operation is specified.
Execution:
  Arrange: Initialize two numbers for addition.
  Act: Call the calculator function with the '+' operation.
  Assert: Check if the result is the sum of the two numbers.
Validation:
  Rationalize the importance of verifying correct operation routing and calculation in the addition functionality, ensuring that the calculator adheres to basic arithmetic principles.

### Scenario 2: Basic Subtraction
Details:
  TestName: test_calculator_basic_subtraction
  Description: Verify that the calculator correctly performs subtraction when the '-' operation is specified.
Execution:
  Arrange: Initialize two numbers for subtraction.
  Act: Call the calculator function with the '-' operation.
  Assert: Check if the result is the difference between the first and the second number.
Validation:
  Rationalize the importance of ensuring the subtraction operation correctly computes differences, as it is fundamental for accurate arithmetic operations.

### Scenario 3: Basic Multiplication
Details:
  TestName: test_calculator_basic_multiplication
  Description: Verify that the calculator correctly performs multiplication when the '*' operation is specified.
Execution:
  Arrange: Initialize two numbers for multiplication.
  Act: Call the calculator function with the '*' operation.
  Assert: Check if the result is the product of the two numbers.
Validation:
  Rationalize the importance of validating multiplication, as it is essential for correct computation in various applications.

### Scenario 4: Basic Division
Details:
  TestName: test_calculator_basic_division
  Description: Verify that the calculator correctly performs division when the '/' operation is specified.
Execution:
  Arrange: Initialize two numbers for division where the second number is not zero.
  Act: Call the calculator function with the '/' operation.
  Assert: Check if the result is the quotient of the first number divided by the second.
Validation:
  Rationalize the importance of ensuring division is handled properly, especially handling non-zero divisors to prevent mathematical errors.

### Scenario 5: Division by Zero
Details:
  TestName: test_calculator_division_by_zero
  Description: Verify that the calculator handles division by zero appropriately.
Execution:
  Arrange: Initialize two numbers for division where the second number is zero.
  Act: Call the calculator function with the '/' operation.
  Assert: Check if the result is "Cannot divide by zero".
Validation:
  Rationalize the importance of correctly handling errors such as division by zero to prevent undefined operations in applications.

### Scenario 6: Invalid Operation
Details:
  TestName: test_calculator_invalid_operation
  Description: Verify that the calculator returns an appropriate message when an invalid operation is passed.
Execution:
  Arrange: Initialize two numbers and an invalid operation character.
  Act: Call the calculator function with the invalid operation.
  Assert: Check if the result is "Invalid operation".
Validation:
  Rationalize the importance of handling unexpected inputs gracefully, ensuring the calculator's robustness and reliability.

### Scenario 7: Floating Point Arithmetic
Details:
  TestName: test_calculator_floating_point_arithmetic
  Description: Verify that the calculator handles floating point numbers correctly across various operations.
Execution:
  Arrange: Initialize two floating point numbers and a valid operation.
  Act: Call the calculator function with each operation ('+', '-', '*', '/').
  Assert: Check if the results are correct for floating point arithmetic.
Validation:
  Rationalize the importance of accurate floating point operations, which are crucial in real-world applications and scientific computations.

These scenarios cover a comprehensive range of expected behaviors, edge cases, and error conditions while focusing on the business logic of the calculator function.
"""

# ********RoostGPT********
import unittest
from calc import calculator

class Test_CalcCalculator(unittest.TestCase):

    def test_calculator_basic_addition(self):
        # Arrange
        num1, num2 = 5, 3
        expected_result = 8
        # Act
        result = calculator(num1, num2, '+')
        # Assert
        self.assertEqual(result, expected_result, "Addition does not match expected result")

    def test_calculator_basic_subtraction(self):
        # Arrange
        num1, num2 = 10, 4
        expected_result = 6
        # Act
        result = calculator(num1, num2, '-')
        # Assert
        self.assertEqual(result, expected_result, "Subtraction does not match expected result")

    def test_calculator_basic_multiplication(self):
        # Arrange
        num1, num2 = 7, 6
        expected_result = 42
        # Act
        result = calculator(num1, num2, '*')
        # Assert
        self.assertEqual(result, expected_result, "Multiplication does not match expected result")

    def test_calculator_basic_division(self):
        # Arrange
        num1, num2 = 20, 5
        expected_result = 4
        # Act
        result = calculator(num1, num2, '/')
        # Assert
        self.assertEqual(result, expected_result, "Division does not match expected result")

    def test_calculator_division_by_zero(self):
        # Arrange
        num1, num2 = 15, 0
        expected_result = "Cannot divide by zero"
        # Act
        result = calculator(num1, num2, '/')
        # Assert
        self.assertEqual(result, expected_result, "Division by zero should return specific message")

    def test_calculator_invalid_operation(self):
        # Arrange
        num1, num2 = 10, 3
        expected_result = "Invalid operation"
        # Act
        result = calculator(num1, num2, '%')
        # Assert
        self.assertEqual(result, expected_result, "Invalid operation should return specific message")

    def test_calculator_floating_point_arithmetic(self):
        # Arrange
        num1, num2 = 5.5, 2.2
        expected_addition_result = 7.7
        expected_subtraction_result = 3.3
        expected_multiplication_result = 12.1
        expected_division_result = 2.5
        # Act and Assert
        self.assertAlmostEqual(calculator(num1, num2, '+'), expected_addition_result, places=2, msg="Floating point addition is incorrect")
        self.assertAlmostEqual(calculator(num1, num2, '-'), expected_subtraction_result, places=2, msg="Floating point subtraction is incorrect")
        self.assertAlmostEqual(calculator(num1, num2, '*'), expected_multiplication_result, places=2, msg="Floating point multiplication is incorrect")
        self.assertAlmostEqual(calculator(num1, num2, '/'), expected_division_result, places=2, msg="Floating point division is incorrect")

if __name__ == '__main__':
    unittest.main()
