'''
Written by Yusuf Patoglu
25.09.2021

Reads showg's output as adjacency form and converts it to adjacency list form that is acceptable by fmc package.

'''
import sys
fileName = sys.argv[-2]
inputFile = open(fileName, 'r')
fileName = sys.argv[-1]
outputFile = open(fileName, 'w')

#Read from showg's output and create the adjacency matrix graph.
def initMatrix(filePointer):
    matrix = []
    row = []
    while 1:
         
        # read by character
        char = filePointer.read(1)
        if char == '\n':
            matrix.append(row)
            row = []
        elif char != ' ':
            row.append(char)
        if not char:
            break
       
    filePointer.close()
    return matrix

#Convert from adjacency
def printAdjacencyListToFile(theMatrix, filePointer):

    
    
    redEdgeCount = 0 #Red edges are 1.
    #print("%%MatrixMarket matrix coordinate pattern symmetric")
    n = len(theMatrix)
    for i in range (0, n):
        for j in range(0, i + 1):
            if theMatrix[i][j] == '0':
                print(i + 1, j + 1, file = filePointer)
                redEdgeCount += 1

    
    
    
    
    tempFilePointer = open("temp", 'w+')
    print("%%MatrixMarket matrix coordinate pattern symmetric", file = tempFilePointer)
    print(n, n, redEdgeCount, file = tempFilePointer)
    filenames = [tempFilePointer.name, filePointer.name]
    filePointer.close()
    tempFilePointer.close()

    with open('original.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())
                
 
        
    
matrix = initMatrix(inputFile)
print(matrix)
printAdjacencyListToFile(matrix, outputFile)

