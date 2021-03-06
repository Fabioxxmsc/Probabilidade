from tkinter import Tk, PhotoImage
from view import View
from model import Model
from controller import Controller
import sys

class App(Tk):
  def __init__(self):
    super().__init__()

    self.title("Calculadora")

    if sys.platform.startswith("win"):
      self.iconbitmap(r"icone\menu.ico")
    else:
      logo = PhotoImage(file = r"./icone/menu.gif")
      self.call('wm', 'iconphoto', self._w, logo)
      
    self.resizable(False, False)

    self.largura = 800
    self.altura = 600
    self.largura_screen = self.winfo_screenwidth()
    self.altura_screen = self.winfo_screenheight()
    self.posicao_x = (self.largura_screen / 2) - (self.largura / 2)
    self.posicao_y = (self.altura_screen / 2) - (self.altura / 2)
    self.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posicao_x, self.posicao_y))

    model = Model()

    view = View(self)
    view.grid(row = 0, column = 0, padx = 10, pady = 10)

    controller = Controller(model, view)

    view.controller = controller

if __name__ == "__main__":
  app = App()
  app.mainloop()