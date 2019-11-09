import sys


def coin_change(coins,val):
	n = len(coins)
	if val == 0 : return 0
	res = sys.maxsize
	#print(res)
	for i in range(n):
		if coins[i] <= val : subres = coin_change(coins,val - coins[i])
		#print(subres,res)
		if subres != sys.maxsize and subres + 1 < res : res = subres + 1

	return res

coins = [1,2,5,10]
inp = int(input("enter val : "))
print(coin_change(coins,inp))