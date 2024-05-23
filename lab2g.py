#!/usr/bin/env python3
import sys

#Author: Lou Gardie Iringan Campos
#Author: 135443224
#Date Created: 2024/05/23
if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    print(f"Usage: {sys.argv[0]} [timer]")
    sys.exit(1)
    
while timer > 0:
    print(timer)
    timer = timer - 1
print('blast off!')