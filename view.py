from tkinter import DISABLED, Frame, Label, Entry, Button, END, messagebox, Listbox
from tkinter.ttk import Combobox
from decimal import *
from controller import Controller
import sys

class View(Frame):
  def __init__(self, parent):
    super().__init__(parent)

    getcontext().prec = 4
    self._controller: Controller = None

    self.lblTitulo = Label(self, text = "Probabilidade Binomial", font = "Arial 20 bold")
    self.lblXi = Label(self, width = 5, text = "x inicial", font = "Arial 10")
    self.lblXf = Label(self, width = 5, text = "x final", font = "Arial 10")    
    self.lblN = Label(self, width = 5, text = "n", font = "Arial 10")
    self.lblP = Label(self, width = 5, text = "p", font = "Arial 10")
    self.lblQ = Label(self, width = 5, text = "q", font = "Arial 10")

    self.etrXi = Entry(self)
    self.etrXf = Entry(self)
    self.etrN = Entry(self)
    self.etrP = Entry(self)
    self.etrP.bind("<KeyRelease>", self.etrPKeyRelease)
    self.etrQ = Entry(self, state = DISABLED)

    self.comboPItens = ["Percentual %", "Decimal"]
    self.comboP = Combobox(self, values = self.comboPItens, state = "readonly")
    self.comboP.set("Percentual %")
    self.comboP.bind("<<ComboboxSelected>>", self.ComboboxSelected)

    self.btnCalcular = Button(self, text = "Calcular", font = "Arial 10", command = self.btnCalcularOnClick)

    self.listBox = Listbox(self, width = 70, xscrollcommand = True, yscrollcommand = True)

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

    self.listBox.grid(row = 1, column = 3, rowspan = 6)

  @property
  def controller(self) -> Controller:
    if self._controller is None:
      raise ValueError("Classe de controle não criada!")
    else:
      return self._controller

  @controller.setter
  def controller(self, controller: Controller):
    if controller is None:
      raise ValueError("Classe de controle não criada!")
    else:
      self._controller = controller
  
  def btnCalcularOnClick(self):
    self.controller.Calcular(self.etrXi.get(), self.etrXf.get(), self.etrN.get(), self.etrP.get(), self.etrQ.get(), self.comboP.current())

  def etrPKeyRelease(self, sender):
    win: bool = sys.platform.startswith("win")

    valor = sender.char.strip() if win else sender.keysym.strip()

    if valor != "":
      if self.controller.EhValorDecimal(valor):
        self.controller.AtribuirComplemento(Decimal(self.etrP.get()), self.comboP.current())

      elif win:
        if valor.find(".") == -1:
          self.etrQ["state"] = "normal"
          self.etrQ.delete(0, END)
          self.etrQ["state"] = "disabled"
          self.MsgErro("Valor '" + valor + "' não é numérico")
      else:
        if not (sender.keysym_num in [46, 65288, 65293]):
          self.etrQ["state"] = "normal"
          self.etrQ.delete(0, END)
          self.etrQ["state"] = "disabled"
          self.MsgErro("Valor '" + valor + "' não é numérico")

    else:
      self.limparQ()

  def setValueComplemento(self, value):
    self.etrQ["state"] = "normal"
    self.etrQ.delete(0, END)
    self.etrQ.insert(0, str(value))
    self.etrQ["state"] = "disabled"

  def limparQ(self):
    self.etrQ["state"] = "normal"
    self.etrQ.delete(0, END)
    self.etrQ["state"] = "disabled"

  def ComboboxSelected(self, event):
    self.controller.AtribuirComplemento(self.etrP.get(), self.comboP.current())

  def limparListBox(self):
    self.listBox.delete(0, END)

  def AddStrListBox(self, valor):
    self.listBox.insert(END, valor)

  def AddListBox(self, x, probabilidade, acumulado):
    self.listBox.insert(END, "[" + str(x) + "]  [       " + str(probabilidade) + "      ]  [      " + str(acumulado) + "    ]")

  def MsgErro(self, msg):
    messagebox.showerror(title="Erro", message=msg)

  def MsgAviso(self, msg):
    messagebox.showwarning(title="Aviso", message=msg)