import unittest
from contarpalabra import palabra

class TestDecimalToRoman (unittest.TestCase):
    def test_r1(self):
        resp= palabra("hola")
        self.assertEqual(resp, 1)
    def test_hola2(self):
        resp= palabra("hola chau")
        self.assertEqual(resp, 2)
    def test_hola3(self):
        resp= palabra("hola hola hola")
        self.assertEqual(resp, 1)
    def test_habia(self):
        resp= palabra("habia una vez")
        self.assertEqual(resp, 3)       
    def test_habia(self):
        resp= palabra("hola hola hola")
        self.assertEqual(resp, 1)
    def test_la(self):
        resp= palabra("la casa de la amiga es verde")
        self.assertEqual(resp, 6)
    def test_vacas(self):
        resp= palabra("hay que irse irse antes de ir de vacaciones")
        self.assertEqual(resp, 7)

if __name__ == "__main__":
    unittest.main()