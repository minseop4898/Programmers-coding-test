def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    boat = 0
    boat_count = 0
    last_idx = len(people)-1
    for i, p in enumerate(people):
        if i == last_idx:
            if boat_count == 0:
                return answer + 1
            else:
                if boat+p <= limit:
                    return answer
                else:
                    return answer + 1
            return 
        if boat_count == 0:
            boat_count = 1
            answer += 1
            boat += p
        elif boat_count ==1:
            boat_p = boat + p
            boat_idx = boat + people[last_idx]
            if boat_p <= limit:
                boat = 0
                boat_count = 0
            elif boat_idx <= limit:
                boat = p
                answer += 1
                boat_count = 1
                last_idx -= 1
            else:
                boat = p
                answer += 1
                boat_count = 1
