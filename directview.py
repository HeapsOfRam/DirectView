#directview.py
#A GUI directory view
#Author: HeapsOfRam
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style

class directview(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent

		self.initUI()

	def initUI(self):
		self.parent.title("Windows")
		self.style = Style()
		self.style.theme_use("default")
		self.pack(fill = BOTH, expand = 1)

		self.columnconfigure(1, weight = 1)
		self.columnconfigure(3, pad = 7)
		self.rowconfigure(3, weight = 1)
		self.rowconfigure(5, pad = 7)

		lbl = Label(self, text = "Windows")
		lbl.grid(sticky = W, pady = 4, padx = 5)

		area = Text(self)
		area.grid(row = 1, column = 0, columnspan = 2, rowspan = 4,
			padx = 5, sticky = E + W + S + N)

		selectbtn = Button(self, text ="Select")
		selectbtn.grid(row = 1, column = 3, pady = 4)

		backbtn = Button(self, text ="<<")
		backbtn.grid(row = 2, column = 3)

		helpbtn = Button(self, text = "Help")
		helpbtn.grid(row = 5, column = 0, padx = 5)

		closebtn = Button(self, text = "Close")
		closebtn.grid(row = 5, column = 3)

def main():
	root = Tk()
	root.geometry("350x300+300+300")
	app = directview(root)
	root.mainloop()

if __name__ == "__main__":
	main()