# -*- coding: utf-8 -*-
x = int(input())
count = 0
while count < 6:
    if x % 2 != 0:
        print(x)
        count += 1
    x += 1
