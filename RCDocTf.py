import json

tDocs = {}
for key in list(chr(i) for i in range(ord('a'), ord('z')+1)):
	with open("index/"+ key + ".jdb", 'r') as content:
		print key
		terms = json.loads(content.read())
		for key in terms:
			term = terms[key]
			docs = term["docs"]
			for docId in docs:
				if tDocs.get(docId) == None:
					tDocs[docId] = {}
				tDocs[docId][key] = docs[docId]["tf"]

print "saving"
with open("docs/docs.jdb", 'w') as output:
	json.dump(tDocs, output)