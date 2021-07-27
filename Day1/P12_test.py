# Test file for P12

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P12_solution import main
from P12 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''20
	         15
	         2'''
	out = '''The final velocity is 50.0.'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''12.8
	         9.8
	         1'''
	out = '''The final velocity is 22.6.'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''125000
	         500
	         0'''
	out = '''The final velocity is 125000.0.'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''-2.5
	         5
	         10'''
	out = '''The final velocity is 47.5.'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''13.97
	         -2.5
	         13.5'''
	out = '''The final velocity is -19.78.'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

