# coding=utf-8
import warc
import json
from HTMLParser import HTMLParser
from textblob import TextBlob as tb

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
        return (', '.join(self.datas)).lower()
    def init(self):
        self.taglevels=[] 
        self.handledtags=['head', 'script']
        self.processing=None 
        self.datas = []


class InvertedIndex():
    def __init__(self):
        self.index = {}
    def addDocument(self,docId,data):
        words = tb(data).words
        for idx, value in enumerate(words):
            term = value
            self.addTerm(docId,term,idx)
    def addTerm(self,docId,term,pos):
        if self.index.get(term) == None:
            self.index[term] = self.newTerm()
        if self.index[term]["docs"].get(docId) == None:
            self.index[term]["df"] += 1
            self.index[term]["docs"][docId] = self.newDoc()
        self.index[term]["docs"][docId]["tf"] += 1
        self.index[term]["docs"][docId]["pos"].append(pos)

        #print term, pos
    def newTerm(self):
        return {"df": 0, "docs": {}}
    def newDoc(self):
        return {"tf": 0, "pos": []}
    def getIndex(self):
        return self.index
    def printIndex(self):
        print self.index

index = InvertedIndex()
f = warc.open("data/10.warc.gz")
#f = warc.open("data/ClueWeb09_English_Sample.warc")
docId = 0
for doc in f:
    parser = MyHTMLParser()
    try:
        parser.feed(unicode(doc.payload, errors="ignore"))
        index.addDocument(docId,parser.getDatas())
    except Exception, e:
        print e
    print "doc: " + str(docId)
    docId += 1
#index.printIndex()
with open('invertedIndex.jdb', 'w') as outfile:
  json.dump(index.getIndex(), outfile)