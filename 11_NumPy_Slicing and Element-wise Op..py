import numpy as np

def sum_2_rows(M):
    return M[::2,:] +M[1::2,:]

def sum_left_right(M):
    n = M.shape[1]
    return M[:,:n//2] + M[:, n//2:]

def sum_upper_lower(M):
    n = M.shape[0]
    return M[:n//2,:] + M[n//2:,:]

def sum_4_quadrants(M):
    return sum_left_right(sum_upper_lower(M))

def sum_4_cells(M):
    return M[::2,::2] + M[::2,1::2] + M[1::2,::2] + M[1::2, 1::2]

def count_leap_years(years):
    years-=543
    return np.sum((years%400==0) | ((years%4==0) & (years%100!=0)))
    
exec(input().strip())