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
  
  def __init__(self):
    self._items = []
    
  def addItem(self, item):
    self._items.append(item)
    
  def items(self):
    for item in self._items:
      yield item

  def getTotalShipping(self, sLogic):
    weight = sLogic.calcWeightForCost(self)
    cost = sLogic.calcCostForShippingByWeight(weight)
    return cost
