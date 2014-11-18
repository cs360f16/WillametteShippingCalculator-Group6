#!/usr/bin/python3

################################
# File Name:	main.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Simulate an online store
################################

from itemStore import ItemStore
from basket import Basket
from ShippingLogic import *


def displayItems(theStore):
  counter = 1
  
  for item in theStore.items():
    print(str(counter).rjust(3) + '.' + item.getTitle().ljust(25)+ '\t'+
    '\t' + "${:.2f}".format(int(item.getCost())).rjust(7) + 
     '\t'+item.getWeight().rjust(5), end='')
    if item.getFreeShipping() :
      print(' Free Shipping!')
    else:
      print('')
    counter += 1

def addItem(theStore, basket, choice, qty):
  
  basket.addItem( [qty, theStore.getItem(choice)])
  
def printBasket(basket):
  
  for item in basket.items():
    print('Quantity: ' + str(item[0]) + ' ' +item[1].getTitle() 
      + ' Total Cost: ' + "${:.2f}".format(int(item[1].getCost()) * item[0]))
    
def main():
  # read items into the itemStore
  # display menu
  # add item to basket in given quantity
  # repeat to display
  # calculate shipping

  theStore = ItemStore('dataFiles/normalSales.csv')
  basket = Basket()
  
  displayItems(theStore)
  choice = int(input('Select item (-1 to quit)'))
  
  qty = int(input('Quantity:'))
  
  addItem(theStore, basket, choice-1, qty)
  
  printBasket(basket)
  
  total = basket.getTotalShipping(ShippingLogic())
  print(total)
  total = basket.getTotalShipping(SaleShippingLogic())
  print(total)
  
  
# invoke main()
if __name__ == "__main__":
  main()
