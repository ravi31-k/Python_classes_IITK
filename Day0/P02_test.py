# Test file for P02

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P02 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''AK'''
	out = '''Hi AK\nBye AK'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''**'''
	out = '''Hi **\nBye **'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''\\n'''
	out = '''Hi \\n\nBye \\n'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''Everyone'''
	out = '''Hi Everyone\nBye Everyone'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''Every1'''
	out = '''Hi Every1\nBye Every1'''
	res = run(main, inp)
	assert (out == res)



