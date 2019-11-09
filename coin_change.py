def mincoin(coins,val):
	if val == 0 : return 0
	res = 999
	for i in range(len(coins)) : 
		if coins[i] <= val : subres = mincoin(coins,val-coins[i]) 
		if subres + 1 < res : res = subres + 1
	return res

coins = [10,5,2,1]
print(mincoin(coins,11))
