def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    M = []
    for row in A:
        M.append([c*e for e in row])
    return M

def mult(A, B):
    M = [[0]*len(B[0]) for k in range(len(A))] #rows of A x columns of B
    for i in range(len(A)):
        for j in range(len(B[0])):
            M[i][j] = 0
            for k in range(len(A[0])):
                M[i][j] += A[i][k]*B[k][j]
    return M

exec(input().strip())