# coding=utf-8
import json
import os
from math import log, sqrt

class InvertedIndex():
	def __init__(self):
		self.index = {}
		self.load()
		with open("index/_info", 'r') as content_file:
			self.info = json.loads(content_file.read())
	def load(self):
		print "Loading..."
		for key in list(chr(i) for i in range(ord('a'), ord('z')+1)):
			with open("index/"+ key + ".jdb", 'r') as content:
				index = content.read()
				self.index[key] = index
	def doScore(self, keywords):
		keywords = keywords.strip().lower().split(" ")
		terms = {}
		for keyword in keywords:
			if terms.get(keyword) == None:
				postingList = self.findTerm(keyword)
				if postingList != {}:
					terms[keyword] = {"count": 1}
					terms[keyword]["info"] = postingList
			else:
				terms[keyword]["count"] += 1

		dicScores = {} # dependency docId
		dicWtd2 = {} # dependency docId
		Wtq2 = 0
		for key in terms:
			# print "key", key
			term = terms[key]
			idf = self.idf(float(term["info"]["df"]))
			Wtq = self.weight(float(term["count"]), idf)
			Wtq2 += Wtq * Wtq
			# print "idf", idf
			# print "Wtq", Wtq

			docs = term["info"]["docs"]
			for docId in docs:
				if dicScores.get(docId) == None:
					dicScores[docId] = float(0)
					dicWtd2[docId] = float(0)
				# print docId, docs[docId]["tf"]
				Wtd = self.weight(docs[docId]["tf"], idf)
				# print "Wtd", docId, ": " , Wtd
				# print "Wtq * Wtd: ", Wtq * Wtd
				dicWtd2[docId] += Wtd * Wtd
				dicScores[docId] += Wtq * Wtd

		for docId in dicScores:
			Wtd2 = dicWtd2[docId]
			Wtq2 = Wtq2
			Length = sqrt(Wtd2) * sqrt(Wtq2)
			dicScores[docId] = dicScores[docId] / Length
		print "Scores", dicScores
		#jIndex = json.loads(self.index[head])

		# if jIndex.get(keyword) != None:
		# 	print jIndex[keyword]["df"]
		# else:
		# 	print "None"
	def findTerm(self, term):
		head = term[0]
		jIndex = json.loads(self.index[head])
		if jIndex.get(term) != None:
			return jIndex[term]
		else:
			return {}
	def weight(self, tf, idf):
		return (1 + log(tf)) * idf
	def idf(self, df):
		DocNum = float(self.info["DocNum"])
		return log(DocNum / df)

def main():
    index = InvertedIndex()
    print "OK"
    keywords = "Hong Kong"
    index.doScore(keywords)
    return
    while 1:
    	try:
    		# os.system("cls")
    		# keyword = raw_input("Query: ")
    		print "Result: "
    		keywords = "a ffff"
    		index.doScore(keywords)
    		break
    		os.system("pause")
    	except Exception, e:
    		print e
    		break

if __name__ == '__main__':
    main()