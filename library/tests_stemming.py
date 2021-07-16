from django.test import TestCase, Client
from pprint import pprint
from library.algorithms.stemming.Stemmer.StemmerFactory import StemmerFactory
from library.algorithms.stemming.Dictionary.FileDatabase import FileDatabase
# Create your tests here.
# 
# 
class PrefixTestCase(TestCase):
	factory = StemmerFactory()
	kamusDatabase = FileDatabase()
	stemmer = factory.create_stemmer(False, kamusDatabase)
	print(stemmer.stem('abang'))
	
