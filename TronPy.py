import ecdsa
import base58
import requests
from Crypto.Hash import keccak
from tronpy.keys import PrivateKey
import colorama
from colorama import Fore, Back, Style

colorama.init()


print("Please Wait...")

a = 1
while True:

    priv_key = PrivateKey.random()
    xbase = priv_key.public_key.to_base58check_address()
    xHex = priv_key.public_key.to_hex_address()
    Prix = priv_key.hex()
    xPub = priv_key.public_key.hex()
    bloc = requests.get("https://apilist.tronscan.org/api/account?address=" + xbase)
    res = bloc.json()
    balances = dict(res)["balance"]
    transaction = dict(res)["totalTransactionCount"]
    frozen = dict(res)["totalFrozen"]

    print("\n\n===========================")
    print(str(a) + " --> Account information ")
    print("---------------------------")
    print(Fore.YELLOW + "Address :" + xbase + " " + Style.RESET_ALL)
    print("---------------------------")
    print(Fore.LIGHTRED_EX + "Hex :", xHex + " " + Style.RESET_ALL)
    print("---------------------------")
    print(Fore.LIGHTWHITE_EX + "Private Key :", Prix + " " + Style.RESET_ALL)
    print("---------------------------")
    print(Fore.LIGHTGREEN_EX + "Public Address :", xPub + " " + Style.RESET_ALL)
    print("---------------------------")
    print(
        Fore.RED
        + "[ "
        + " Balance = "
        + str(balances)
        + " | "
        + "  Frozen  = "
        + str(frozen)
        + " | "
        + "  Transactions = "
        + str(transaction)
        + " ]"
        + Style.RESET_ALL
    )
    a = a + 1
