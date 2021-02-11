from colorutils import Color
import replacement
from replacement import Replacer
import tkinter as tk

#newReplacer = Replacer()

#Using colorutils
buttonColor = Color((110, 190, 250))

#instantiation
window = tk.Tk()
window.geometry("400x400")

#strings lolw
theText = tk.StringVar()
replacedWord = tk.StringVar()
replacementWord = tk.StringVar()

#the main fucker
def Replace():
	#Get rid of any previous replacements
	theNewText.delete("0.0", tk.END)

	#converting tkinter shit into strings
	entireText = theWholeText.get()
	getReplacedWord = replacedWord.get()
	getReplacementWord = replacementWord.get()

	#replacement
	newString = entireText.replace(getReplacedWord, getReplacementWord)

	#giving you the jacked replacement
	theNewText.insert(tk.END, newString)

	#reset, ig
	replacedWord.set("")
	replacementWord.set("")

#el button
theButton = tk.Button(
	text = "click me",
	width = 50,
	height = 5,
	bg = buttonColor.web,
	command = Replace
)

#BUNCHA SHIT
theLabelOne = tk.Label(window, text="Word to be replaced")

theReplaced = tk.Entry(
	window,
	width=100,
	textvariable = replacedWord
)

theLabelTwo = tk.Label(window, text="Replacement word")

theReplacement = tk.Entry(
	window,
	width=100,
	textvariable = replacementWord
)

theLabelThree = tk.Label(window, text="The entire text")

theWholeText = tk.Entry(
	window,
	width = 100,
	textvariable = theText
)

theLabelFour = tk.Label(window, text="Your new text")

theNewText = tk.Text(
	height = 4
)

#OH GOD OH FUCK
theButton.pack()
theLabelOne.pack()
theReplaced.pack()
theLabelTwo.pack()
theReplacement.pack()
theLabelThree.pack()
theWholeText.pack()
theButton.pack()
theLabelFour.pack()
theNewText.pack()
window.mainloop()
