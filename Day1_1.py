N = int(input()) # Number of elements
elements = list(map(int, input().split())) #Elements

value = 0
mean = sum(elements) / N

for i in elements:
    value += (i - mean) ** 2
   
standardDeviation = round((value / N) ** 0.5, 1)

print(standardDeviation)
