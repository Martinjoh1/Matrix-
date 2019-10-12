#recieved help from: 
#
#
#
#
#
#
#
#
#
#
#
#
#
def makeMatrix():
    m1 = [  [1,2,3],
            [4,5,6],
            [7,8,9]]
    
    m2 = [  [1,2,3],
            [4,5,6],
            [7,8,9]]
    print('Matrix 1 =',m1)
    print ('Matrix 2 =',m2)
    return(m1,m2)

def get_col(m1,m2,j):
    col = [row[j] for row in m1]
    col2 = [row[j] for row in m2]
    numcol = len(m1[j])
    numcol2 = len(m2[j])
    print('Matrix 1 collumn complete=',col)
    print('Matrix 2 collumn complete=',col2)
    print('Matrix 1 collumn=',numcol)
    print('Matrix 2 collumn=',numcol2)
    return(col,col2,numcol,numcol2)

def get_row(m1,m2,j):
    rowm1=[]
    rowm2=[]
    rowm1.append(m1[j])
    print("row of m1 =",rowm1)
    rowm2.append(m2[j])
    print("row of m2 =",rowm2)
    return(rowm1,rowm2)

def add(m1, m2):
    addition = [    [0,0,0],
                    [0,0,0],
                    [0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            addition[i][j] = m1[i][j] + m2[i][j]
    for a in addition:
        print ("The Adittion of M1 and M2 =", a)
    return (a)

def sub(m1,m2):
    sub = [     [0,0,0],
                [0,0,0],
                [0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            sub[i][j] = m1[i][j] - m2[i][j]
    for s in sub:
        print ("The Subtraction of M1 and M2 =", s)
    return (s)

def mult(m1,m2):
    mult = [    [0,0,0],
                [0,0,0],
                [0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                mult[i][j] += m1[i][k] * m2[k][j]
    for m in mult:
        print ("The multiplication of M1 and M2 =", m)
    return (m)

def transpose(m1):
    for trowm1 in m1:
        rezm1 = [[m1[j][i]for j in range (len(m1))] for i in range(len(m1[0]))]
    for trowm1 in  rezm1: 
        print("This is m1 transposed =", rezm1)
        return(rezm1)

#def dot(m1,m2):
#    if len(m1) != len(m2):
#       return(0)
#    dotsum = sum(i[0] * i[1] for i in zip (m1,m2))
#    print("This is the dotproduct =", dotsum)
#    return (dotsum)




def main():
    m1,m2 = makeMatrix()
    col,col2,numcol,numcol2= get_col(m1,m2,1)
    rowm1,rowm2= get_row(m1,m2,0)
    a = add(m1,m2)
    s = sub(m1,m2)
    m = mult(m1,m2)
    rezm1 = transpose(m1)
#    dotsum = dot(m1,m2)


if __name__ == "__main__":
    main()