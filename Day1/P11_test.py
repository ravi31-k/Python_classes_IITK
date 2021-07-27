# Test file for P11

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P11_solution import main
from P11 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''212'''
	out = '''Fahrenheit temperature 212.0 is the same as 100.0 degrees Celsius.'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''0.555'''
	out = '''Fahrenheit temperature 0.555 is the same as -17.47 degrees Celsius.'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''-23'''
	out = '''Fahrenheit temperature -23.0 is the same as -30.56 degrees Celsius.'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''-40'''
	out = '''Fahrenheit temperature -40.0 is the same as -40.0 degrees Celsius.'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''373.0'''
	out = '''Fahrenheit temperature 373.0 is the same as 189.44 degrees Celsius.'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

