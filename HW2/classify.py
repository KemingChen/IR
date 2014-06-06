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
sys.path.append('../../')

# Importing the irlib stuff
from irlib.classifier import NaiveBayes
from irlib.classifier import Rocchio  
from irlib.classifier import KNN  
from irlib.classifier import Evaluation 
from irlib.preprocessor import Preprocessor  
from irlib.configuration import Configuration  
import json

VERBOSE = True

def get_doc_id(fold=1, filename=""):
	doc_id = 'fold' + str(fold) + ':' + filename.split(".")[0]
	return doc_id


# Parse not any more than the first_n_files in folder
# @ml: Object for our classifier class (Rocchio, kNN, etc)
# @config: Our configuration class (class as in OOP not ML)
# @prep: Preprocessor class; tokenizers, stemmers, etc.
def parse_files(fold=1, mode = "training", first_n_files = 500, ml=object, config=object, prep=object):
	config_data = config.get_configuration()

	fd = open(fold, 'r')
	file_data = fd.read()
	objs = json.loads(file_data)
	counter = 0;
	length = len(objs)
	if length > first_n_files :
		length = first_n_files
	print "%s data length: %d" % (mode,length)
	for i in objs:
		if counter > first_n_files:
			break
		counter += 1
		if counter % 100 == 0:
			print counter
		doc_id = objs[i][unicode('id')]
		terms = prep.ngram_tokenizer(text=objs[i][unicode('content')])
		# terms = objs[i][unicode('content')]
		for class_name in objs[i][unicode('topics')]:
			if mode == 'training':
				ml.add_doc(doc_id = doc_id, doc_class=class_name, doc_terms=terms)
			else:
				# Class known from filename
				ml.add_query(query_id = doc_id, query_class=class_name, query_terms=terms)	
	fd.close()

# Let's do some workout now on all folders but one
def training(config, test_fold, ml, prep, first_n_files):
	parse_files(fold = test_fold, mode = 'training', first_n_files = first_n_files, ml=ml, config=config, prep=prep)

# Let's test on the remaining folder
def testing(config, test_fold, ml, ev, prep, first_n_files):
	parse_files(fold = test_fold, mode = 'testing', first_n_files = first_n_files, ml=ml, config=config, prep=prep)
	ml.compare_queries()

# Call this if anything goes wrong, for clean exit
def classifier_exit():
	if VERBOSE: 
		print sys.exc_info()
	print "\n[!] Houston, we have a problem [!]" 
	raise
	sys.exit()

class Classifier():
	def __init__(self):
		self.config = Configuration(config_file='classify.conf')
		try:
			self.config.load_configuration()
			self.config_data = self.config.get_configuration()
		except:
			print "Error loading configuration file."
			print "Classifier aborting."
			raise 	
		
		# config.display_configuration()
		print self.config

		#Preporcessor: tokenizer, stemmer, etc.
		prep_lower = self.config_data['lower']
		prep_stem = self.config_data['stem']
		prep_pos = self.config_data['pos']
		prep_ngram = self.config_data['ngram'] 
		self.prep = Preprocessor(pattern='\W+', lower=prep_lower, stem=prep_stem, pos=prep_pos, ngram=prep_ngram)

		self.ev = Evaluation()
		self.ml = Rocchio(verbose=VERBOSE, fold='n/a', config=self.config, ev=self.ev)
	def train(self,train_file="TRAIN.jdb", train_number=50):
		training(self.config, train_file, self.ml, self.prep, first_n_files=train_number)
		self.ml.do_padding()
		self.ml.calculate_training_data()
		# r.display_idx()
		self.ml.diagnose()
	def test(self, test_file="TEST.jdb", test_number=10):
		testing(self.config, test_file, self.ml, self.ev, self.prep, first_n_files=test_number)
		k = self.config_data['k']
		self.results = self.ev.calculate(review_spam=True, k=k)
	def result(self):
		return self.results
		
if __name__ == '__main__':

	# Profiling mode is not to be used in production,
	# only used for profiling the code's performance.
	profiling_mode = False
	if profiling_mode: 
		import cProfile
		import pstats
		cProfile.run('main()','classifier_prof')
		p_stats = pstats.Stats('classifier_prof')
		p_stats.sort_stats('time').print_stats(10)
	else:
		try:
			cl = Classifier()
			cl.train()
			cl.test(test_file="TEST.jdb", test_number=10)
			print cl.result()
		except:
			classifier_exit()