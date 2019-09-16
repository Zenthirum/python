from roman import *
import unittest

class Test(unittest.TestCase):
    def test_9(self):
        self.assertEqual(romannumeral(9), "IX")
    def test_29(self):
        self.assertEqual(romannumeral(29),"XXIX")
    def test_707(self):
        self.assertEqual(romannumeral(707),"DCCVII")
    def test_1800(self):
        self.assertEqual(romannumeral(1800),"MDCCC")
        
if __name__ == '__main__':
    number_in = input("Enter a number: ")
    print (romannumeral(int(number_in)))
