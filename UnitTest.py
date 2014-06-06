from Tkinter import *
from tkFileDialog import *
import HW2.ReutersReader.py
 
class IRHw2GUI(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.filename = ""
		self.pack(side=LEFT)
		self.grid()
		self.createWidgets()

	def createButton(self, text, row, col, event=None):
		btn = Button(self)
		btn["text"] = text
		btn["width"] = 15
		btn["padx"] = 5
		btn["pady"] = 5
		btn["command"] = event
		btn.grid(row=row, column=col)
		return btn

	def createWidgets(self):
		self.selectBtn = self.createButton("Select", 0, 0, self.selectFile)
		self.readBtn = self.createButton("Parse", 0, 1, self.parseFile)
		self.trainBtn = self.createButton("Train", 0, 2)
		self.testBtn = self.createButton("Test", 0, 3)
		self.testBtn = self.createButton("Result", 0, 4)
 
		self.message = Text(self, relief=RIDGE)
		self.message.grid(row=1, column=0, columnspan=6)

	def selectFile(self):
		self.filename = askopenfilename()
		self.message.insert(INSERT, "Select: " + self.filename)

	def parseFile(self):
		RReader = ReutersReader()
		docs = RReader.handle_tar("datas/reuters21578.tar.gz")
		# docs = RReader.load()
		print len(docs["train"]), len(docs["test"])
 
if __name__ == '__main__':
	root = Tk()
	app = IRHw2GUI(master=root)
	app.mainloop()