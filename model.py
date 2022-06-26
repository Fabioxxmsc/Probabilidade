from math import factorial
from decimal import *

class Model:
  def __init__(self):
    getcontext().prec = 4
    self.result = {}

  def CalcularCombinacao(self, n, x) -> Decimal:
    return Decimal(factorial(n) / (factorial(n - x) * factorial(x)))

  def EhValorInteiro(self, value) -> bool:
    try:
      val = int(value)
      return True if type(val) == int else False
    except:
      return False
  
  def EhValorDecimal(self, value) -> bool:
    try:
      val = Decimal(value)
      return True if type(val) == Decimal else False
    except:
      return False

  def xValido(self, xi, xf) -> bool:
    if self.EhValorInteiro(xi) and self.EhValorInteiro(xf):
      return (int(xi) >= 0) and (int(xf) >= 0) and (int(xi) <= int(xf))
    else:
      return False

  def nValido(self, n) -> bool:
    if self.EhValorInteiro(n):
      return int(n) >= 1
    else:
      return False

  def pqvalido(self, p, q) -> bool:
    if self.EhValorDecimal(p) and self.EhValorDecimal(q):
      return (Decimal(p) > 0) and (Decimal(p) + Decimal(q)) == 1
    else:
      return False

  def DadosValidos(self, xi, xf, n, p, q) -> bool:
    return self.xValido(xi, xf) and self.nValido(n) and self.pqvalido(p, q)

  def CalcularProbabilidade(self, xi, xf, n, p, q):
    acumulado = 0
    for x in range(xi, xf + 1):
      combinacao = self.CalcularCombinacao(n, x)
      proba = Decimal(combinacao * (p**x) * (q**(n - x)))
      self.result[x] = [proba, acumulado]
      acumulado += proba