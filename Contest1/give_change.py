# count number of coins to change
def count_coins(tmp, denomination):
    cnt_coin = 0
    while tmp >= denomination:
        tmp = tmp - denomination
        cnt_coin += 1
    return cnt_coin


INPUT_NUM = float(f"{float(input()):.{2}f}")
INPUT_NUM = INPUT_NUM * 100
SUM_COINS = count_coins(INPUT_NUM, 1000)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - 1000 * SUM_COINS
    print(f"{10.00:{5}.{2}f}", SUM_COINS, sep='\t')
SUM_COINS = count_coins(INPUT_NUM, 500)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - 500 * SUM_COINS
    print(f"{5.00:{5}.{2}f}", SUM_COINS, sep='\t')
SUM_COINS = count_coins(INPUT_NUM, 200)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - 200 * SUM_COINS
    print(f"{2.00:{5}.{2}f}", SUM_COINS, sep='\t')
SUM_COINS = count_coins(INPUT_NUM, 100)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - 100 * SUM_COINS
    print(f"{1.00:{5}.{2}f}", SUM_COINS, sep='\t')
SUM_COINS = count_coins(INPUT_NUM, 50)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - 50 * SUM_COINS
    print(f"{0.50:{5}.{2}f}", SUM_COINS, sep='\t')
SUM_COINS = count_coins(INPUT_NUM, 10)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - 10 * SUM_COINS
    print(f"{0.10:{5}.{2}f}", SUM_COINS, sep='\t')
SUM_COINS = count_coins(INPUT_NUM, 5)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - 5 * SUM_COINS
    print(f"{0.05:{5}.{2}f}", SUM_COINS, sep='\t')
SUM_COINS = count_coins(INPUT_NUM, 1)
if SUM_COINS:
    INPUT_NUM = INPUT_NUM - SUM_COINS
    print(f"{0.01:{5}.{2}f}", SUM_COINS, sep='\t')
