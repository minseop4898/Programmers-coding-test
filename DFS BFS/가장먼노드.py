import queue

def solution(n, edge):
    answer = 0
    distance = [0 for _ in range(n+1)]
    visited = set([1])
    node_queue = queue.Queue()
    node_queue.put(1)
    adj_dict = {}
    for i in range(n):
        adj_dict[i+1] = []
    for e in edge:
        adj_dict[e[0]].append(e[1])
        adj_dict[e[1]].append(e[0])
    
    while node_queue.qsize() != 0:
        node = node_queue.get()
        
        for next_node in adj_dict[node]:
            if not next_node in visited:
                node_queue.put(next_node)
                visited.add(next_node)
                distance[next_node] = distance[node] + 1
    answer = distance.count(max(distance))
    return answer
