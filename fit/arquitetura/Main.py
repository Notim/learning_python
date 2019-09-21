from abc import abstractmethod
from unittest import TestCase, main


class Main(object):

    @staticmethod
    def init(self):
        print(Calculadora.calcular(5, 7, "SUB"))


class Calculadora(object):

    @staticmethod
    def calcular(value1, value2, operador):
        factory = OperacaoFabrica()
        Operador = factory.criar(operador)

        return Operador.executa(value1, value2)


class OperacaoFabrica(object):
    def __init__(self):
        pass

    def criar(self, operador):
        if operador == "SUM":
            return Soma()
        if operador == "SUB":
            return Subtracao()
        if operador == "DIV":
            return Divisao()
        if operador == "MUL":
            return Multiplicacao()


class OperacaoAbstract(object):
    def __init__(self):
        pass

    @abstractmethod
    def executa(self, valor1, valor2):
        return


class Divisao(object):
    def __init__(self):
        pass

    def executa(self, valor1, valor2):
        return valor1 / valor2


class Soma(OperacaoAbstract):
    def __init__(self):
        super().__init__()

    def executa(self, valor1, valor2):
        return valor1 + valor2


class Subtracao(OperacaoAbstract):
    def __init__(self):
        super().__init__()

    def executa(self, valor1, valor2):
        return valor1 - valor2


class Multiplicacao(OperacaoAbstract):
    def __init__(self):
        super().__init__()

    def executa(self, valor1, valor2):
        return valor1 * valor2


class Testes(TestCase):
    def test_eh_SUB(self):
        self.assertEqual(Calculadora.calcular(5, 7, "SUB"), -2)

    def test_eh_SUM(self):
        self.assertEqual(Calculadora.calcular(5, 7, "SUM"), 12)

    def test_eh_DIV(self):
        self.assertEqual(Calculadora.calcular(5, 7, "DIV"), 0.7142857142857143)

    def test_eh_MUL(self):
        self.assertEqual(Calculadora.calcular(5, 7, "MUL"), 35)


if __name__ == '__main__':
    main()
