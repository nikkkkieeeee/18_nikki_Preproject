import unittest
import pratice as prog


class MyTestCase(unittest.TestCase):
    def test_totalset1(self):
        data = prog.set1['Calories']
        result = round(prog.TestMarks.totalset1(data), 1)
        self.assertEqual(result, 3637.2)

    def test_meanset1(self):
        data = prog.set1['Calories']
        result = round(prog.TestMarks.meanset1(data), 1)
        self.assertEqual(result, 330.7)

    def test_totalset2(self):
        data = prog.set2['Calories']
        result = round(prog.TestMarks.totalset2(data), 1)
        self.assertEqual(result, 2782.2)

    def test_meanset2(self):
        data = prog.set2['Calories']
        result = round(prog.TestMarks.meanset2(data), 1)
        self.assertEqual(result, 278.2)

    def test_totalset3(self):
        data = prog.set3['Calories']
        result = round(prog.TestMarks.totalset3(data), 1)
        self.assertEqual(result, 2939.2)

    def test_meanset3(self):
        data = prog.set3['Calories']
        result = round(prog.TestMarks.meanset3(data), 1)
        self.assertEqual(result, 293.9)




if __name__ == '__main__':
    unittest.main()
