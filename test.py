''' função responsável pela representação dos produtos nos elementos da matriz '''

def produto(x, y):
    if(x == '0' or y == '0'):
        return '0'
    if(x == '1'):
        return y
    if(y == '1'):
        return x
    if('+' in y):
        strng = '+' + x
        strng = strng.join(y.split('+'))
        return x + strng

    return x + y


''' função responsável pela representação da soma em cada elemento da matriz '''

def soma(x, y):
    if(x == '0'):
        return y
    if(y == '0'):
        return x

    return x + '+' + y


''' função que realiza uma multiplicação de matrizes '''

def solucao(A, B, n, itr):
    i, j, k = [0, 0, 0]
    vet = []
    Linhas = []
    for x in range(n):  # conta o número de vértices e enumera alfabeticamente
        vet.append(chr(x + 97))
    while(i < n):
        Colunas = []
        while(j < n):
            somatorio = '0'
            while(k < n):
                # os elementos das matrizes recebidas são multiplicados
                p = produto(B[i][k], A[k][j])
                # e somados, resultando no elemento da matriz saída
                somatorio = soma(somatorio, p)
                k += 1
            k = 0
            somatorio = verificar(somatorio, vet[i], vet[j], itr)
            Colunas.append(somatorio)
            j += 1
        j = 0
        Linhas.append(Colunas)
        i += 1

    return Linhas


''' iterações do algoritmo '''

def aplicacao(A, B, n):
    itr = 1
    Result = solucao(A, B, n, itr)
    itr += 1
    for i in range(n-3):
        Result = solucao(Result, B, n, itr)
        itr += 1

    return Result


''' elimina caminhos que não fazem parte '''

def verificar(strng, vet, vt, n): #se o vértice inicial ou final estiver no caminho, fazer o eleemento = '0'
    if(vet == vt):
        return '0'
    aux = strng.split('+')
    novo = ''
    for i in range(len(aux)):
        if(not(vet in aux[i] or vt in aux[i] or len(aux[i]) != n)):
            novo += aux[i]
            if(i < len(aux)-1):
                novo += '+'
    if(novo == ''):
        return '0'
    return novo


''' correções '''

def organizar(M, n, adj): #trata de alguns erros lógicos da aolicação
    for i in range(n):
        for j in range(n):
            if(adj[i][j] == '0' and adj[j][i] == '0'):
                M[i][j] = '0'
            else:
                if(M[i][j] != '0'):
                    strng = M[i][j].split('+')
                    M[i][j] = strng[0]
                    for k in range(len(strng)-1):
                        if(len(strng[k+1]) == n-2):
                            M[i][j] = soma(M[i][j], strng[k+1])

    return M


# é preciso receber duas matrizes que descrevem a conectividade do grafo
grafo = open('grafo3/grafo3.txt', 'r')
adj = open('grafo3/adjacencia.txt', 'r')
texto = []
matriz = []
mtrzAdj = []
texto = grafo.readlines()

for i in range(len(texto)):
    matriz.append(texto[i].split())

for i in range(len(texto)):
    print(matriz[i])
print("")

texto = adj.readlines()

for i in range(len(texto)):
    mtrzAdj.append(texto[i].split())

for i in range(len(texto)):
    print(mtrzAdj[i])
print("")

result = aplicacao(mtrzAdj, matriz, len(texto))  # aplicação do algoritmo
result = organizar(result, len(result), mtrzAdj)
print("resultado:")
for i in range(len(texto)):  # exibição do rresultado
    print(result[i])
print("")

adj.close()
grafo.close()
