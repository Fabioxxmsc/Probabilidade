from math import factorial
from decimal import *

class Model:
  def __init__(self):
    getcontext().prec = 4
    self.result = {}

  def CalcularCombinacao(self, n, x):
    return Decimal(factorial(n) / (factorial(n - x) * factorial(x)))

  def CalcularProbabilidade(self, xi, xf, n, p, q):
    acumulado = 0
    for x in range(xi, xf + 1):
      combinacao = self.CalcularCombinacao(n, x)
      proba = Decimal(combinacao * (p**x) * (q**(n - x)))
      self.result[x] = [proba, acumulado]
      acumulado += proba