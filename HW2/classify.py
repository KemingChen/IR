''' 
Review Spam Classifier 
======================
What it reallt does:
* Load configuration 
* Load preprocessor (preprocessor.py)
* Load classifier (irlib.py) specified by configuration 
* Train on all folds but one
* Test on remaining fold
* Permutate and do previous two steps on all folds
* Get results
'''

# Author: Tarek Amr <@gr33ndata> 

import os
import re
import sys

# Adding this to path to be able to import irlib
sys.path.append('irlab')

# Importing the irlib stuff
from irlib.classifier import NaiveBayes
from irlib.classifier import Rocchio  
from irlib.classifier import KNN  
from irlib.classifier import Evaluation 
from irlib.preprocessor import Preprocessor  
from irlib.configuration import Configuration  
import json
from whoosh.analysis import SimpleAnalyzer

VERBOSE = True

class Classify():
	def __init__(self, printMessage=None):
		self.prep = SimpleAnalyzer(expression=r"[A-Za-z]*", gaps=False)
		self.printMessage = printMessage

	def setConfig(self):
		self.config = Configuration(config_file='classify.conf')
		try:
			self.config.load_configuration()
			config_data = self.config.get_configuration()
		except:
			self.printMessage("Error loading configuration file.")
			self.printMessage("Classifier aborting.")
			raise 	
		
		# config.display_configuration()
		self.printMessage(self.config)

	# Parse not any more than the first_n_files in folder
	# @ml: Object for our classifier class (Rocchio, kNN, etc)
	# @config: Our configuration class (class as in OOP not ML)
	# @prep: Preprocessor class; tokenizers, stemmers, etc.
	def parse_files(self, fold=1, mode = "training", first_n_files = 500, ml=object, config=object, prep=object):
		config_data = config.get_configuration()

		fd = open(fold, 'r')
		file_data = fd.read()
		objs = json.loads(file_data)
		counter = 0;
		length = len(objs)
		if length > first_n_files :
			length = first_n_files
		self.printMessage("%s data length: %d" % (mode,length))
		for i in objs:
			if counter > first_n_files:
				break
			counter += 1
			if counter % 100 == 0:
				self.printMessage(counter)
			doc_id = objs[i][unicode('id')]
			# terms = prep.ngram_tokenizer(text=objs[i][unicode('content')])
			terms = [token.text for token in prep(objs[i][unicode('content')]) if token.text != "" ]
			# self.printMessage(terms)

			for class_name in objs[i][unicode('topics')]:
				if mode == 'training':
					ml.add_doc(doc_id = doc_id, doc_class=class_name, doc_terms=terms)
				else:
					# Class known from filename
					ml.add_query(query_id = doc_id, query_class=class_name, query_terms=terms)	
		fd.close()

	# Let's do some workout now on all folders but one
	def training(self):
		self.ev = Evaluation()
		self.ml = Rocchio(verbose=VERBOSE, fold='n/a', config=self.config, ev=self.ev)
		self.parse_files(fold="sgms/TRAIN.jdb", mode='training', first_n_files=200, ml=self.ml, config=self.config, prep=self.prep)
		self.ml.do_padding()
		self.ml.calculate_training_data()
		self.ml.diagnose()
		
	# Let's test on the remaining folder
	def testing(self):
		self.parse_files(fold="sgms/TEST.jdb", mode='testing', first_n_files=10, ml=self.ml, config=self.config, prep=self.prep)
		self.ml.compare_queries()

	def result(self):
		results = self.ev.calculate(review_spam=True, k=config.get_configuration()['k'])
		self.printMessage(results)
