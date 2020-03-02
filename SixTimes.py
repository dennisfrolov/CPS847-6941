import unittest

class TestMethods(unittest.TestCase):
  def cps6941(y):
    return (y*6);
  def test_add(self):
    self.assertEqual(cps6941(8), 48)
if __name__ == '__main__':
    unittest.main()
