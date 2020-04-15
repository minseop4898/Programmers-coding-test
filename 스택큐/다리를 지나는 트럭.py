def solution(bridge_length, weight, truck_weights):
    answer = 1
    q = []
    total_weight = truck_weights[0]
    q.append(truck_weights.pop(0))
    while truck_weights and q:
        if len(q) == bridge_length:
            cur_truck_weight = q.pop(0)
            total_weight -= cur_truck_weight
        if total_weight + truck_weights[0] <= weight:
            cur_truck_weight = truck_weights.pop(0)
            total_weight += cur_truck_weight
            q.append(cur_truck_weight)
        else: q.append(0)
        answer += 1
    return answer + bridge_length
