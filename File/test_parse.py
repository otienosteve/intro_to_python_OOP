from unittest import TestCase


class TestParse(TestCase):

    def test_output(self):
        data=open("output.txt","r")
        datain=data.readlines()
        expected=open("expected.txt","r")
        expectedData=expected.readlines()
        self.assertEqual(datain,expectedData)