from colorutils import Color
import replacement
from replacement import Replacer
import tkinter as tk

newReplacer = Replacer()

buttonColor = Color((110, 190, 250))

window = tk.Tk()

theButton = tk.Button(
	text = "click me",
	width = 100,
	height = 100,
	bg = buttonColor.web,
	command = newReplacer.runReplacer()
)

theButton.pack()
window.mainloop()
