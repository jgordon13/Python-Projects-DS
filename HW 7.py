# Author: Julia Gordon 
# Date: 3/22/22
# HW 7: 
"""Create an implementation of the Diffie-Hellman key exchange 
protocol with Python. Diffie-Hellman key exchange
Alice and Bob use Diffie-Hellman key exchange to share secrets. They start 
with prime numbers, pick private keys, generate and share public keys, and 
then generate a shared secret key."""

import random 
P = 2946901
G = 7

def dHKeyExchange(p,g):
    x = random.randrange(2,p)
    publicKey = pow(g,x) % p 
    return {x:publicKey}

alice = dHKeyExchange(P,G)
bob= dHKeyExchange(P,G)

commonKey = pow(list(bob.values())[0],list(alice.keys())[0]) % P

print(commonKey)