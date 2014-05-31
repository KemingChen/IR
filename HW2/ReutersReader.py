from sgmllib import SGMLParser
import re
import os
import tarfile
import json

class ReutersParser(SGMLParser):
	"""Utility class to parse a SGML file and yield documents one at a time."""
	def __init__(self, verbose=0):
		self.docsTrain = {}
		self.docsTest = {}
		SGMLParser.__init__(self, verbose)
		self._reset()

	def _reset(self):
		self.in_body = 0
		self.in_topics = 0
		self.in_topic_d = 0
		self.newid = None
		self.body = ""
		self.topics = []
		self.topic_d = ""
		self.hasTopics = False
		self.LEWISSPLIT = ""

	def parse(self, fd):
		for chunk in fd:
			self.feed(unicode(chunk, errors="ignore"))
		self.close()

	def handle_data(self, data):
		if self.in_body:
			self.body += data
		elif self.in_topic_d:
			self.topic_d += data

	def start_reuters(self, attributes):
		for pair in attributes:
			if pair[0] == "topics":
				self.hasTopics = True if pair[1] == "YES" else False
			elif pair[0] == "lewissplit":
				self.LEWISSPLIT = pair[1]
			elif pair[0] == "newid":
				self.newid = pair[1]

	def end_reuters(self):
		# Save: id(int), content(string), topics(array)
		self.body = re.sub(r'\s+', r' ', self.body)
		# print [self.newid, self.hasTopics, len(self.topics), len(self.body)]
		if self.newid != None and self.hasTopics and len(self.topics) > 0 and len(self.body) > 0:
			doc = {
				'id': self.newid,
				'content': self.body,
				'topics': self.topics
			}
			if self.LEWISSPLIT == "TRAIN":
				self.docsTrain[self.newid] = doc;
			elif self.LEWISSPLIT == "TEST":
				self.docsTest[self.newid] = doc;
		self._reset()

	def start_body(self, attributes):
		self.in_body = 1

	def end_body(self):
		self.in_body = 0

	def start_topics(self, attributes):
		self.in_topics = 1

	def end_topics(self):
		self.in_topics = 0

	def start_d(self, attributes):
		self.in_topic_d = 1

	def end_d(self):
		self.in_topic_d = 0
		self.topics.append(self.topic_d)
		self.topic_d = ""

	def getTrainDocs(self):
		return self.docsTrain

	def getTestDocs(self):
		return self.docsTest

class ReutersReader():
	def __init__(self, verbose=0):
		self.root = "sgms"
		self.RParser = ReutersParser()

	def handle_tar(self, filename):
		# ex: "HW2/datas/reuters21578.tar.gz"
		tar = tarfile.open(filename)
		tar.extractall(self.root, members=self.sgm_files(tar))
		tar.close()
		return self.handle_sgms()

	def handle_sgms(self):
		docs = {}
		for root, _dirnames, filenames in os.walk(self.root):
			for filename in filenames:
				path = os.path.join(root, filename)
				name, ext = os.path.splitext(path)
				# print name, ext
				if ext == ".sgm":
					print path
					self.RParser.parse(open(path))
					print "TRAIN: ", len(self.RParser.getTrainDocs())
					print "TEST: ", len(self.RParser.getTestDocs())
					print ""
		docs["train"] = self.RParser.getTrainDocs()
		docs["test"] = self.RParser.getTestDocs()
		return docs

	def load(self):
		docs = {}
		with open(self.root + "/TRAIN.jdb", 'r') as content_file:
			docs["train"] = json.loads(content_file.read())
		with open(self.root + "/TEST.jdb", 'r') as content_file:
			docs["test"] = json.loads(content_file.read())
		return docs

	def save(self):
		with open(self.root + "/TRAIN.jdb", 'w') as output:
			json.dump(self.RParser.getTrainDocs(), output)
		with open(self.root + "/TEST.jdb", 'w') as output:
			json.dump(self.RParser.getTestDocs(), output)

	def sgm_files(self, members):
		for tarinfo in members:
			if os.path.splitext(tarinfo.name)[1] == ".sgm":
				yield tarinfo

RReader = ReutersReader()

docs = RReader.handle_tar("datas/reuters21578.tar.gz")

# docs = RReader.load()
print len(docs["train"]), len(docs["test"])