usuario_ativo = True
usuario_cadastrado = True

if usuario_cadastrado and usuario_ativo:
    print("Usuario cadastrado!")
else:
    print("Usuario não cadastrado.")

print("\n")

produto_exibicao = False
produto_estoque = True

if produto_exibicao or produto_estoque:
    print("Produto disponível para venda!")
else:
    print("Produto indisponível no momento.")