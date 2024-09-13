import unittest
from main import oldFunction
class TestOldFunction(unittest.TestCase):
 def test_output(self ):
  self.assertEqual(newFunction(), "This is the old function.")
 if __name__ == "__main__":
 unittest.main()
