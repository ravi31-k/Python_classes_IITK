# Test file for P13

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P13_solution import main
from P13 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''20
	         15
	         2'''
	out = '''The displacement is 70.0.'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''12.8
	         9.8
	         1'''
	out = '''The displacement is 17.7.'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''125000
	         500
	         0'''
	out = '''The displacement is 0.0.'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''-2.5
	         5
	         10'''
	out = '''The displacement is 225.0.'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''13.97
	         -2.5
	         13.5'''
	out = '''The displacement is -39.22.'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

