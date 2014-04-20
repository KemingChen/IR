# coding=utf-8
import warc

def main():
    targetId = 10090
    #filename = "data/ClueWeb09_English_Sample.warc"
    filename = "data/10.warc.gz"
    warcfile = warc.open(filename)
    docId = 0
    for doc in warcfile:
        if docId  == targetId:
            print unicode(doc.payload, errors="ignore")
        elif docId > targetId:
            break
        docId += 1

if __name__ == '__main__':
    main()