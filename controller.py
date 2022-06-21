class Controller:
  def __init__(self, model, view):
    self.model = model
    self.view = view

  def Calcular(self, xi, xf, n, p, q):
    try:
      print(str(self.model.CalcularProbabilidade(int(xi), int(xf), int(n), float(p), float(q))))
    except Exception as ex:
      print(ex)

  def CalcularComplemento(self, p):
    return float(1 - p)

  def CalcularPorcentagem(self, p, indexCK):
    if indexCK == 0:
      return float(p / 100)
    else:
      return p