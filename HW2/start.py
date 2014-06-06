from Tkinter import *
from tkFileDialog import *
from ReutersReader import *
from threading import Thread

class myButton(Button):
	def __init__(self, root):
		Button.__init__(self, root)

	def setThread(self, thread):
		self.thread = thread

	def start(self):
		if self.thread != None:
			self.thread.start()

	def close(self):
		if self.thread != None:
			self.thread.close()

class IRHw2GUI(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.filename = ""
		self.pack(side=LEFT)
		self.grid()
		self.createWidgets()

	def createButton(self, text, row, col, disable, event=None, asy=False):
		btn = myButton(self)
		btn["text"] = text
		btn["width"] = 15
		btn["padx"] = 5
		btn["pady"] = 5
		btn.setThread(Thread(target=event) if asy else None)
		if asy:
			btn["command"] = btn.start
		else:
			btn["command"] = event
		btn.grid(row=row, column=col)
		self.setButtonDisable(btn, disable)
		return btn

	def setButtonDisable(self, btn, disable):
		btn["state"] = "normal" if not disable else "disable"

	def newReadButton(self, disable=True):
		self.readBtn = self.createButton("Parse", 0, 1, disable, self.parseFile, asy=True)

	def newTrainButton(self, disable=True):
		self.trainBtn = self.createButton("Train", 0, 2, disable)

	def newTestButton(self, disable=True):
		self.testBtn = self.createButton("Test", 0, 3, disable)

	def newResultButton(self, disable=True):
		self.testBtn = self.createButton("Result", 0, 4, disable)

	def createWidgets(self):
		self.selectBtn = self.createButton("Select", 0, 0, False, self.selectFile)
		self.newReadButton()
		self.newTrainButton()
		self.newTestButton()
		self.newResultButton()

		self.message = Text(self, relief=RIDGE)
		self.message.grid(row=1, column=0, columnspan=6)

	def printMessage(self, message, end="\n"):
		print message
		self.message.insert(INSERT, message + end)

	def selectFile(self):
		filename = askopenfilename()
		if filename != "":
			self.filename = filename
			self.printMessage("Select: " + self.filename)
			self.newReadButton(False)
		else:
			self.printMessage("No Selected File...")
			self.setButtonDisable(self.readBtn, True)

	def parseFile(self):
		self.setButtonDisable(self.selectBtn, True)
		self.setButtonDisable(self.readBtn, True)
		RReader = ReutersReader(printMessage=self.printMessage)
		docs = RReader.handle_tar(self.filename, True)
		self.printMessage("Train Docs: " + str(len(docs["train"])) + "\n" + 
			"Test Docs: " + str(len(docs["test"])))
		self.setButtonDisable(self.selectBtn, False)
		
		self.docs = docs
 
if __name__ == '__main__':
	root = Tk()
	app = IRHw2GUI(master=root)
	Thread(target=app.mainloop).start()