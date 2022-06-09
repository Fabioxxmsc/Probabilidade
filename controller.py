class Controller:
  def __init__(self, model, view):
    self.model = model
    self.view = view

  def Calcular(self, xi, xf, n, p, q):
    try:
      print(xi, xf, n, p, q)
    except Exception as ex:
      print(ex)