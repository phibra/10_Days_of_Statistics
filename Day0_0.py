from collections import Counter

N = int(input()) # Number of elements
raw_input = input() # Elements

elements = []

for i in raw_input.split(" "):
	elements.append(int(i))
	
elements.sort()


# Mean
mean = sum(elements) / N

# Median
if (N % 2 == 0):
	median = (elements[int(N / 2 - 1)] + elements[int(N / 2)]) / 2
else:
	median = elements[int(N / 2)]

# Mode
mode = 0
count = 0


for i in elements:
	countTemp = elements.count(i)
	if (countTemp > count):
		count = countTemp
		mode = i
	
# Output
print(mean)
print(median)
print(mode)