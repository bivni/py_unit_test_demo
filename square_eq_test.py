import unittest

from square_eq import solve_sqe
      
class SimpleTest(unittest.TestCase):
      def test_D_negative(self):
                self.assertEqual(solve_sqe(4,5,4),())
                      
      def test_D_zero(self):
                self.assertEqual(solve_sqe(1,-2,1),(1.0,))
                      
      def test_D_positive(self):
                self.assertEqual(solve_sqe(1,-7,12),(3.0,4.0))
                      
if __name__ == '__main__':
     unittest.main()
