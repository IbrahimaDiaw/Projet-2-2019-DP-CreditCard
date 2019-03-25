# coding: utf8

import banque
from abc import ABCMeta, abstractmethod

class Verificteur(object):
	__metaclass__ = ABCMeta
	def __init__(self,numeros):
		self.numeros=numeros
	
	def Verifier_numero_carte(self,numeros):
		pass
   

