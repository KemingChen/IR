# coding=utf-8
import warc
import json
from HTMLParser import HTMLParser
from textblob import TextBlob as tb
from threading import Thread
from math import ceil
import time

class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.init()
        HTMLParser.__init__(self) 
    def handle_starttag(self,tag,attrs): 
        if tag not in self.handledtags: 
            self.data='' 
            self.processing=tag 
    def handle_data(self,data): 
        if self.processing: 
            self.data += data
    def handle_endtag(self,tag): 
        if tag==self.processing: 
            #print str(tag) + ": " + str(self.data)
            self.data=self.data.replace("/", " ")
            self.datas.append(self.data);
            self.processing=None 
    def getDatas(self):
        return (', '.join(self.datas))
    def init(self):
        self.taglevels=[] 
        self.handledtags=['head', 'script', 'style']
        self.processing=None 
        self.datas = []

class MapDoc():
    def __init__(self):
        self.docs = {}
    def addTerm(self, docId, term, pos):
        if self.docs.get(docId) == None:
            self.docs[docId] = self.addDoc()
        self.docs[docId].append([term, pos])
    def addDoc(self):
        return []
    def getData(self):
        return self.docs

class InvertedIndex():
    def __init__(self):
        self.index = {}
    def addDocument(self, docId, terms):
        for term in terms:
            self.addTerm(docId, term)
    def addTerm(self, docId, term):
        termName = term[0]
        pos = term[1]
        if self.index.get(termName) == None:
            self.index[termName] = self.newTerm()
        if self.index[termName]["docs"].get(docId) == None:
            self.index[termName]["df"] += 1
            self.index[termName]["docs"][docId] = self.newDoc()
        self.index[termName]["docs"][docId]["tf"] += 1
        self.index[termName]["docs"][docId]["pos"].append(pos)
    def newTerm(self):
        return {"df": 0, "docs": {}}
    def newDoc(self):
        return {"tf": 0, "pos": []}
    def getIndex(self):
        return self.index

def inverter(mapDocs):
    index = {"af": InvertedIndex(), "gp": InvertedIndex(), "qz": InvertedIndex()}
    for key in mapDocs:
        mapDoc = mapDocs[key].getData()
        for docId in mapDoc:
            index[key].addDocument(docId, mapDoc[docId])
            if docId % 100 == 0:
                print "reduce: " + str(docId)
        with open("result/invertedIndex_" + key + ".jdb", 'w') as outfile:
            json.dump(index[key].getIndex(), outfile)

def parser(filename):
    warcfile = warc.open(filename)
    htmlParser = MyHTMLParser()
    mapDocs = {"af": MapDoc(), "gp": MapDoc(), "qz": MapDoc()}
    docId = 0
    for doc in warcfile:
        try:
            htmlParser.init()
            htmlParser.feed(unicode(doc.payload, errors="ignore"))
            words = tb(htmlParser.getDatas()).words
            for idx, value in enumerate(words):
                head = value[0]
                key = ""
                if head >= "a" and head <= "f":
                    key = "af"
                elif head >= "g" and head <= "p":
                    key = "gp"
                elif head >= "q" and head <= "z":
                    key = "qz"
                if key != "":
                    mapDocs[key].addTerm(docId, value, idx)
        except Exception, e:
            print e
        if docId % 100 == 0:
            print "map: " + str(docId)
        docId += 1

    for key in mapDocs:
        with open("result/map_" + key + ".jdb", 'w') as outfile:
            json.dump(mapDocs[key].getData(), outfile)
    return mapDocs

def main():
    #filename = "data/ClueWeb09_English_Sample.warc"
    filename = "data/10.warc.gz"
    mapDocs = parser(filename)
    #inverter(mapDocs)

if __name__ == '__main__':
    main()