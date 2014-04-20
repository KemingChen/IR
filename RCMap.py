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
class HtmlExtract():
    def __init__(self):
        self.patterns = {}
        self.patterns[0] = re.compile(r'[\n\r]*')
        self.patterns[1] = re.compile(r'HTTP/1.1[^<]*')
        self.patterns[2] = re.compile(r'(?i)<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>')
        self.patterns[3] = re.compile(r'(?i)<head\b[^<]*(?:(?!<\/head>)<[^<]*)*<\/head>')
        self.patterns[4] = re.compile(r'(?i)<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>')
        self.patterns[5] = re.compile(r'<.*?>')
    def re(self, content):
        string = content
        string = self.patterns[0].sub('', string)
        string = self.patterns[1].sub('', string)
        string = self.patterns[2].sub('', string)
        string = self.patterns[3].sub('', string)
        string = self.patterns[4].sub('', string)
        string = self.patterns[5].sub(', ', string)
        return string

def saveDocTf(docId, words):
    temp = {}
    for word in words:
        if temp.get(word) == None:
            temp[word] = words.count(word)
    with open("docs/" + str(docId) + ".jdb", 'w') as output:
        json.dump(temp, output)

def parser(filename):
    warcfile = warc.open(filename)
    mapDocs = MapDocs()
    htmlExtract = HtmlExtract()
    docId = 0
    for doc in warcfile:
        try:
            content = htmlExtract.re(unicode(doc.payload, errors="ignore"))
            docText = tb(content)
            words = docText.words
            saveDocTf(docId, words)
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