from decimal import *

class Controller:
  def __init__(self, model, view):
    getcontext().prec = 4
    self.model = model
    self.view = view

  def EhValorInteiro(self, value) -> bool:
    return self.model.EhValorInteiro(value)
  
  def EhValorDecimal(self, value) -> bool:
    return self.model.EhValorDecimal(value)   

  def PopularResultado(self, dic):
    self.view.limparListBox()
    self.view.AddStrListBox("[x]  [Probabilidade]  [Acumulado]")
    for x in dic:
      try:
        proba = round(Decimal(dic[x][0]), 4)
      except:
        proba = Decimal(dic[x][0])

      try:
        acumu = round(Decimal(dic[x][1]), 4)
      except:
        acumu = Decimal(dic[x][1])

      self.view.AddListBox(x, proba, acumu)

  def Calcular(self, xi, xf, n, p, q, indexCK):
    try:
      if self.model.DadosValidos(xi, xf, n, p, q, indexCK):
        self.model.CalcularProbabilidade(int(xi), int(xf), int(n), Decimal(p), Decimal(q), int(indexCK))
        self.PopularResultado(self.model.result)
      else:
        self.view.MsgAviso("Dados inválidos!")
    except Exception as ex:
      self.view.MsgErro("[" + str(ex) + "]")

  def AtribuirComplemento(self, p, indexCK):
    if self.EhValorDecimal(p):
      proba = Decimal(p)
      ix = int(indexCK)
      if ix == 0:
        if (proba >= 0) and (proba <= 100):
          valorQ = self.model.CalcularComplemento(proba, ix)
          self.view.setValueComplemento(valorQ)
        else:
          self.view.limparQ()
      else:
        if (proba >= 0) and (proba <= 1):
          valorQ = self.model.CalcularComplemento(proba, ix)
          self.view.setValueComplemento(valorQ)
        else:
          self.view.limparQ()