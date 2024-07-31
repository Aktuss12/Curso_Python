conjunto = set({1, 2, 2, 3, 1, 4, 5, 4, 6, 3, 7})
print(conjunto)
print(type(conjunto))

conjunto2 = {1, 'b', False, '155', 986}
print(conjunto2)

for valor in conjunto2:
    print(valor)

conjuntoteste = set({'Jales', 'Florianópolis', 'Camboriu', 'Rio Preto'})
print(conjuntoteste)

for valor2 in conjuntoteste:
    print(valor2)

conjunto3 = {'Olá', 12, True}
print(conjunto3)

conjunto.add('Hello World')
print(conjunto)
