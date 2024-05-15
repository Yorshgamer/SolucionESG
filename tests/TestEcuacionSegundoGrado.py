import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado
class TestEcuacionSegundoGrado(unittest.TestCase):
    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()
    def TearDown(self):
        self.calculoRaices = None
    def test_calculoESG_dosNumeros_retornaSolución(self):
        #Arrange
        a = 3
        b = -5
        c = 1
        resultadoEsperadoRaiz1 = 1.43
        resultadoEsperadoRaiz2 = 0.23
        #Do
        resultadoActualRaiz1,resultadoActualRaiz2 = self.calculoRaices.calculoESG(a, b, c)
        #Assert
        self.assertAlmostEqualsEqual(resultadoEsperadoRaiz1,resultadoActualRaiz1,2)
        self.assertAlmostEqualsEqual(resultadoEsperadoRaiz2,resultadoActualRaiz2,2)

if __name__ == '__main__':
    unittest.main()
