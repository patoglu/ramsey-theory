import sys
fileName = sys.argv[-1]
file = open(fileName, 'r')
 

 
def initMatrix(theFile):
    matrix = []
    row = []
    while 1:
         
        # read by character
        char = file.read(1)
        if char == '\n':
            matrix.append(row)
            row = []
        elif char != ' ':
            row.append(char)
        if not char:
            break
       
    file.close()
    return matrix

def getAdjacencyList(theMatrix):
    n = len(theMatrix)
    for i in range (0, n):
        for j in range(0, i + 1):
            #print(theMatrix[i][j] , end='')
            if theMatrix[i][j] == '1':
                print(i + 1, " - ", j + 1)
            
        print("")


matrix = initMatrix(file)
print(matrix)
getAdjacencyList(matrix)

