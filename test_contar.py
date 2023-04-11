import unittest
from contarpalabra import palabra

class TestDecimalToRoman (unittest.TestCase):
    def test_r1(self):
        resp= palabra("hola")
        self.assertEqual(
            resp, 
            {"hola":1
             })
    def test_hola2(self):
        resp= palabra("hola como estas hola")
        self.assertEqual (
            resp, 
            {
                "hola": 2, 
                "como": 1,
                "estas": 1,
        }
        )
    def test_hola3(self):
        resp= palabra("hola hola hola")
        self.assertEqual(
            resp, 
            {
            "hola": 3,
            })
    def test_habia(self):
        resp= palabra("habia una vez")
        self.assertEqual(
            resp, 
            {
                "habia": 1, 
                "una": 1,
                "vez": 1,
        } 
        )      
    def test_juliana(self):
        resp= palabra("la amiga de juliana esta en la casa")
        self.assertEqual(
            resp, 
            {
                "la": 2, 
                "amiga": 1,
                "de": 1,
                "juliana": 1,
                "esta": 1,
                "en": 1,
                "casa": 1,
        }
        )

    def test_irse(self):
        resp= palabra("hay que irse irse antes")
        self.assertEqual(
            resp,
            {
            "hay": 1,
            "que": 1,
            "irse": 2,
            "antes": 1,
            })
#lo responde en diccionarios, asi que los test estan en diccionarios
if __name__ == "__main__":
    unittest.main()