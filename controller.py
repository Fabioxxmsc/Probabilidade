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
      self.view.AddListBox(x, Decimal(dic[x][0]), Decimal(dic[x][1]))

  def Calcular(self, xi, xf, n, p, q):
    try:
      if self.model.DadosValidos(xi, xf, n, p, q):
        self.model.CalcularProbabilidade(int(xi), int(xf), int(n), Decimal(p), Decimal(q))
        self.PopularResultado(self.model.result)
      else:
        self.view.MsgAviso("Dados inválidos!")
    except Exception as ex:
      print(ex)

  def AtribuirComplemento(self, p, indexCK):
    if self.EhValorDecimal(p):
      ix = int(indexCK)
      
      valorP = self.CalcularPorcentagem(p, indexCK)
      valorQ = self.CalcularComplemento(valorP)

      if ix == 0:
        self.view.setValueComplemento(str(valorQ) + "%")
      else:
        self.view.setValueComplemento(valorQ)

  def CalcularPorcentagem(self, p, indexCK) -> Decimal:
    proba = Decimal(p)
    ix = int(indexCK)
    if ix == 0:      
      if proba <= 0:
        return 0
      else:
        return Decimal(proba / 100)
    else:
      return proba

  def CalcularComplemento(self, p) -> Decimal:
    return Decimal(1 - p)