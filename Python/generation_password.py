# -*- coding:utf -8 -*-
#!/usr/bin/python3

import json
import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(input("Введите количество паролей:" + '\n'))
length = int(input('длина паролей?' + '\n'))

for n in range(number):
    password = ''
    for i in range(length):
        password +=random.choice(chars)
    print(password)
    
   
