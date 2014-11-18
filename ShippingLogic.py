#!/usr/bin/python3

################################
# File Name:	ShippingLogic.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		The shipping calculator
################################

class ShippingLogic:
  
  def __init__(self):
    self._rate=[]
    self._rate.append( ( .1, 1, 5) )
    self._rate.append( ( 1.1, 5, 7) )
    self._rate.append( ( 5, None, 10) )
    self._FREE_SHIPPING_WEIGHT = 100
  
  def calcWeightForCost(self, basket):
    self._weight = 0
    
    for item in basket.items():
      if not item[1].getFreeShipping() :
        self._weight += (item[0] * int(item[1].getWeight()))
        
    return self._weight


  def calcCostForShippingByWeight(self, weight):
    
    self._cost = 0
    
    if weight <= self._FREE_SHIPPING_WEIGHT:
      for rate in self._rate :
        if weight >= rate[0] and (rate[1] is None or weight < rate[1]) :
          self._cost = rate[2]
          return self._cost

    return self._cost

class SaleShippingLogic(ShippingLogic):
  
  def __init__(self):
    self._rate=[]
    self._rate.append( ( .1, 1, 3) )
    self._rate.append( ( 1.1, 5, 4) )
    self._rate.append( ( 5, None, 6) )
    self._FREE_SHIPPING_WEIGHT = 50

