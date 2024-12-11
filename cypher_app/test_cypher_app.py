import unittest
import cypher


class MyTestCase(unittest.TestCase):
    def test_that_cypher_app_works(self):
        self.assertEqual(cypher.encrypt("CODEDAMN", 3), "FRGHGDPQ")

    def test_that_cypher_decryption_app_works(self):
        self.assertEqual(cypher.decryption("FRGHGDPQ", 3), "CODEDAMN")
    # add assertion here

