from abc import abstractmethod, ABC


class Conta:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        self.__balance = value


class CalculadorInvestimento:
    def __init__(self):
        self.__tax = 0.075

    def aplicar_taxa(self, val):
        return val + (val * self.__tax)


class AplicadorInvestimento:
    def __init__(self):
        pass

    def start(self):
        conta = Conta()
        conta.set_balance(int(input("Digite o valor inicial: ")))

        calculadora = CalculadorInvestimento()
        total_investimento = calculadora.aplicar_taxa(conta.get_balance())

        print("Total: ", total_investimento)


AI = AplicadorInvestimento()
AI.start()


class Tigre:
    def __init__(self):
        pass

    def rosnar(self):
        return "ghrrraaaauuuuu"


class Gato(Tigre):
    def __init_subclass__(cls, **kwargs):
        pass

    def rosnar(self):
        return "ghrrraaaauuuuu"

    def miar(self):
        return "Miaauuuu"

    def ronronar(self):
        return "trututuururtrrutrutru"


gato = Gato()
print(gato.miar())
print(gato.ronronar())
print(gato.rosnar())


class Veiculo:
    def __init__(self):
        pass

    @abstractmethod
    def ligar_motor(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def ligar_motor(self):
        return "Vruuuuummmmm"

    def acelerar(self):
        return "ruuuuuun-ruuuuuuuunnnnn"


class Trem(Veiculo):
    def ligar_motor(self):
        return "thcuuuunnnnnnnn"

    def acelerar(self):
        return "thcuuuunnnnnnnn"


class ILoginValidacao:
    def __init__(self):
        pass

    @abstractmethod
    def verificar_senha(self):
        pass


class ILoginAuthenticacao:
    def __init__(self):
        pass

    @abstractmethod
    def autenticar(self):
        pass


class Login(ILoginAuthenticacao, ILoginValidacao, ABC):
    def __init__(self):
        super().__init__()

    def autenticar(self):
        return "autenticado"

    def verificar_senha(self):
        return "verificado"


class ITax:
    def __init__(self):
        pass

    @abstractmethod
    def calcular(self, valor):
        pass


class ICC(ITax):
    def __init__(self):
        super().__init__()

    def calcular(self, valor):
        return valor * 0.05


class Program:
    def __init__(self):
        pass

    def calcular_imposto(self):
        tax = ICC()  # no python eh meio ruim pra isso
        return tax.calcular(10)


