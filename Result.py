# coding=utf-8
import json
import os

class InvertedIndex():
	def __init__(self):
		self.index = {}
		self.load()
	def load(self):
		print "Loading..."
		for key in list(chr(i) for i in range(ord('a'), ord('z')+1)):
			with open("index/"+ key + ".jdb", 'r') as content:
				index = content.read()
				self.index[key] = index
	def doScore(self, keyword):
		head = keyword[0]
		jIndex = json.loads(self.index[head])
		if jIndex.get(keyword) != None:
			print jIndex[keyword]["df"]
		else:
			print "None"

def main():
    index = InvertedIndex()
    print "OK"
    while 1:
    	try:
    		os.system("cls")
    		keyword = raw_input("Enter Keyword: ")
    		index.doScore(keyword)
    		os.system("pause")
    	except Exception, e:
    		print e
    		break

if __name__ == '__main__':
    main()