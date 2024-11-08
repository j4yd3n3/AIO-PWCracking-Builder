import os
import sys
import src.leet
import src.append
import src.prepend
import src.toggles
import src.utils


char_possibilities = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(){}[]:\"\\/|;,.<>~-_=0123456789")

def append_digit(orig:set) -> set:
	for word in orig:
		append_combinations = set()
		for i in range(0,10):
			append_combinations.add(word + str(i))
	return append_combinations

def append_2digit(orig:set) -> set:
	append_combinations = set()
	for word in orig:
		for i in range(10,100):
			append_combinations.add(word + str(i))
	return append_combinations

def append_3digit(orig:set) -> set:
	for word in orig:
		append_combinations = set()
		for i in range(100,1000):
			append_combinations.add(word + str(i))
	return append_combinations

def append_uno(orig: set) -> set:
    append_combinations = set()
    for word in orig:
        for char in char_possibilities:
            append_combinations.add(word + char) 
    return append_combinations

def append_dos(orig: set) -> set:
    append_combinations = set()  
    for word in orig:
        for char1 in char_possibilities:
            for char2 in char_possibilities:
                append_combinations.add(word + char1 + char2)
    return append_combinations

def append_tres(orig: set) -> set:
    append_combinations = set()  
    for word in orig:
        for char1 in char_possibilities:
            for char2 in char_possibilities:
            	for char3 in char_possibilities:
                	append_combinations.add(word + char1 + char2 + char3) 
    return append_combinations
