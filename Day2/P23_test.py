# Test file for P23

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P23_solution import main
from P23 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''Nitin'''
	out = '''Nitin True'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''Uma'''
	out = '''Uma False'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''AmeyemA'''
	out = '''AmeyemA True'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''Tintin'''
	out = '''Tintin False'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''Amy Yummy'''
	out = '''Amy Yummy False'''
	res = run(main, inp)
	assert (out == res)

def test_case6():
	inp = '''Amrev Verma'''
	out = '''Amrev Verma True'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

