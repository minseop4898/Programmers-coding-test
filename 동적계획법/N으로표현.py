from itertools import product

def solution(N, number):
    material = {1 : [N]}
    if N == number: return 1
    
    for i in range(2, 9):
        material[i] = [int(str(N)*i)]
        for j in range(1, (i//2)+1):
            for k in list(product(material[j], material[i-j])):
                a, b = k
                if not a + b in material[i]:
                    material[i].append(a + b)
                if not a - b in material[i]:
                    material[i].append(a - b)
                if not b - a in material[i]:
                    material[i].append(b - a)
                if not a * b in material[i]:
                    material[i].append(a * b)
                if b != 0 and a % b == 0 and not a / b in material[i]:
                    material[i].append(a / b)
                if a != 0 and b % a == 0 and not b / a in material[i]:
                    material[i].append(b / a)
        if number in material[i]:
            return i
    return -1