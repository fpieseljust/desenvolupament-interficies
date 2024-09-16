class SaldoInsuficiente(Exception):
    pass

class Cartera(object):

    def __init__(self, saldo_inicial=0):
        if isinstance(saldo_inicial, int) > 0:
            self.saldo = saldo_inicial
        else:
            self.saldo = 0

    def gastar(self, cantidad):
        if self.saldo < cantidad:
            raise SaldoInsuficiente(
                'No tienes dinero suficiente. Saldo actual: {}'.format(cantidad))
        self.saldo -= cantidad

    def ingresar(self, cantidad):
        self.saldo += cantidad