import re
patterns = {}
patterns[0] = re.compile(r'[\n\r]*')
patterns[1] = re.compile(r'HTTP/1.1[^<]*')
patterns[2] = re.compile(r'(?i)<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>')
patterns[3] = re.compile(r'(?i)<head\b[^<]*(?:(?!<\/head>)<[^<]*)*<\/head>')
patterns[4] = re.compile(r'(?i)<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>')
patterns[5] = re.compile(r'<.*?>')
for x in patterns:
	print x