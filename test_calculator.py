import unittest
import calculator


class Test_calculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(5, 5), 10)
        self.assertEqual(calculator.add(-5, 5), 0)
        self.assertEqual(calculator.add(5, -5), 6)
        self.assertEqual(calculator.add(5, -5), 0)
        self.assertEqual(calculator.add(0.1, 0.1), 0.2)
    def test_sub(self):
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(-10, 5), -15)
        self.assertEqual(calculator.sub(10, -5), 15)
    def test_mul(self):
        self.assertEqual(calculator.mul(2, 2), 4)
        self.assertEqual(calculator.mul(-2, 2), -4)
        self.assertEqual(calculator.mul(2, -2), -4)
    def test_div(self):
        self.assertEqual(calculator.div(10, 5), 2)
        self.assertEqual(calculator.div(-10, 5), -2)
        self.assertEqual(calculator.div(10, -5), -2)

        with self.assertRaises(ValueError):
            calculator.div(10,0)
        with self.assertRaises(ValueError):
            calculator.div(0,0)
        

if __name__ == '__main__':
    unittest.main()