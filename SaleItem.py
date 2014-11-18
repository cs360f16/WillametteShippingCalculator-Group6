#!/usr/bin/python3

################################
# File Name:	SaleItem.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		An individual item for sale
################################

class SaleItem:
	
	def __init__ (self, listDetails) :
		self._cost = listDetails[0]
		self._weight = listDetails[1]
		self._title = listDetails[2]
		self._freeShipping = False
		
		if len(listDetails) == 4 :
			self._freeShipping = True
			

	def getCost(self):
		return self._cost
		
	def getWeight(self):
		return self._weight
		
	def getTitle(self):
		return self._title

	def getFreeShipping(self):
		return self._freeShipping
		
	def getDetails(self):
		return self._title + ' $' +str(self._cost)
		
		
		
