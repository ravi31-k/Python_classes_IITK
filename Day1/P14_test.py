# Test file for P14

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P14_solution import main
from P14 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''5'''
	out = '''0:0:5'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''67'''
	out = '''0:1:7'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''601'''
	out = '''0:10:1'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''3692'''
	out = '''1:1:32'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''7199'''
	out = '''1:59:59'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

