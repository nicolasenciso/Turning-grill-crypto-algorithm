import copy

def buildMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append("")
    return matrix

def cipher(msg, matrix, n, direction, holes):
    count = len(holes)
    finalOut = ""
    auxCount = 0
    msg = msg.replace(" ","")
    msg = msg.upper()
    matHoles = copy.deepcopy(matrix)
    for hole in holes:
        matHoles[hole[0]][hole[1]] = 1
    if (direction == 1): #to the left
        while(count<=len(msg)):
            msgAux = msg[auxCount:count]
            holesAux = []
            for i in range(n):
                for j in range(n):
                    if matHoles[i][j] == 1:
                        holesAux.append((i,j))
            for k in range(len(msgAux)):
                matrix[holesAux[k][0]][holesAux[k][1]] = msgAux[k]
            rotationLeft(matHoles)
            auxCount = count
            count = count +len(holes)
        for i in range(n):
            for j in range(n):
                finalOut = finalOut + str(matrix[i][j])
    elif(direction == 0): #to the right
        while(count<=len(msg)):
            msgAux = msg[auxCount:count]
            holesAux = []
            for i in range(n):
                for j in range(n):
                    if matHoles[i][j] == 1:
                        holesAux.append((i,j))
            for k in range(len(msgAux)):
                matrix[holesAux[k][0]][holesAux[k][1]] = msgAux[k]
            rotationLeft(matHoles)
            rotationLeft(matHoles) #3 times left = 1 right
            rotationLeft(matHoles)
            auxCount = count
            count = count + len(holes)
        for i in range(n):
            for j in range(n):
                finalOut = finalOut + str(matrix[i][j])
    return finalOut

def decipher(msg, matrix, n, direction, holes):
    finalOut = ""
    msg = msg.replace(" ","")
    msg = msg.upper()
    matHoles = copy.deepcopy(matrix)
    for hole in holes:
        matHoles[hole[0]][hole[1]] = 1
    var = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = msg[var]
            var = var + 1
    if (direction == 1): #to the left
        for k in range(len(msg)):
            for i in range(n):
                for j in range(n):
                    if matHoles[i][j] == 1:
                        finalOut = finalOut + matrix[i][j]
            rotationLeft(matHoles)
        finalOut = finalOut[0:len(msg)]
    elif (direction == 0): #to the right
        for k in range(len(msg)):
            for i in range(n):
                for j in range(n):
                    if matHoles[i][j] == 1:
                        finalOut = finalOut + matrix[i][j]
            rotationLeft(matHoles)
            rotationLeft(matHoles)
            rotationLeft(matHoles)
        finalOut = finalOut[0:len(msg)]
        last = finalOut[n:2*n]
        second = finalOut[3*n:len(msg)]
        first = finalOut[0:n]
        third = finalOut[2*n:3*n]
        finalOut = first+second+third+last
        
    print(finalOut)


def rotationLeft(matrix):
    size = len(matrix)
    for x in range(0, int(n/2)):
        for y in range(x, n-x-1):
            temp = copy.deepcopy(matrix[x][y])
            matrix[x][y] = copy.deepcopy(matrix[y][n-1-x])
            matrix[y][n-1-x] = copy.deepcopy(matrix[n-1-x][n-1-y])
            matrix[n-1-x][n-1-y] = copy.deepcopy(matrix[n-1-y][x])
            matrix[n-1-y][x] = copy.deepcopy(temp)
    return matrix


n = 4
print("> Tamanio matriz")
print(n)
print("> Hoyos")
holes = [(0,0),(2,1),(2,3),(3,2)]
print(holes)
print("> Mensaje a cifrar: ")
msg2 = "BOMBS AT TRENCH TWO"
print(msg2)
print("> Mensaje a descifrar")
msg = "BRHSEANTTOWMOTBC"
print(msg)

# PARAMETROS: MENSAJE, TAMANO MATRIZ, DIRECCION (O=DERECHA, 1=IZQUIERDA), HOYOS
s = buildMatrix(n)
print("> Cifrado por derecha:")
print(cipher(msg2,s,n,0,holes))#right
print("> Cifrado por izquierda:")
print(cipher(msg2,s,n,1,holes))#left
print("> Descifrado por derecha:")
decipher(msg,s,n,0,holes)#right
print("> Descifrado por izquierda")
decipher(msg,s,n,1,holes)#left
print("")
print("")
print("-----------------------------------------------------")
print("> Descrifrado ejercicio slides:")
print("> Tamanio matriz")
n = 9
print(n)
print("> Hoyos")
holes = [(0,0),(0,3),(0,5),(1,2),(1,8),(2,1),(2,6), (3,2), (3,4), (3,7), (4,4), (4,6), (4,8), (5,3), (5,7), (6,0),
        (6,5), (7,1), (7,4), (7,8), (8,2) ]
print(holes)
print("> Mensaje de descifrar")
msg = "TESHNINCIGLSRGYLRIUSPITSATLILMREENSATTOGSIAWGIPVERTOTEHHVAEAXITDTUAIMERANPMTLHIEE"
print(msg)
matrix = buildMatrix(n)
print("> Mensaje descifrado")
decipher(msg,matrix,n,0,holes)



