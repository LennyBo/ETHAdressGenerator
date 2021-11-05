# ETHAdressGenerator

This short program will generate a eth key pair that has the public key that starts with a defined amount of 0

# Requirements

 * Python 3.x (tested on 3.8 and 3.9)
 * Install dependencies

At the root of the repo in a command line:
```
pip install requests
```


# Warning
I would strongly advice to not use an address generated by this program for the following reasons:
 * The seed phrase is completly random (not really a phrase)
 * The randomnes is pseudo random so that is a security risk
 
So not my fault if you loose your eth

# Starting

If everything is installed correctly you can run

```
py eth.py [n]
```

with n being the amount of 0s the address should start with

On my machine I have been able to generate an address with 7 zeros. The complexity is exponetial so I doupt it is possible to make more without proper optimizations like threads. If I really wanted to go all out, I would make a program that uses CUDA. Maybe one day...

 
