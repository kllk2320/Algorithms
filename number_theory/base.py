# Just for self-study
from numpy import *
from math import sqrt
from random import randint
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

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
  

    
#5 Modular Exponentiation
#  The following function would compute the modular exponentiation (a^b % n)
#  efficiently by the method of repeated squaring 
#
def modular_exp(a, b, n):
    """
    :param a : base, a nonnegative integer
    :param b : exponent, a nonnegative integer
    :param n : modulo, a postive integer
    """
    if a < 0 or b < 0 or n <= 0:
        return -1
    b_str = bin(b)[2:]
    d = 1
    for i in b_str:
        d = (d*d) % n
        if i == '1':
            d = (d * a) % n
    return d



#6 Primality testing
#a. Important theorems related to primality testing
#a.1 Prime number theorem
#  The number of primes that are less than or equal to n approximates to n/ln(n) as n grows to infinite
#a.2 If p is an odd prime, and e >= 1, then the equation x^2 = 1 (mod p^e) has only two solutions, x = 1
#     or x = -1.
#    If there exists a nontrivial square root of 1, modulo n, then n is composite.
#

#6.1 Pseudoprimality testing
def pseudoprime(a, n):
    """
    This function tests whether n is composite or base-a pseudo prime. If it returns
    False, then n is definitely composite. If it returns True, then n is base-a pseudo
    prime, which is very likely prime. 
    So it gives a very simple method for primality testing that "almost works" 
    and in fact is good enough for many pratical applicaton. 

    a: a base number, normally 2 is chosen
    n: an odd integer greater than 2
    return : False, n is not prime (definitely)
             True,  n is prime (most likely)
    """
    if a < 2 or n < 2 or n & 1 == 0:
        return False
    if modular_exp(a, n-1, n) != 1 :
        return False    # n is definitley a composite number
    else :
        return True    # n is most likely a prime number 
    
#6.2 Miller-Rabin primality testing
# An improved version of pseudoprime testing with 2 modifications:
#  a. It tries several randomly chosen base values a instead of just one base value
#  b. While computing each modular exponentiation, it looks for a nontrival square 
#     square root of 1, modulo n, during the final set of squarings. If it finds one,
#     it stops and returns composite. 

# First, we need an auxiliary procedure called 'witness' such that 'witness(a, n)' 
# is TRUE if and only if a is a "witness" to the compositeness of n, that is if it
# is possible using a to prove that n is composite.
def witness(a, n):
    if a < 2 or n < 2 or n & 1 == 0:
        return True
    u = n-1
    t = 0
    while u & 1 == 0:
        u = u >> 1
        t = t + 1
    x0 = modular_exp(a, u, n)
    logger.debug("[FUNC: %s] u = %d, t = %d", __name__, u, t)
    #print "u=%d t= %d" % (u, that)
    while t:
        #print x0
        x1 = (x0 * x0) % n
        if x1 == 1 and x0 != 1 and x0 != n - 1:
            return True
        x0 = x1
        t = t - 1
    if x1 != 1:
        return True
    return False
    
#
def miller_rabin(n, s):
    if n < 2 or n & 1 == 0:
        return False
    if s < 1:
        print "ERROR: s must be positive integer"
        return False
    while s:
        a = randint(1, n-1)
        if witness(a, n) == True:
            #print a
            return False
        s = s -1
    return True
