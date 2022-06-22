from decimal import *

class Controller:
  def __init__(self, model, view):
    getcontext().prec = 4
    self.model = model
    self.view = view

  def Calcular(self, xi, xf, n, p, q):
    try:      
      self.model.CalcularProbabilidade(int(xi), int(xf), int(n), Decimal(p), Decimal(q))
      dic = self.model.result

      self.view.limparListBox()
      self.view.AddStrListBox("[x]  [Probabilidade]  [Acumulado]")
      for x in dic:
        self.view.AddListBox(x, Decimal(dic[x][0]), Decimal(dic[x][1]))
    except Exception as ex:
      print(ex)

  def CalcularComplemento(self, p):
    return Decimal(1 - p)

  def CalcularPorcentagem(self, p, indexCK):
    if indexCK == 0:
      return Decimal(p / 100)
    else:
      return p

  def EhValorNumerico(self, value):
    try:
      val = Decimal(value)
      return True if type(val) == Decimal else False
    except:
      return False