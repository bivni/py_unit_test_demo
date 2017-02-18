import unittest

from add_demo import add
      
class SimpleTest(unittest.TestCase):
      def testadd1(self):
                self.assertEqual(add(4,5),9)
                      
if __name__ == '__main__':
     unittest.main()
