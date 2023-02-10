"""This module make sum of concatenations"""

number, times = input().split()
SUM_OUT = 0
for i in range(0, int(times)):
    tmp = number * (i + 1)
    SUM_OUT += int(tmp)
print(SUM_OUT)
