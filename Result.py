# coding=utf-8
import json
import os
from math import log, sqrt
import operator

class InvertedIndex():
	def __init__(self):
		self.index = {}
		self.docs = {}
		self.load()
		with open("index/_info", 'r') as content_file:
			self.info = json.loads(content_file.read())
	def load(self):
		print "Loading..."
		for key in list(chr(i) for i in range(ord('a'), ord('z')+1)):
			with open("index/"+ key + ".jdb", 'r') as content:
				index = content.read()
				self.index[key] = index
		with open("index/_docs.jdb", 'r') as content:
			self.docs = json.loads(content.read())
	def doScore(self, keywords):
		keywords = keywords.strip().lower().split(" ")
		querys = {}
		docList = []
		Wtqs = {}
		for keyword in keywords:
			if querys.get(keyword) == None:
				postingList = self.findTerm(keyword)
				if postingList != {}:
					querys[keyword] = {"tf": 1, "df": postingList["df"]}
					docList = list(set(docList) | set(postingList["docs"].keys()))
					# print len(postingList["docs"].keys())
			else:
				querys[keyword]["tf"] += 1
		if len(querys) == 0:
			print "Not Match Anything."
			return

		for key in querys:
			query = querys[key]
			Wtqs[key] = self.weight(query["tf"], query["df"], self.info["DocNum"])
		# Wtqs = self.normalize(Wtqs)
		# print Wtqs
		# print len(docList)

		Scores = {}
		for docId in docList:
			Scores[docId] = float(0)
			tf_wt = {}
			terms = self.docs[docId]
			for key in terms:
				tf_wt[key] = self.tf_weight(terms[key])
			tf_wt = self.normalize(tf_wt)
			# print tf_wt
			
			for key in querys:
				if key not in tf_wt:
					continue
				Scores[docId] += tf_wt[key] * Wtqs[key]
			# print Scores
			# break

		for k, v in sorted(Scores.iteritems(), key = operator.itemgetter(1), reverse = True)[0 : 10]:
			print "  " + str(k) + ": " + str(round(v, 3))
	def findTerm(self, term):
		head = term[0]
		jIndex = json.loads(self.index[head])
		if jIndex.get(term) != None:
			return jIndex[term]
		else:
			return {}
	def weight(self, tf, df, N):
		try:
			return (1 + log(tf)) * log(N / df)
		except Exception, e:
			return 0
	def tf_weight(self, tf):
		return (1 + log(tf))
	def normalize(self, vector):
		value = float(0)
		for i in vector:
			value += vector[i] * vector[i]
		L = sqrt(value)
		for i in vector:
			vector[i] = vector[i] / L
		return vector

def main():
    index = InvertedIndex()
    print "OK"
    while 1:
    	try:
			os.system("cls")
			keywords = raw_input("Query: ")
			# keywords = "google"
			print "Result: \n  <doc#>: <similarity score>"
			index.doScore(keywords)
			# break
			os.system("pause")
    	except Exception, e:
    		print e
    		break

if __name__ == '__main__':
    main()