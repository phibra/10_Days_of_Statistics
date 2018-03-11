def median(inputList):
    length = len(inputList)
    
    if (length % 2 == 0):
        return((inputList[int(length / 2 - 1)] + inputList[int(length / 2)]) / 2)
    else:
        return(inputList[int(length / 2)])


def snip(inputList, part):
    length = len(inputList)
    
    if (length % 2 == 0):
        begin = inputList[:int(length/2)]
        end = inputList[int(length/2):]
    else:
        begin = inputList[:int(length/2)]
        end = inputList[int(length/2) + 1:]
        
    if part == 0:
        return begin
    else:
        return end
    

N = int(input()) # Number of elements
element = list(map(int, input().split())) 
frequency = list(map(int, input().split())) 

elements = []

for i in range(N):
    for j in range(frequency[i]):
        elements.append(element[i])

elements.sort()

q1 = median(snip(elements, 0))
q3 = median(snip(elements, 1))

interquartileRange = round(q3 - q1 * 1.0, 1)

print(interquartileRange)
