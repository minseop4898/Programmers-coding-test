from itertools import permutations

def solution(baseball):
    digit = [str(i) for i in range(1, 10)]
    candidate = set(map(''.join, permutations(digit, 3)))
    for game in baseball:
        number, strike, ball = game
        number = str(number)
        
        remove_set = set()
        for cand in candidate:
            temp_strike, temp_ball = 0, 0
            for i in range(3):
                if number[i] == cand[i]: temp_strike += 1
                elif number[i] in cand: temp_ball += 1
            if temp_strike != strike or temp_ball != ball:
                remove_set = remove_set.union([cand])
        candidate = candidate.difference(remove_set)
    return len(candidate)