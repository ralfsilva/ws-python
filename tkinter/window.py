from tkinter import *

color ='#000024'

window = Tk()
window.title('Olá Mundo!')
window.geometry('600x450') # (width x height)
window.config(bg=color)

window.iconphoto(False, PhotoImage(file='python.png'))
window.resizable(width=False, height=False)

window.mainloop()