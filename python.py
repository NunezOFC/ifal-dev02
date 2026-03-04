#Questão 7
def seven():
    y = "0"
    z = 0

    y = bool(y)
    z = bool(z)
    print(y)
    print(z)


#Questão 8
def eight():
    x = "5.67"

    x = float(x)
    print(x)

    x2 = "5.67"

    x2 = int(x2)
    print(x2)

#Questão 9
def nine():
    try:
        n1 = float(input("Insira a Primeira Nota: ").replace(',','.'))
        n2 = float(input("Insira a Segunda Nota: ").replace(',','.'))
        n3 = float(input("Insira a Terceira Nota: ").replace(',','.'))
        n4 = float(input("Insira a Quarta Nota: ".replace(',','.')))
    except ValueError as erro:
        print("Apenas números \n""Pode ser com virugla/Ponto")
        nine()
    media = (n1+n2+n3+n4)/4
    print(f"Sua média é {media}")
    choice


#Escolha de questões porque sim
def choice():
    question = int(input("Qual questão fazer código: "))
    
    
    if question == 7:
        seven()
    elif question == 8:
        eight()
    elif question == 9:
        nine()

choice()