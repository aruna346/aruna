import unittest
from minicalculator import addition, subtraction, multiplication, division

def read_test_cases(file_path):
  test_cases = []
  with open(file_path, "r") as file:
    for line in file:
      parts = line.strip().split(", ")
      operation = parts[0]
      x = float(parts[1])
      y = float(parts[2])
      expected_result = parts[3]
      test_cases.append((operation, x, y, expected_result))
  return test_cases

class TestCalculatorFunctions(unittest.TestCase):

  def test_operations_from_file(self):
    test_cases = read_test_cases("minical_history.txt")
    for operation, x, y, expected_result in test_cases:
      if operation == "addition":
        result = addition(x, y)
      elif operation == "subtraction":
        result = subtraction(x, y)
      elif operation == "multiplication":
        result = multiplication(x, y)
      elif operation == "division":
        result = division(x, y)

      if expected_result == "Cannot divide by zero":
        self.assertEqual(result, expected_result)

      else:
        self.assertEqual(result, float(expected_result))

if __name__ == 'main':
  unittest.main()
