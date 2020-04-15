def solution(numbers, target):
    answer = recursion(numbers, 0, target)
    return answer

def recursion(numbers, total_sum, target):
    answer = 0
    if len(numbers) == 1:
        if numbers[0]+total_sum == target or -numbers[0]+total_sum == target: return 1
        else: return 0
    answer += recursion(numbers[1:], total_sum+numbers[0], target)
    answer += recursion(numbers[1:], total_sum-numbers[0], target)
    return answer
