""""This module work with anagrams"""
n = int(input())
Dict = {}
for i in range(0, n):
    word = input()
    tmp = list(word)
    tmp.sort()
    Dict[word] = tmp
Used = set()
Dict = dict(sorted(Dict.items(), key=lambda item: item[1]))
keys = list(Dict.keys())
check = len(keys)
print(keys[0], end=' ')
cnt = 1
for i in Dict:
    if i == keys[check - 1]:
        continue
    if Dict[i] == Dict[keys[cnt]]:
        print(keys[cnt], end=' ')
    else:
        print()
        print(keys[cnt], end=' ')
    cnt += 1
