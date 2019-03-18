import os

gravity = {
    "lua": 1.62,
    "terra": 10,
    "marte": 3.711,
    "europa": 1.315
}

def main():
    print("""
###################################
# Informações relevantes a seguir #
###################################

Muitas das vezes costumamos usar a palavra "peso" para descrever
a nossa massa corporal. Se tornou um costume, e então usamos essa
expressão até os dias de hoje. Na realidade, o peso é a força exercida
sobre um corpo ou matéria pela gravidade, ficamos com o pé no chão pelo
simples motivo que a gravidade nos empurra para baixo nos mantendo na superficie,
isso é peso.

Já a massa é a quantidade matéria presente em um corpo. Por exemplo, medimos
nosso "peso" em uma balança, este "peso" na realidade, é a nossa massa!
conforme a gravidade, podemos nos sentir mais pesados ou mais leves
pelo motivo citado anteriormente. A força da gravidade pode tanto nos "pressionar"
como nos dar a sensação de estarmos mais "leves".

Então a nossa massa pode "variar" de gravidade em gravidade pela força
exercida em nossos corpos, e existe uma fórmula para isso
criada por Isaac Newton que diz o seguinte:
    p = m.g
Lembrando que a nossa massa não pode ser alterada, e sim é uma questão
da força exercida em nossos corpos, causado pela gravidade que nos faz
a sensação de estarmos mais leves, ou mais pesados.

--------------------------------------------------------------------------

Desenvolvido por @sadstan www.github.com/sadstan

    """)
    inp = input("Digite o nome do planeta ou lua: ").lower().strip()

    if inp == "lua":
        digite_massa(inp)
    elif inp == "terra":
        digite_massa(inp)
    elif inp == "marte":
        digite_massa(inp)
    elif inp == "europa":
        digite_massa(inp)
    else:
        print("Opção incorreta!")
        main()

def digite_massa(planet):
    massa = float(input("Digite a sua massa: "))
    calculo(planet,gravity[planet], massa)
    voltar()

def calculo(planeta,gravidade,massa):
    print("A sua massa no planeta {} em newtons é igual a {:.2f} newtons!".format(planeta, gravidade * massa))

def voltar():
    escolha = input("Deseja reiniciar o programa? ").lower()
    if escolha == "s":
        os.system('clear' or 'cls')
        main()
    else:
        exit()

main()