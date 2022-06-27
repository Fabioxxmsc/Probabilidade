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

  def xValido(self, xi, xf, n) -> bool:
    if self.EhValorInteiro(xi) and self.EhValorInteiro(xf):
      xIni = int(xi)
      xFim = int(xf)
      return (xIni >= 0) and (xFim >= 0) and (xIni <= xFim) and (xFim <= int(n))
    else:
      return False

  def nValido(self, n) -> bool:
    if self.EhValorInteiro(n):
      return int(n) >= 1
    else:
      return False

  def pqvalido(self, p, q, indexCK) -> bool:
    if self.EhValorDecimal(p) and self.EhValorDecimal(q):
      val = 1
      if int(indexCK) == 0:
        val = 100  
      return (Decimal(p) > 0) and (Decimal(p) + Decimal(q)) == val
    else:
      return False

  def DadosValidos(self, xi, xf, n, p, q, indexCK) -> bool:
    return self.xValido(xi, xf, n) and self.nValido(n) and self.pqvalido(p, q, indexCK)

  def CalcularProbabilidade(self, xi, xf, n, p, q, indexCK):
    acumulado = 0
    self.result.clear()
    valorP = self.CalcularPorcentagem(p, indexCK)

    if int(indexCK) == 0:
      valorQ = Decimal(q / 100)
    else:
      valorQ = q

    for x in range(xi, xf + 1):
      combinacao = self.CalcularCombinacao(n, x)
      proba = Decimal(combinacao * (valorP**x) * (valorQ**(n - x)))
      acumulado += proba
      self.result[x] = [proba, acumulado]      

  def CalcularPorcentagem(self, p, indexCK) -> Decimal:
    proba = Decimal(p)
    if int(indexCK) == 0:
      proba = Decimal(proba / 100)
      if proba > 0 and proba < 1:
        return proba
      else:
        return -1
    else:
      if proba > 0 and proba < 100:
        return proba
      else:
        return -1

  def CalcularComplemento(self, p, indexCK) -> Decimal:
    val = 1
    proba = Decimal(p)
    if int(indexCK) == 0:
      val = 100
    return Decimal(val - proba)