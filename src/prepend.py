import os
import sys
import src.leet
import src.append
import src.prepend
import src.toggles
import src.utils


char_possibilities = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(){}[]:\"\\/|;,.<>~-_=0123456789")

def prepend_digit(orig:set) -> set:
	prepend_combinations = set()
	for word in orig:
		for i in range(0,10):
			prepend_combinations.add(str(i) + word)
	return prepend_combinations

def prepend_2digit(orig:set) -> set:
	prepend_combinations = set()
	for word in orig:
		for i in range(0,100):
			prepend_combinations.add(str(i) + word)
	return prepend_combinations

def prepend_3digit(orig:set) -> set:
	prepend_combinations = set()	
	for word in orig:
		for i in range(0,1000):
			prepend_combinations.add(str(i) + word)
	return prepend_combinations

def prepend_uno(orig: set) -> set:
    prepend_combinations = set()
    for word in orig:
        for char in char_possibilities:
            prepend_combinations.add(char+word) 
    return prepend_combinations

def prepend_dos(orig: set) -> set:
    prepend_combinations = set()  
    for word in orig:
        for char1 in char_possibilities:
            for char2 in char_possibilities:
                prepend_combinations.add(char1 + char2 + word)
    return prepend_combinations

def prepend_tres(orig: set) -> set:
    prepend_combinations = set()  
    for word in orig:
        for char1 in char_possibilities:
            for char2 in char_possibilities:
            	for char3 in char_possibilities:
                	prepend_combinations.add(char1 + char2 + char3 + word) 
    return prepend_combinations
