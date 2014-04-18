import re
import warc

# f = warc.open("data/ClueWeb09_English_Sample.warc")
f = warc.open("data/10.warc.gz")

docID = 0
for doc in f:
	print doc.payload
	print "--------------"
	docID += 1
		# print unicode(doc.payload, errors = "ignore")
	if docID == 6:
		exit();