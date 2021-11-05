from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from colorama import Fore

import sys

n = 0

if len(sys.argv) == 1:
    print(Fore.RED + "Missing argument.\nCall the script like '" + Fore.GREEN + "py eth.py 3" + Fore.RED + "'")
    exit(-1)
else:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print(Fore.RED + "Could not parse int of argument 1\nCall the script like '" + Fore.GREEN + "py eth.py 3" + Fore.RED + "'")
        exit(-1)


n1 = -(n-1)
str = "0" * n
private_key = "a"
public_key = "a"
addr = 0
while True:
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    if addr.hex()[0:n] == str:
        break


print('private_key:', private_key.hex())
print('eth addr: 0x' + addr.hex())