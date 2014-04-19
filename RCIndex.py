# coding=utf-8
import json

class InvertedIndex():
    def __init__(self):
        self.index = {}
    def addDocument(self, docId, terms):
        for term in terms:
            self.addTerm(docId, term)
    def addTerm(self, docId, data):
        term = data[0]
        pos = data[1]
        if self.index.get(term) == None:
            self.index[term] = self.newTerm()
        if self.index[term]["docs"].get(docId) == None:
            self.index[term]["df"] += 1
            self.index[term]["docs"][docId] = self.newDoc()
        self.index[term]["docs"][docId]["tf"] += 1
        self.index[term]["docs"][docId]["pos"].append(pos)
    def newTerm(self):
        return {"df": 0, "docs": {}}
    def newDoc(self):
        return {"tf": 0, "pos": []}
    def getIndex(self):
        return self.index

def main():
    for key in list(chr(i) for i in range(ord('a'), ord('z')+1)):
        index = InvertedIndex()
        with open("result/map_" + key + ".jdb", 'r') as content:
            jsonMap = json.loads(content.read())
            count = 0
            for docId in jsonMap:
                if count % 100 == 0:
                    print "start index " + key + ": " + str(count)
                index.addDocument(docId, jsonMap[docId])
                count += 1
        with open("index/" + key + ".jdb", 'w') as output:
            json.dump(index.getIndex(), output)

if __name__ == '__main__':
    main()