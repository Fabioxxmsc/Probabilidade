from tkinter import DISABLED, Frame, Label, Entry, Button, END
from tkinter.ttk import Combobox

class View(Frame):
  def __init__(self, parent):
    super().__init__(parent)

    self.controller = None

    self.lblTitulo = Label(self, text = "Probabilidade Binomial", font = "Arial 20 bold")
    self.lblXi = Label(self, width = 5, text = "X inicial", font = "Arial 10")
    self.lblXf = Label(self, width = 5, text = "X final", font = "Arial 10")    
    self.lblN = Label(self, width = 5, text = "N", font = "Arial 10")
    self.lblP = Label(self, width = 5, text = "P", font = "Arial 10")
    self.lblQ = Label(self, width = 5, text = "Q", font = "Arial 10")

    self.etrXi = Entry(self)
    self.etrXf = Entry(self)
    self.etrN = Entry(self)
    self.etrP = Entry(self)
    self.etrP.bind("<KeyPress>", self.etrPChange)
    self.etrQ = Entry(self, state = DISABLED)

    self.comboPItens = ["Percentual %", "Decimal"]
    self.comboP = Combobox(self, values = self.comboPItens, state = "readonly")
    self.comboP.set("Percentual %")

    self.btnCalcular = Button(self, text = "Calcular", font = "Arial 10", command = self.btnCalcularOnClick)

    self.lblTitulo.grid(row = 0, column = 0, columnspan = 3)
    self.lblXi.grid(row = 1, column = 0, sticky = "w")
    self.lblXf.grid(row = 2, column = 0, sticky = "w")    
    self.lblN.grid(row = 3, column = 0, sticky = "w")
    self.lblP.grid(row = 4, column = 0, sticky = "w")
    self.lblQ.grid(row = 5, column = 0, sticky = "w")

    self.etrXi.grid(row = 1, column = 1, sticky = "w")
    self.etrXf.grid(row = 2, column = 1, sticky = "w")    
    self.etrN.grid(row = 3, column = 1, sticky = "w")
    self.etrP.grid(row = 4, column = 1, sticky = "w")
    self.etrQ.grid(row = 5, column = 1, sticky = "w")

    self.comboP.grid(row = 4, column = 2, sticky = "w")

    self.btnCalcular.grid(row = 6, column = 1, columnspan = 2)

  def btnCalcularOnClick(self):
    if self.controller is None:
      raise ValueError("Classe de controle não criada!")
    else:
      self.controller.Calcular(self.etrXi.get(), self.etrXf.get(), self.etrN.get(), self.etrP.get(), self.etrQ.get())

  def set_controller(self, controller):
    self.controller = controller

  def etrPChange(self, sender):
    valor = self.etrP.get().strip()

    if not valor is None:
      self.etrQ["state"] = "normal"
      self.etrQ.delete(0, END)
      self.etrQ.insert(0, str(valor))
      self.etrQ["state"] = "disabled"