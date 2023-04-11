from parameterized import parameterized, parameterized_class
import unittest
from contadorpalabra import contador_de_palabras
class Mytest(unittest.TestCase):
    @parameterized.expand([
        ("Soy de Argentina, soy", {"soy":2, "de":1, "argentina":1}),
        ("Hola, ¿cómo estás?", {"hola":1, "cómo":1, "estás":1}),
        ("Tres tristes tigres estan tristes", {"tres":1, "tristes":2, "tigres":1, "estan":1}),

    ])
    def test(self, frase, nropal):
        self.assertEqual(contador_de_palabras(frase),nropal)

if __name__ == '__main__':
    unittest.main()