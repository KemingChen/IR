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


class InvertedIndex():
    def __init__(self):
        self.index = {}
    def addDocument(self,docId,data):
        words = tb(data).words
        #print words
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

def parse(filename,ifrom, ito):
    warcfile = warc.open(filename)
    print "ifrom " + str(ifrom) + " " + str(ito) + ";"
    index = InvertedIndex()
    parser = MyHTMLParser()
    docId = 0
    for doc in warcfile:
        if docId >= ifrom and docId <= ito:
            try:
                parser.init()
                parser.feed(unicode(doc.payload, errors="ignore"))
                index.addDocument(docId,parser.getDatas())
            except Exception, e:
                print e
            if docId % 100 == 0:
                print "doc: " + str(docId)
        elif docId > ito:
            break
        docId += 1
    print "finish: " + str(ifrom) + "~" + str(ito)

def main():
    #filename = "data/ClueWeb09_English_Sample.warc"
    filename = "data/10.warc.gz"
    warcfile = warc.open(filename)
    fileCount = sum(1 for _ in warcfile)
    threadNum = 4
    oneSize = int(ceil(fileCount / float(threadNum)))
    threads = []

    # Create Thread
    for i in xrange(0, threadNum):
        t = Thread(target=parse, args=(filename, i * oneSize, (i + 1) * oneSize - 1,))
        t.start()
        threads.append(t) 

    for t in threads:
        t.join()

    # parse(filename, 0, 100)

 
if __name__ == '__main__':
    main()


#index.printIndex()
# with open('invertedIndex.jdb', 'w') as outfile:
#   json.dump(index.getIndex(), outfile)