# coding=utf-8
import json

class InvertedIndex():
    def __init__(self):
        self.index = {}
        self.tDocs = {}
    def addDocument(self, docId, terms):
        if self.tDocs.get(docId) == None:
            self.tDocs[docId] = {}

        for idx, value in enumerate(terms):
            self.addTerm(docId, idx, value)
            self.tDocs[docId][idx] = value
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
        print "finishing"
        with open("index/_docs.jdb", 'w') as output:
            json.dump(self.tDocs, output)
    def commit(self, key):
        with open("index/" + key + ".jdb", 'w') as output:
            json.dump(self.index, output)
        self.index = {}

def main():
    index = InvertedIndex()
    for key in list(chr(i) for i in range(ord('a'), ord('z')+1)):
        with open("result/map_" + key + ".jdb", 'r') as content:
            jsonMap = json.loads(content.read())
            count = 0
            for docId in jsonMap:
                if count % 10000 == 0:
                    print "start index " + key + ": " + str(count)
                index.addDocument(docId, jsonMap[docId])
                count += 1
            index.commit(key)
    index.finish()
        

if __name__ == '__main__':
    main()