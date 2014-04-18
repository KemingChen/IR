# coding=utf-8
import warc
import json
from HTMLParser import HTMLParser
from textblob import TextBlob as tb
from threading import Thread
from math import ceil
import time
from sgmllib import SGMLParser
import re

class TextExtracter(SGMLParser):
    def __init__(self):
        self.init()
        SGMLParser.__init__(self)
    def handle_data(self, data):
        self.text.append(data)
    def getDatas(self):
        return ''.join(self.text)
    def init(self):
        self.text = []

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

class MapDocs():
    def __init__(self):
        self.keys = ["af", "gp", "qz"]
        self.outputs = {}
        for key in self.keys:
            self.outputs[key] = open("result/map_" + key + ".jdb", 'w')
            self.outputs[key].write("{")
    def addDoc(self, docId, words):
        TP = {} # term & pos
        for key in self.keys:
            TP[key] = []

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
                TP[key].append([value, idx])

        for key in self.keys:
            if docId > 0:
                self.outputs[key].write(",")
            self.outputs[key].write("\"" + str(docId) + "\":")
            json.dump(TP[key], self.outputs[key])
    def close(self):
        for key in self.keys:
            self.outputs[key].write("}")

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
    #htmlParser = MyHTMLParser()
    htmlParser = TextExtracter()
    mapDocs = MapDocs()
    docId = 0
    for doc in warcfile:
        # try:
        string = unicode(doc.payload, errors="ignore")
        string = re.compile(r'[\n\r]*').sub('', string)
        string = re.compile(r'HTTP/1.1[^<]*').sub('', string)
        string = re.compile(r'(?i)<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>').sub('', string)
        string = re.compile(r'(?i)<head\b[^<]*(?:(?!<\/head>)<[^<]*)*<\/head>').sub('', string)
        string = re.compile(r'(?i)<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>').sub('', string)
        string = re.compile(r'<.*?>').sub(',', string)
        #htmlParser.init()
        #content = re.compile(r'HTTP/1.1[^<]*').sub('', unicode(doc.payload, errors="ignore"))
        #htmlParser.feed(content)
        #words = tb(htmlParser.getDatas()).words
        words = tb(string).words
        mapDocs.addDoc(docId, words)
        # except Exception, e:
        #     print e
        # if docId % 100 == 2:
        #     break;
        if docId % 100 == 0:
            print "map: " + str(docId)
        docId += 1
    mapDocs.close()

def loader():
    for key in ["af", "gp", "qz"]:
        with open("result/map_" + key + ".jdb", 'r') as content:
            print json.loads(content.read())
        break

def main():
    #filename = "data/ClueWeb09_English_Sample.warc"
    filename = "data/10.warc.gz"
    parser(filename)
    #inverter(mapDocs)
    #loader()

if __name__ == '__main__':
    main()