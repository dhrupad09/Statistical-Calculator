import unittest

from src.Calculator.Calculator import calculator
from Csvreader.Csvreader import csvreader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_addition(self):
        test_data = csvreader('Tests/csvfiles/TestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.Addition(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)


    def test_subtraction(self):
        test_data = csvreader('Tests/csvfiles/TestSubtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.Subtraction(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result,result)

    def test_times(self):
        test_data = csvreader('Tests/csvfiles/TestMultiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.Multiplication(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_div(self):
        test_data = csvreader('Tests/csvfiles/TestDivision.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.Division(row['Value 1'], row['Value 2']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_square(self):
        test_data = csvreader('Tests/csvfiles/TestSquare.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.Square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt(self):
        test_data = csvreader('Tests/csvfiles/TestSquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.Sqrt(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
