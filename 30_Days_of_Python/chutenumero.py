import random

jogar_novamente = input("Digite 'S' para começar. ").upper()

while jogar_novamente == "S":
    num = random.randint(1, 101)
    print(f"{'#' * 46}\nDescubra o número!")
    tentativa = 1
    chute_errado = True
    
    while chute_errado:
        chute = int(input("Digite um número inteiro de 1 a 100 (ou 999 para sair): "))
        if not isinstance(chute, int):
            print("Entrada inválida! Não é um número inteiro.")
            continue
        if chute == 999:
            jogar_novamente = "N"
            break
        elif chute not in range(1, 101):
            print("Entrada inválida! O número está fora do intervalo [1, 100]")
            continue
        elif chute == num:
            print(f"Parabéns! O número é: {num}\nTentativas: {tentativa}")
            chute_errado = False
            jogar_novamente = input("Digite 'S' caso deseje jogar novamente. ").upper()
            break
        else:
            mensagem = "cima" if chute < num else "baixo"
            print(f"Número errado. Chute mais pra {mensagem}.\nTentativas: {tentativa}\n")
            tentativa += 1
else:
    print("FIM! Até mais, jogador!")
