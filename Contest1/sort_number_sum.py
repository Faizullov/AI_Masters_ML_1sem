# Sort array by sum of numbers in each number
def num_sum(tmp_number):
    # Count sum of numbers in number
    sum_num = 0
    while tmp_number > 0:
        dig = tmp_number % 10
        sum_num = sum_num + dig
        tmp_number = tmp_number // 10
    return sum_num


Output = []
Lst = []
n = int(input())
input_tmp = map(int, input().split())
input_tmp = list(input_tmp)
for i in range(0, n):
    inp_sum_num = num_sum(input_tmp[i])
    Lst.append((inp_sum_num, input_tmp[i]))
Lst = sorted(Lst)
for i in range(0, n):
    Output.append(Lst[i][1])
print(*Output, sep=" ")
