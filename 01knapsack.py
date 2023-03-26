'''
0/1 knapsack problem

Given a set of n items with p profits and w weights and a bag with c capacity, return the set of items that fit in the bag and maximize profit

Basic idea - Use a 2D DP array to store the optimal solution to subproblems.

Without DP: O(2^n)) where n = # items
With DP: O(nw) where n = # items and w = bag capacity 

DP decision (v = DP array):
	if i = 0 or w = 0:
		v[i,w] = 0
	else if obj weight <= capacity:
		v[i,w] = max{v[i-1,w] , v[i-1,w-w[i]]+p[i]}
	else:
		v[i,w] = v[i-1,w]
'''

def zeroOneKnapsack(capacity, objects):
	n = len(objects)
	dp = [[0 for j in range(capacity+1)] for i in range(len(objects)+1)]
	#for row in dp:
	#	print(row)
	#for currentCap in range(capacity):
	#	print(currentCap)
	weights = [row[0] for row in objects]
	profits = [row[1] for row in objects]
	print(f'\nprofits: {profits}')
	print(f'weights: {weights}')

	for i in range(len(dp)):
		for w in range(len(dp[0])):
			if i == 0 or w == 0:
				continue
			elif (weights[i-1] <= w):
				dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+profits[i-1])
			else:
				dp[i][w] = dp[i-1][w]

	print('\nFinal DP Array:')
	for row in dp:
		print(row)
	return dp[-1][-1]

## DRIVER CODE FOR TESTING
def main():
	objects = [[2,1],[3,2],[4,5],[5,6]]
	capacity = 8
	ans = zeroOneKnapsack(capacity, objects)
	print(f"\nMaximum Profit: {ans}")

if __name__ == '__main__':
	main()
