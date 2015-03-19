# Just for self-study
from numpy import *
from math import sqrt

#1 GCD computing
#
#1.1 Euclid's algorithm (GCD recursion theorem):
#
#	For any nonnegative integer a and any positive integer b,
#
#		gcd(a,b) = gcd(b, a mod b)
#   
# Time complexity: O(lgb)
def gcd_euclid(a, b):
    """
    :param a : nonnegative integer
    :param b : positive b 
    :return :  0 (Wrong input parameters) 
               gcd(a,b)
    """
    if a < 0 or b < 0: 
        return 0
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a % b)

def gcd_euclid_nr(a, b):
    """
    This is an iterative form that uses only a constant 
    amount of memory(without recursive function call)

    :param a : nonnegative integer
    :param b : positive b 
    :return :  0 (Wrong input parameters) 
               gcd(a,b)
    """
    if a < 0 or b < 0: 
        return 0
    while b != 0:
        tmp = b
        b = a % tmp
        a = tmp
    return a
        


#1.2 Extended form of Euclid's algorithm:
#  The following function extends Euclid's algorithm to compute integer
#  conefficients x and y such that:
#
#  		d = gcd(a, b) = ax + by.
#
#  where x and y may be zero or negative 
#
# Time complexity: O(lgb)
def gcd_euclid_ext(a, b):
    """
    :param a : nonnegative integer
    :param b : positive b 
    :return : (d, x, y)
    """
    if a < 0 or b < 0: 
        return 0, 0, 0
    elif b == 0:
        return (a, 1, 0)
    else:
	d0, x0, y0 = gcd_euclid_ext(b, a%b)
        d = d0
        x = y0 
        y = x0 - (a/b) * y0 
        return (d, x, y)
	

#2 LCM Computing:
#2.1
#  The following function computes the least common multiple of two integers
#  using the gcd operationi as subroutine
#
def lcm(a, b):
    """
    :param a : nonnegative integer
    :param b : positive b 
    :return :  lcm(a, b)
    """
    d = gcd_euclid(a, b)
    return a * (b /d)
    



#3 Solving modular linear equations
#  The following function solves the equation  ax = b(mod n), and returns all 
#  solutions to this equation
#
def mle_solver(a, b, n):
    s = []
    d, x, y = gcd_euclid_ext(a, n)
    if b % d == 0:
        s0 = (x * ( b / d)) % n
        order = n/d
        tmp  = s0
        while d != 0:
            s.append((tmp % n))
            tmp = tmp + order
            d = d - 1
    return s
