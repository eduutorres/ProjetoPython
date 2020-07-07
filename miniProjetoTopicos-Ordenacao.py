import random


class Sort:
    def __init__(self, listaN):
        self.listaN = listaN

    # Inicia BubbleSort GRUPO #01

    def bubblesort(self, listaN):
        for final in range(len(listaN), 0, -1):
            controlador = False

            for atual in range(0, final - 1):
                if listaN[atual] > listaN[atual + 1]:
                    listaN[atual + 1], listaN[atual] = listaN[atual], listaN[atual + 1]
                    controlador = True

            if not controlador:
                break

    # Inicia QuickSort GRUPO #02

    def quicksort(self, listaN, inicial, final):
        if inicial < final:
            posicaoF = self.particionar(listaN, inicial, final)
            self.quicksort(listaN, inicial, posicaoF - 1)
            self.quicksort(listaN, posicaoF + 1, final)

    def particionar(self, listaN, inicial, final):
        pivo = listaN[inicial]
        i = inicial
        j = inicial + 1

        while j <= final:
            if listaN[j] < pivo:
                i += 1
                self.trocar(listaN, i, j)
            j += 1
        self.trocar(listaN, inicial, i)
        return i

    def trocar(self, listaN, n, m):
        temp = listaN[n]
        listaN[n] = listaN[m]
        listaN[m] = temp

    # Inicia MergeSort GRUPO #02

    def mergesort(self, listaN):
        if len(listaN) > 1:
            meio = len(listaN) // 2
            metadeE = listaN[:meio]
            metadeD = listaN[meio:]

            self.mergesort(metadeE)
            self.mergesort(metadeD)

            i = 0
            j = 0
            k = 0
            while i < len(metadeE) and j < len(metadeD):
                if metadeE[i] < metadeD[j]:
                    listaN[k] = metadeE[i]
                    i = i + 1
                else:
                    listaN[k] = metadeD[j]
                    j = j + 1
                k = k + 1

            while i < len(metadeE):
                listaN[k] = metadeE[i]
                i = i + 1
                k = k + 1

            while j < len(metadeD):
                listaN[k] = metadeD[j]
                j = j + 1
                k = k + 1

    # Inicia ShellSort GRUPO #03

    def shellsort(self, listaN):
        subLista = len(listaN) // 2
        while subLista > 0:

            for startposition in range(subLista):
                self.gapInsertionSort(listaN, startposition, subLista)

            subLista = subLista // 2

    def gapInsertionSort(self, listaN, inicial, gap):
        for i in range(inicial + gap, len(listaN), gap):

            atual = listaN[i]
            posicao = i

            while posicao >= gap and listaN[posicao - gap] > atual:
                listaN[posicao] = listaN[posicao - gap]
                posicao = posicao - gap

            listaN[posicao] = atual

    # Inicia RadixSort GRUPO #03

    def countingsort(self, listaN, local):
        tamanho = len(listaN)
        resultado = [0] * tamanho
        contador = [0] * 10
        for i in range(0, tamanho):
            inicio = listaN[i] // local
            contador[inicio % 10] += 1
        for i in range(1, 10):
            contador[i] += contador[i - 1]
        i = tamanho - 1
        while i >= 0:
            inicio = listaN[i] // local
            resultado[contador[inicio % 10] - 1] = listaN[i]
            contador[inicio % 10] -= 1
            i -= 1
        for i in range(0, tamanho):
            listaN[i] = resultado[i]

    def radixsort(self, listaN):
        elementoMx = max(listaN)
        local = 1
        while elementoMx // local > 0:
            self.countingsort(listaN, local)
            local *= 10


# Lista randomica automática
listaV = list(range(0, 20))
random.shuffle(listaV)

# Lista randomica editável
# listaV = [57, 23, 92, 19, 75, 34, 49, 56, 26]

print('====================================================== ')
print('Lista Embaralhada: ')
print(listaV)
print('====================================================== ')
bubbleSort = Sort(listaV)
bubbleSort.bubblesort(listaV)
print('====================================================== ')
print('Lista Ordenada por BubbleSort: ')
print(bubbleSort.listaN)
print('====================================================== ')
quickSort = Sort(listaV)
quickSort.quicksort(listaV, 0, len(listaV) - 1)
print('====================================================== ')
print('Lista Ordenada por QuickSort')
print(quickSort.listaN)
print('====================================================== ')
mergeSort = Sort(listaV)
mergeSort.mergesort(listaV)
print('====================================================== ')
print('Lista Ordenada por MergeSort')
print(mergeSort.listaN)
print('====================================================== ')
shellSort = Sort(listaV)
shellSort.shellsort(listaV)
print('====================================================== ')
print('Lista Ordenada por ShellSort')
print(shellSort.listaN)
print('====================================================== ')
radixSort = Sort(listaV)
radixSort.radixsort(listaV)
print('====================================================== ')
print('Lista Ordenada por RadixSort')
print(radixSort.listaN)
print('====================================================== ')

# @luiztORRES.
