#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

num = 0
begin = time.time()
print(begin)
for i in range(10000):
    pass
end = time.time()
print(num)
print(end)
print(end-begin)
