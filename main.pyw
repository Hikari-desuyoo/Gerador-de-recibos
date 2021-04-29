from gui.GUI_recibo import GUI_recibo
from image_editor.gerador_de_recibo import Recibo
from monochrome.monochrome import monochrome
from printme.print import imprimir

#module for user UI with tkinter
gui=GUI_recibo()

#module for making the files
recibo_maker = Recibo()

#method for starting UI
gui.start_gui([recibo_maker.recibo,#'criar recibo'
               monochrome,#'ver recibo'
               imprimir])#'imprimir recibo'
