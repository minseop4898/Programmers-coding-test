import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    heap = []
    job_idx = 0
    global_time = 0
    cur_job_time = 0
    stage_flag = False
    answer = []
    while True:
        while job_idx < len(jobs) and jobs[job_idx][0] == global_time:
                    heapq.heappush(heap,(jobs[job_idx][1], jobs[job_idx]))
                    job_idx += 1
        if not stage_flag:
            if len(heap) > 0:
                stage_flag = True
                cur_job = heapq.heappop(heap)[1]
        
        global_time +=1
        if stage_flag:
            cur_job_time += 1
            if cur_job[1] == cur_job_time:
                stage_flag = False
                cur_job_time = 0
                answer.append(global_time - cur_job[0])
                if len(heap) == 0 and job_idx >= len(jobs):
                    break
    return int(sum(answer)/len(answer))
