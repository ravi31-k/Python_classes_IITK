# Test file for P21

import sys, os, pytest
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P21_solution import main
from P21 import main

############ TEST CASES BEGIN ############

def test_case1():
	inp = '''18\n80\n90\n45'''
	out = '''8.6'''
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '''20\n100\n100\n50'''
	out = '''10.0'''
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = '''0\n27\n41\n13'''
	out = '''2.55'''
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''19\n99\n99\n49'''
	out = '''9.81'''
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = '''1\n80\n61\n11'''
	out = '''5.05'''
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

