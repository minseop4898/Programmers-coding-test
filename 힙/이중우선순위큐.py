import heapq

def solution(operations):
    heap = []
    
    for op_str in operations:
        op, num = op_str.split()
        if op == 'I':
            heapq.heappush(heap, int(num))
        elif op == 'D':
            if len(heap) == 0: continue
            if num == '-1':
                heapq.heappop(heap)
            elif num == '1':
                heap.remove(max(heap))
    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap), heap[0]]
    return answer
