# Test file for P24

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P24_solution import main
from P24 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''Food is not bad.'''
	out = '''Food is good.'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''The lyrics is not that bad!'''
	out = '''The lyrics is good!'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''!! not !! bad !!'''
	out = '''!! good !!'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''*notbad*'''
	out = '''*good*'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''The song is not extremely gently bad for my ears.'''
	out = '''The song is good for my ears.'''
	res = run(main, inp)
	assert (out == res)

def test_case6():
	inp = '''The sight is not very very bad.'''
	out = '''The sight is good.'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

