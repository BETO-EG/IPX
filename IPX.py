# -*- coding: utf-8 -*-
import requests, sys
from time import time as timer
from multiprocessing.dummy import Pool as ThreadPool
import ctypes

x =  """
          _____                    _____             _____                   _______         
         /\    \                  /\    \           /\    \                 /::\    \        
        /::\    \                /::\    \         /::\    \               /::::\    \       
       /::::\    \              /::::\    \        \:::\    \             /::::::\    \      
      /::::::\    \            /::::::\    \        \:::\    \           /::::::::\    \     
     /:::/\:::\    \          /:::/\:::\    \        \:::\    \         /:::/~~\:::\    \    
    /:::/__\:::\    \        /:::/__\:::\    \        \:::\    \       /:::/    \:::\    \   
   /::::\   \:::\    \      /::::\   \:::\    \       /::::\    \     /:::/    / \:::\    \  
  /::::::\   \:::\    \    /::::::\   \:::\    \     /::::::\    \   /:::/____/   \:::\____\ 
 /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\    \   /:::/\:::\    \ |:::|    |     |:::|    |
/:::/__\:::\   \:::|    |/:::/__\:::\   \:::\____\ /:::/  \:::\____\|:::|____|     |:::|    |
\:::\   \:::\  /:::|____|\:::\   \:::\   \::/    //:::/    \::/    / \:::\    \   /:::/    / 
 \:::\   \:::\/:::/    /  \:::\   \:::\   \/____//:::/    / \/____/   \:::\    \ /:::/    /  
  \:::\   \::::::/    /    \:::\   \:::\    \   /:::/    /             \:::\    /:::/    /   
   \:::\   \::::/    /      \:::\   \:::\____\ /:::/    /               \:::\__/:::/    /    
    \:::\  /:::/    /        \:::\   \::/    / \::/    /                 \::::::::/    /     
     \:::\/:::/    /          \:::\   \/____/   \/____/                   \::::::/    /      
      \::::::/    /            \:::\    \                                  \::::/    /       
       \::::/    /              \:::\____\                                  \::/____/        
        \::/____/                \::/    /                                   ~~              
         ~~                       \/____/                                                    
                                                                                             


||||||||THANKS FOR SIRBUGS|||||
"""
print x
try:
    with open(raw_input('IPS BETO '), 'r') as f:
        beto = f.read().splitlines()
except IOError:
    pass
beto = list((beto))

good = 0
totalnum = len(beto)

def data_url(ip):
    global good
    global totalnum
    ctypes.windll.kernel32.SetConsoleTitleA('CPANEL IPS CHECKER BETO |THANKS FOR SIR.BUGS||IPS {} | {}'.format(good, totalnum))
    try:

        req = requests.get("http://" + ip + "/cpanel")

        if 'cpanel-logo.svg' in req.content:
            print('CPANEL IPS : {} |TOTAL IPS CPANEL {}|').format(ip, good)
            open('ip_cpanel.txt', 'a').write(ip + '\n')
            good += 1
        else:
            print('NOT CPANEL IP : {}  ...!').format(ip)

    except:
        pass

def Main():
    try:
        start = timer()
        pp = ThreadPool(2)
        pr = pp.map(data_url, beto)
    except:
        pass


if __name__ == '__main__':
    Main()