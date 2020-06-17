from itertools import permutations

def solution(numbers):
    num_set = set()
    for i in range(1, len(numbers)+1):
        num_set = num_set.union(set(map(''.join, list(permutations(numbers, i)))))
    num_set = set(map(int, num_set))
    
    return sum(list(map(is_prime, num_set)))

def is_prime(num):
    if num <= 1:
        return 0
    i = 2
    while i**2 <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1