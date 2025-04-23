import unittest

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial_str(self):
        with self.assertRaises(TypeError):
            factorial("5")

    def test_factorial_plusfloat(self):
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_factorial_minus(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_bool(self):
        self.assertEqual(factorial(True), 1)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_normal(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
