from unittest import TestCase, main
from juros_simples import JurosSimples

class JurosSimplesTest(TestCase):
    js = JurosSimples()
    m = 1400      # Montante.
    c = 1000      # Capital Inicial ou Principal.
    j = 0.1       # Taxa de juros de 10% ao mes
    t = 4         # Prazo de 4 meses

    def test_jurosPagosPorCadaPeriodo(self):
        # Resultado é: Capital inicial * taxa de juros
        self.assertEqual(self.js.jurosPagosPorCadaPeriodo(self.c, self.j), 100)

    def test_jurosTotaisPago(self):
        # Resultado é: Capital inicial * taxa de juros * prazo
        self.assertEqual(self.js.jurosTotaisPago(self.c, self.j, self.t), 400)
        
    def test_jurosTotaisPeloMontante(self):
        # Resultado é: Montante - capital inicial
        self.assertEqual(self.js.jurosTotaisPeloMontante(self.m, self.c), 400)

    def test_prazoParaChegarNoMontante(self):
        # Resultado é: Prazo = ((montante / capital inicial) - 1) / taxa de juros        
        self.assertEqual(self.js.prazoParaChegarNoMontante(self.m, self.c, self.j), 4)

if __name__ == "__main__":
    main()
