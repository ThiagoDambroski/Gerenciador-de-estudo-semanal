def linhas():
    print("-=" * 25)

def convertendo_horas(x):
    loucura = str(float(x))
    loucura.split()
    horas = ""
    min = ""
    achou = False
    for c in loucura:
        if c == ".":
            achou = True
        if achou and c != ".":
            min += c
        elif achou == False and c != ".":
            horas += c


    print(f"{horas} horas e {int(min) * 0.6} minutos")

def mostrar_semana(x):
    pag = open(f"{x}", "r")
    linhas()
    print(pag.read())
    pag.close()

def devendo(x):
    pag = open(f"{x}", "r+")
    b = pag.readlines()
    soma = 0
    for c in b:
        z = c.split()
        soma += float(z[3])
    return soma

def adicionando(opcao,local):
    print("Quantas horas hoje ?")
    horas = float(input("digite aqui: "))
    pag = open(f"{local}", "r+")
    b = pag.read()
    b = b.replace(f"placeholder{opcao}", f" eita {horas}")
    pag.close()
    pag = open(f"{local}", "r+")
    pag.write(b)
    pag.close()

def soma_horas_semanais(x):
    pag = open(f"{x}", "r")
    b = pag.readlines()
    soma = 0
    for c in b:
        if "eita" in c:
            z = c.split()
            soma += float(z[3])
    pag.close()
    return soma

def registrar_semana(x):
    pag = open(f"{x}", "r+")
    b = pag.readlines()
    soma = 0
    correto = 0
    for c in b:
        if "eita" in c:
            z = c.split()
            soma += float(z[3])
            correto += 1
    pag.close()
    if correto == 7:
        pag2 = open(f"{arquivo_semana}", "r+")
        z = pag2.readlines()
        contador = 0
        for c in z:
            contador += 1
        pag2.write(f"semana {contador} = {(horas_semanais - soma)}\n")
        pag2.close()
        pag = open(f"{x}", "w")
        pag.write("segunda = placeholder1\nterça = placeholder2\nquarta = placeholder3\nquinta = placeholder4\n"
                  "sexta = placeholder5\nsab = placeholder6\ndomingo = placeholder7 ")
        pag.close()
    else:
        print("Registrar todos os 7 dias da semana antes de finalizar")

def horas_diarias(x):
    pag = open(f"{x}", "r+")
    b = pag.readlines()
    soma = 0
    for c in b:
        soma += float(c)
    pag.close()
    print(f"Foram estudas {soma / 60:.2f} horas hoje")
    linhas()
    print("opção 1 - adicionar horas")
    print("opção 2 - resetar horas")
    z = int(input("Digite a sua opção: "))
    if z == 1:
        linhas()
        pag = open(f"{x}", "a")
        horas = int(input("Digite a quantidade de horas: "))
        minutos = int(input("Digite a quantidade de minutos:"))
        pag.write(f"{(horas * 60) + minutos}")
        print("Adicionado com sucesso")
        linhas()
        pag.close()
    elif z == 2:
        certeza = str(input("Tem certeza? "))
        if certeza.lower().strip() == "sim" or certeza.lower() == "s":
            pag = open("", "w")
            pag.write("0")
            print("resetada com sucesso")
            linhas()