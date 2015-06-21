# Just for self-study
from numpy import *
from base import *

#1 RSA Key generate

def gen_d(p, q, e):
    n = p * q
    phi_n = (p-1) *(q-1)
    d = mle_solver(e, 1, phi_n)
    return d[0]

#Encryption/Decryption
def encrypt(K, M):
    e = K[0]
    n = K[1]
    C = modular_exp(M, e, n)
    return C



