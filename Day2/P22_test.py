# Test file for P22

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P22_solution import main
from P22 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''Can you write a whole paragraph without the letter a? I wouldn't recommend it. Honestly, your sentences will sound wrong. Not just you but everyone else too will notice you are doing something weird. You will use uncommon words. It's not worth the effort involved.\nwill'''
	out = '''3'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''""\nthe'''
	out = '''0'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''She never liked cleaning the sink. It was beyond her comprehension how it got so dirty so quickly. It seemed that she was forced to clean it every other day. Even when she was extra careful to keep things clean and orderly, it still ended up looking like a mess in a couple of days. What she didn't know was there was a tiny creature living in it that didn't like things neat.\nit'''
	out = '''4'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''Do you really listen when you are talking with someone??? I have a friend who listens in an unforgiving way? She actually takes every word you say as being something important and when you have a friend that listens like that, words take on a whole new meaning.\n?'''
	out = '''4'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''Barbara had been waiting at the table for twenty minutes. it had been twenty long and excruciating minutes. David had promised that he would be on time today. He never was, but he had promised this one time. She had made him repeat the promise multiple times over the last week until she'd believed his promise. Now she was paying the price.\nshe'''
	out = '''2'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

