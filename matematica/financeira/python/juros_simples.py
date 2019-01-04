from decimal import Decimal

class JurosSimples(object):

    # Juros pagos em cada período(mês, ano, etc). 
    # O resultado é sempre o mesmo para cada par Capital e taxa de juros.
    def jurosPagosPorCadaPeriodo(self, c, j):
        return c * j

    # Juros total pago durante um período.
    # É a soma dos juros de cada período.
    def jurosTotaisPago(self, c, j, t):
        return c * j * t

    # Outra forma de achar os juros totais.
    # Quando sabemos o montante, podemos subtraí-lo pelo capital inicial.
    def jurosTotaisPeloMontante(self, m, c):
        return m - c

    # Para obtermos o prazo para se atingir determinado montante:
    # Prazo = ((montante / capital inicial) - 1) / taxa de juros
    def prazoParaChegarNoMontante(self, m, c, j):
        m = Decimal(str(m))
        c = Decimal(str(c))
        j = Decimal(str(j))
        return ((m / c) - 1) / j