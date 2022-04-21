from unittest import TestCase
from  mod1 import findLength,square

class TestMod(TestCase):
    
    def test_len(self):
        self.assertEqual(findLength([1,2,3,4,5,6,7,8]),8)

    def test_square(self):
        self.assertEqual(square(2),4)
        
#tearDown()
#setUp()