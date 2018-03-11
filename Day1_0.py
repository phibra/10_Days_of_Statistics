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
elements = list(map(int, input().split())) #Elements

elements.sort()

q1 = int(median(snip(elements, 0)))
q2 = int(median(elements))
q3 = int(median(snip(elements, 1)))        
        
print(q1)
print(q2)
print(q3)            
