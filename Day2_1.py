from fractions import Fraction

elements = []
counter = 0
counter9 = 0

for i in range(1,7):
    for j in range(1,7):
        counter += 1
        if (i + j == 6) and (i != j):            
            counter9 += 1

print(Fraction(counter9, counter))
