#
#
#

import secrets
from math import pow
import sympy 

systemRandomGenerator = secrets.SystemRandom()
P = sympy.randprime(1000000, 100000000)
print('the prime is- ', P)
M = '396'
print('the original message is-', M )

def getKeys(P):
    g = 7                               
    privateKey = systemRandomGenerator.randint(2, 13)
    print(privateKey)
    publicKey = (g ** privateKey) % P  # big X
    return {publicKey: privateKey}    

# key generation:
aliceKeys = getKeys(P)
print(aliceKeys)

# encryption:
bobKeys = getKeys(P)
print(bobKeys)
cKeys1 = list(aliceKeys.keys())[0] # alice public key
cKeys2 = list(bobKeys.values())[0]# bobs private key
print(int(cKeys1), int(cKeys2))
print(2519654 ** 34)
cipherMessage = int(M) * (int(cKeys1) ** int(cKeys2) % P)
BpublicKey = list(bobKeys.keys())[0]
print(BpublicKey, cipherMessage)

# decryption:
AprivateKey = list(aliceKeys.values())[0]
commonKey = BpublicKey ** AprivateKey
inverseValue = sympy.mod_inverse(commonKey,P)
M = (cipherMessage * (inverseValue) % P) 

print('The decrypted message is-', M)