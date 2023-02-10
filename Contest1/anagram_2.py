""""This module work with anagrams strings"""
str1 = input()
str1 = str1.lower()
str1 = list(str1.split(' '))
str2 = input()
str2 = str2.lower()
str2 = list(str2.split(' '))
str2.sort()
str1.sort()
if len(str1) < len(str2):
    print('NO')
else:
    cnt = 0
    for word2 in range(0, len(str2)):
        if cnt == len(str1):
            print('NO')
            break
        while str2[word2] > str1[cnt]:
            cnt += 1
        if str2[word2] != str1[cnt]:
            print('NO')
            break
        else:
            cnt += 1
    else:
        print('YES')
