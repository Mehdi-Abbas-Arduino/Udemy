import unittest
import Mister

class Test (unittest.TestCase):
    def __init__(self):
        text = "Python"
        result = Mister.capital(self)
        self.assertEquals(result,"PYTHON")

if __name__ == "__main__":
    unittest.main()