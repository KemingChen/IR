from Tkinter import *
from tkFileDialog import *
from ReutersReader import *
 
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

	def addMessage(self, message, end="\n"):
		self.message.insert(INSERT, message + end)

	def selectFile(self):
		self.filename = askopenfilename()
		self.addMessage("Select: " + self.filename)

	def parseFile(self):
		if self.filename != "":
			RReader = ReutersReader()
			docs = RReader.handle_tar(self.filename)
			# docs = RReader.load()
			print len(docs["train"]), len(docs["test"])
		else:
			self.addMessage("No Selected File...")
 
if __name__ == '__main__':
	root = Tk()
	app = IRHw2GUI(master=root)
	app.mainloop()