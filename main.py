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
import sys


def displayItems(theStore):
	counter = 1
	print('\n')
	print(str(0).rjust(3) + '.' + ' Display Basket'.ljust(25))
	for item in theStore.items():
		print(str(item.getID()).rjust(3) + '.' + item.getTitle().ljust(25)+ '\t'+
		'\t' + "${:.2f}".format(int(item.getCost())).rjust(7) + 
		 '\t'+item.getWeight().rjust(5), end='')
		if item.getFreeShipping() :
			print(' Free Shipping!')
		else:
			print('')
		counter += 1
	print('\n')
	
def addItem(theStore, basket, itemID, qty):
	basket.addItem( [qty, theStore.getItemById(itemID)])

	
def printBasket(basket):

	totalWeight = 0	
	totalChargedWeight = 0
	print('\n=====Basket=====')
	for item in basket.items():
		print('Quantity: ' + str(item[0]) + ' ' +item[1].getTitle() 
			+ ' Total Cost: ' + "${:.2f}".format(int(item[1].getCost()) * item[0]) 
			+ ' Weight: ' + str(item[0]* int(item[1].getWeight())))
		totalWeight += item[0]* int(item[1].getWeight())
		if item[1].getFreeShipping() is False :
			totalChargedWeight += (item[0]* int(item[1].getWeight()))

	print('\nTotal Weight: ' + str(totalWeight))
	print('Total Charged Weight: ' + str(totalChargedWeight))
	print('================\n')
	
def main():
	# read items into the itemStore
	# display menu
	# add item to basket in given quantity
	# repeat to display
	# calculate shipping

	
	theStore = ItemStore(sys.argv[1])
	basket = Basket()
	
	choice = 0
	
	while choice != -1 :
	
		displayItems(theStore)
		choice = int(input('Select item (-1 to quit) '))
	
		if choice == 0:
			printBasket(basket)
			total = basket.getTotalShipping(ShippingLogic())
			print('Estimated Shipping cost: '+ str(total))
			
		elif choice != -1:
			qty = int(input('Quantity: '))
	
			addItem(theStore, basket, choice, qty)
	
	printBasket(basket)
	
	total = basket.getTotalShipping(ShippingLogic())
	print('Normal Shipping cost: '+ str(total))
	total = basket.getTotalShipping(SaleShippingLogic())
	print('Sale Shipping cost: '+ str(total))

# invoke main()
if __name__ == "__main__":
	main()
