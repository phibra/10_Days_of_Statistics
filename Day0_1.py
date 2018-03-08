N = int(input()) # Number of elements
rawInputElements = input() # Elements
rawInputWeight = input() # Elements

elements = []
weight = []

for i in rawInputElements.split(" "):
	elements.append(int(i))
	
for i in rawInputWeight.split(" "):
	weight.append(int(i))

	
numerator = 0
denominator = 0

for i in range(N):
	numerator += (elements[i] * weight[i])
	denominator += weight[i]
	
weightedMean = round(numerator / denominator, 1)

print(weightedMean)