#!/usr/bin/python3

################################
# File Name:	basket.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Provide a shopping basket for an online store
################################

class Basket:
	""" The customer's shopping basket
	"""
	
	def __init__(self):
		self._items = []
		
	def addItem(self, item):
		if self.contains(item[1].getID()):
			self.merge(item[1].getID(), item[0])
		else:
			self._items.append(item)
		
	def items(self):
		for item in self._items:
			yield item

	def getTotalShipping(self, sLogic):
		weight = sLogic.calcWeightForCost(self)
		cost = sLogic.calcCostForShippingByWeight(weight)
		return cost
		
		
	def contains(self, itemID):
		found = False
		for item in self._items:
			if item[1].getID() == itemID:
				found = True
					
		return found
		
	def merge(self, itemID, qty):
		found = False
		for item in self._items:
			if item[1].getID() == itemID:
				item[0] += qty
				found = True
					
		return found
