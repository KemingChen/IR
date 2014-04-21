# coding=utf-8
import warc
import json
from whoosh.analysis import SimpleAnalyzer
import re
import os

class InvertedIndex():
    def __init__(self):
        self.index = {}
        self.tDocs = {}
    def addDocument(self, docId, terms):
        if self.tDocs.get(docId) == None:
            self.tDocs[docId] = {}

        for key in terms:
            term = key
            tf = terms[key]
            self.addTerm(docId, term, tf)
            self.tDocs[docId][term] = tf
    def addTerm(self, docId, term, tf):
        if self.index.get(term) == None:
            self.index[term] = self.newTerm()
        else:
            self.index[term]["df"] += 1

        if self.index[term]["docs"] != "":
            self.index[term]["docs"] += ","
        self.index[term]["docs"] += str(docId)
    def newTerm(self):
        return {"df": 1, "docs": ""}
    def finish(self):
        print "finishing...wait"
        with open("index/_docs.jdb", 'w') as output:
            json.dump(self.tDocs, output)
    def commit(self, key):
        with open("index/" + key + ".jdb", 'w') as output:
            json.dump(self.index, output)
        self.index = {}

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

class MapDocs():
    def __init__(self):
        self.keys = list(chr(i) for i in range(ord('a'), ord('z')+1))
        self.maps = {}
        for key in self.keys:
            self.maps[key] = {}
    def addDoc(self, docId, words):
        for key in self.keys:
            self.maps[key][docId] = {}
        for word in words:
            key = word[0]
            if key in self.keys:
                if word not in self.maps[key][docId]:
                    self.maps[key][docId][word] = 1
                else:
                    self.maps[key][docId][word] += 1
    def close(self, N):
        info = {"DocNum": N}
        with open("index/_info", 'w') as output:
            json.dump(info, output)
    def getMaps(self):
        return self.maps

def parser(filename):
    try:
        warcfile = warc.open(filename)
    except Exception, e:
        os.system("cls")
        print "Can't find the " + filename
        os.system("pause")
        raise e
    mapDocs = MapDocs()
    htmlExtract = HtmlExtract()
    ana = SimpleAnalyzer()
    docId = 0
    for doc in warcfile:
        if docId != 0:
            content = htmlExtract.re(unicode(doc.payload, errors="ignore"))
            words = [token.text for token in ana(content)]
            mapDocs.addDoc(docId, words)
        if docId % 100 == 0:
            print "map: " + str(docId)
        docId += 1
    mapDocs.close(docId)
    return mapDocs.getMaps()

def inverter(maps):
    index = InvertedIndex()
    for key in list(chr(i) for i in range(ord('a'), ord('z')+1)):
        jsonMap = maps[key]
        count = 0
        for docId in jsonMap:
            if count % 10000 == 0:
                print "start index " + key + ": " + str(count)
            index.addDocument(docId, jsonMap[docId])
            count += 1
        index.commit(key)
    index.finish()

def main():
    # filename = "data/ClueWeb09_English_Sample.warc"
    # filename = "data/10.warc.gz"
    while not os.path.isdir("index"):
        os.system("cls")
        print "Please Create `index` folder first!!!"
        os.system("pause")

    os.system("cls")
    print "Please put WARC file in the `data` folder first!!!"
    filename = raw_input("Enter the WARC file name: ")
    filename = "data/" + filename
    try:
        maps = parser(filename)
        inverter(maps)
    except Exception, e:
        main()


if __name__ == '__main__':
    main()