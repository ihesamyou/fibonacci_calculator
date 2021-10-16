import unittest
import fibonacci_sequence


class TestFibonacci(unittest.TestCase):

    def test_index(self):
        self.assertRaises(TypeError, fibonacci_sequence.fibonacci_index, 'abc')
        self.assertRaises(TypeError, fibonacci_sequence.fibonacci_index, 10.2)
        self.assertRaises(TypeError, fibonacci_sequence.fibonacci_index, 0)
        self.assertRaises(TypeError, fibonacci_sequence.fibonacci_index, -10)
        self.assertEqual(fibonacci_sequence.fibonacci_index(2), """[0, 1]
For getting better results enter a whole number bigger than 2.""")
        self.assertEqual(fibonacci_sequence.fibonacci_index(9), [
                         0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_values_until(self):
        self.assertRaises(
            ValueError, fibonacci_sequence.fibonacci_until, 'abc')
        self.assertRaises(
            ValueError, fibonacci_sequence.fibonacci_until, -1)
        self.assertEqual(fibonacci_sequence.fibonacci_until(24), [
                         0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(fibonacci_sequence.fibonacci_until(24.5), [
                         0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(fibonacci_sequence.fibonacci_until(0), """[0, 1]
For getting better results enter a number bigger than 1.""")
        self.assertEqual(fibonacci_sequence.fibonacci_until(0.5), """[0, 1]
For getting better results enter a number bigger than 1.""")
        self.assertEqual(fibonacci_sequence.fibonacci_until(1), """[0, 1]
For getting better results enter a number bigger than 1.""")


if __name__ == '__main__':
    unittest.main()
