import timeit

def mochilaFracionaria(n, weights, values, capacity):
    ratio = [values[i] / weights[i] if weights[i] > 0 else 0 for i in range(n)] #Lista criada para armazenar a razao entre os valores
    #e os pesos dos itens
    totalValue = 0.0

    while capacity > 0: #Laço para buscar os itens da mochila até que a capacidade atinja o limite
        #Variáveis auxiliares para buscar o melhor item da mochila. São iniciadas em -1 para indicar nenhum valor na mochila
        bestItem = -1
        bestRatio = -1.0

        for i in range(n): #Laço para adicionar os items na mochila e atualizar as variáveis auxiliares
            if weights[i] > 0 and ratio[i] > bestRatio: #Verifica se o item ainda não foi colocado na mochila
                #e se foi a melhor razão encontrada até o momento
                #Se for verdadeiro insere o valor atualizado do item do índice "i" nas variáveis
                bestRatio = ratio[i]
                bestItem = i

        if bestItem == -1: #Verifica se o melhor item não foi encontrado
            #Se for verdadeiro a função mochila_fracionaria termina e retorna o valor total encontrado na mochila
            break

        if weights[bestItem] <= capacity: #Verifica se o peso do item é menor ou igual à capacidade restante da mochila
            #Se for verdadeiro adiciona o valor do item no valor total da mochila, atualiza a capacidade restante
            #e modifica o peso do item para 0 para indicar que foi adicionado dentro da mochila
            totalValue += values[bestItem]
            capacity -= weights[bestItem]
            weights[bestItem] = 0
        else:
            #Se não for verdadeiro, significa que o peso do item é maior que a capacidade da mochila 
            #e apenas uma fração do item pode ser adicionado dentro dela
            totalValue += bestRatio * capacity
            capacity = 0 #Atualiza a capacidade para 0 para encerrar o while, pois não é mais possível armazenar valores dentro da mochila

    return totalValue

n = int(input("Insira o número de itens: "))
weights = list(map(int, input("Insira os pesos dos itens: ").split()))
values = list(map(int, input("Insira os valores dos itens: ").split()))
capacity = int(input("Insira a capacidade da mochila: "))

print(f"Valor máximo da mochila: {mochilaFracionaria(n, weights, values, capacity):.2f}")
averageTime = timeit.timeit(lambda: mochilaFracionaria(n, weights, values, capacity), number = 1000)
print(f"Tempo de execução do código foi de {averageTime:.6f} segundos")
