# Check array for duplicates
A = []
Output = []
Scores = set()
COUNTER = 0
n = int(input())
input_tmp = map(int, input().split())
input_tmp = list(input_tmp)
for i in range(0, n):
    if input_tmp[i] not in Scores:
        Scores.add(input_tmp[i])
    A.append(input_tmp[i])
for i in range(0, n):
    if A[i] in Scores:
        Scores.remove(A[i])
        Output.append(A[i])
    else:
        COUNTER += 1
print(*Output, sep=" ")
print(COUNTER)
