tupla1 = tuple(range(10))
print(tupla1)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
i = 0
while i < len(meses):
    print(meses[i])
    i += 1
