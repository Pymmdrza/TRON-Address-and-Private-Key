from tronpy import keys
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider


a=1
while (a<=100):

    priv_key = PrivateKey.random()
    xbase = priv_key.public_key.to_base58check_address()
    xHex = priv_key.public_key.to_hex_address()
    Prix = priv_key.hex()
    xPub = priv_key.public_key.hex()

    print("\n\n===========================")
    print(str(a)+" --> Account information ")
    print("---------------------------")
    print("Address >=>",xbase)
    print("---------------------------")
    print("Hex >=>", xHex)
    print("---------------------------")
    print("Private Key >=>", Prix)
    print("---------------------------")
    print("Public Address >=>", xPub)
    print("---------------------------")
    a=a+1
