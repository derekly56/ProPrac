def maxSubSequence(arr):
	total = 0
	ans = []

	for i in arr:
		if i > 0:
			total += i
			ans.append(i)

	if total > 0:
		print(total)
		print(ans)
	else:
		print(max(arr))
		print(arr)

app = [-1,-2,5,-8]

maxSubSequence(app)
