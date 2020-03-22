import unittest

from Csvreader.csvreader import csvreader
from Statistics.stats import statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, statistics)

    def test_median(self):
        test_data = csvreader('Tests/csvfiles/Array.csv').data
        test_result = csvreader('Tests/csvfiles/res.csv').data

        for column in test_result:
            result_test = float(column['Medain'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)

        self.statistics.median_(listx)
        self.assertEqual(round(self.statistics.result), round(result_test))

    def test_mode(self):
        test_data = csvreader('Tests/csvfiles/Array.csv').data
        test_result = csvreader('Tests/csvfiles/res.csv').data

        for column in test_result:
            result_test = float(column['Mode'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)

        self.statistics.mode_(listx)
        self.assertEqual(round(self.statistics.result), round(result_test))

    def test_mean(self):
        test_data = csvreader('Tests/csvfiles/Array.csv').data
        test_result = csvreader('Tests/csvfiles/res.csv').data

        for column in test_result:
            result_test = float(column['Mean'])


        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)


        self.statistics.mean_(listx)
        self.assertEqual(round(self.statistics.result), round(result_test))

    def test_stdev(self):
        test_data = csvreader('Tests/csvfiles/Array.csv').data
        test_result = csvreader('Tests/csvfiles/res.csv').data

        for column in test_result:
            result_test = float(column['Stdev'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)

        self.statistics.stdev_(listx)
        self.assertEqual(round(self.statistics.result), round(result_test))

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)

if __name__ == '__main__':
    unittest.main()
