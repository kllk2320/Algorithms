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
    """
    This function solves the equation ax = b (mod n)
    :param a : nonnegative integer
    :param b : positive b 
    :return :  lcm(a, b)
    """
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


#4 Chinese remainder theorem
# The Chinese remainder theorem is not an algorithm, but a descriptive "structure 
# theorem that describes the structure of Zn as identical to that of the Cartesian
# product Zn1 * Zn2 * ... * Znk with componentwise addtion and multiplication modulo
# ni in the ith component. 
#
# The theorem was enlighted by solving the problem of finding those integers x that 
# leave remainders 2, 3, and 2 when divided by 3, 5, and 7 repsectively. In fact it
# is a statement about simultaneous congruences, of which the general form is given
# in the following.
# 
# Suppose n1, ..., nk are positve integers that are pairwise coprime. The, for any
# given sequence of integer a1, a2,..., ak, there exists an integer x solving the 
# following system of simultaneous congruences.
#
#   x = a1 (mod n1)
#   ....
#   x = ak (mod nk)
#
# The following function would find the solution x 
#
def sim_cong_solver(n, a):
    """
    :param n : set of positive integers n1, ..., nk that are pairwise coprime
    :param a : list of integers a1, a2, ... , ak. 
    :return :  x mod(n1 * n2 *...* nk)
    """
    if len(n) < 2:
        return -1
    if len(n) != len(a):
        return -1
    N = 1
    for i in range(len(n)):
        if n[i] == 0:
            return -1
        for j in range(i+1, len(n)):
            if gcd_euclid(n[i], n[j]) != 1:
                print "Wrong input argument: number %d and %d are not comprime" % (n[i], n[j])
                return -1
        a[i] = a[i] % n[i]
        N = N * n[i]
    x = 0
    for ni, ai in zip(n, a):
        m = N / ni
        m_inv = mle_solver(m, 1, ni)
        c = m * m_inv[0]
        x = x + c*ai
    return x % N
  

    


#
