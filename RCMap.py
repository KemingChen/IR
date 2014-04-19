# coding=utf-8
import warc
import json
from textblob import TextBlob as tb
import re

class MapDocs():
    def __init__(self):
        self.keys = list(chr(i) for i in range(ord('a'), ord('z')+1))
        self.outputs = {}
        for key in self.keys:
            self.outputs[key] = open("result/map_" + key + ".jdb", 'w')
            self.outputs[key].write("{")
    def addDoc(self, docId, words):
        TP = {} # term & pos
        for key in self.keys:
            TP[key] = []

        for idx, value in enumerate(words):
            key = value[0]
            if key >= "a" and key <= "z":
                TP[key].append([value, idx])

        for key in self.keys:
            if docId > 0:
                self.outputs[key].write(",")
            self.outputs[key].write("\"" + str(docId) + "\":")
            json.dump(TP[key], self.outputs[key])
    def close(self):
        for key in self.keys:
            self.outputs[key].write("}")

# Html Extract Body, except tags
def HtmlExtract(content):
    string = content
    string = re.compile(r'[\n\r]*').sub('', string)
    string = re.compile(r'HTTP/1.1[^<]*').sub('', string)
    string = re.compile(r'(?i)<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>').sub('', string)
    string = re.compile(r'(?i)<head\b[^<]*(?:(?!<\/head>)<[^<]*)*<\/head>').sub('', string)
    string = re.compile(r'(?i)<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>').sub('', string)
    string = re.compile(r'<.*?>').sub(', ', string)
    return string

def parser(filename):
    warcfile = warc.open(filename)
    mapDocs = MapDocs()
    docId = 0
    for doc in warcfile:
        try:
	    	content = HtmlExtract(unicode(doc.payload, errors="ignore"))
	        words = tb(content).words
	        mapDocs.addDoc(docId, words)
        except Exception, e:
            print e
        if docId % 100 == 0:
            print "map: " + str(docId)
        docId += 1
    mapDocs.close()

def main():
    #filename = "data/ClueWeb09_English_Sample.warc"
    filename = "data/10.warc.gz"
    parser(filename)

if __name__ == '__main__':
    main()