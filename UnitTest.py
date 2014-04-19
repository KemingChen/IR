import json
index = """{"z7xtcn": {"df": 1, "docs": {"3454": {"tf": 1, "pos": [766]}}}, "zillions": {"df": 4, "docs": {"16836": {"tf": 1, "pos": [1117]}, "15545": {"tf": 1, "pos": [54]}, "935": {"tf": 1, "pos": [1249]}, "31332": {"tf": 1, "pos": [251]}}}, "zoes.place": {"df": 1, "docs": {"25460": {"tf": 1, "pos": [927]}}}, "zokko": {"df": 1, "docs": {"13449": {"tf": 1, "pos": [486]}}}, "zimony72.101freehost.com/free-mexican-lolita-incest-pics.html": {"df": 1, "docs": {"28162": {"tf": 2, "pos": [2920, 2928]}}}}"""
jIndex = json.loads(index)
for term in jIndex:
	print term
keyword = "z"
if jIndex.get(keyword) != None:
	print jIndex[keyword]["df"]
else:
	print "None"