import numpy as np
import math

def solution(answers):
    length = len(answers)
    a = np.array([1,2,3,4,5])
    b = np.array([2,1,2,3,2,4,2,5])
    c = np.array([3,3,1,1,2,2,4,4,5,5])
    
    a = np.tile(a, math.ceil(length/5))[:length]
    b = np.tile(b, math.ceil(length/8))[:length]
    c = np.tile(c, math.ceil(length/10))[:length]
    
    answer = [np.where(a==answers)[0].shape[0], np.where(b==answers)[0].shape[0], np.where(c==answers)[0].shape[0]]
    max_ = np.max(answer)
    s_list = []
    for i, a in enumerate(answer):
        if a == max_: s_list.append(i+1)
    return s_list