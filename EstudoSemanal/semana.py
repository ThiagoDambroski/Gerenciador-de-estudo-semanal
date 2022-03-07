from defs import *
pag = ("banco de horas.txt","r")
horas_semanais = 24
arquivo_dados = "banco de horas.txt"
arquivo_semana = "semanas.txt"
arquivo_horas = "horas diarias.txt"


while True:

    linhas()
    x = int(input("opção 1 - registrar horas\nopção 2 - quantas horas domingo\nopçao 3 - finalizar semana "
                  "\nopção 4 - Horas diarias\nopção 5 - convertor de horas decimais\n"
                  "Opção 6 - vizualizar\nopção 7 - sair\nDigite a opção: "))

    if x == 1:
        print("1 - segunda\n2 - terça\n3 - quarta\n4 - quinta\n5 - sexta\n6 - sab\n7 - domingo")
        y = int(input("digite a opção: "))
        if y <= 7 and y > 0:
            adicionando(y,arquivo_dados)


    if x == 2:
        resultado = soma_horas_semanais(arquivo_dados)
        print(f"Faltam {horas_semanais - resultado} horas para serem estudadas")


    if x == 3:
        registrar_semana(arquivo_dados)

    if x == 4:
        horas_diarias(arquivo_horas)

    if x == 5:
        convertendo_horas(input("digite a quantidade de horas: "))

    if x == 6:
        linhas()
        ver = int(input("1 - arquivo semanal\n2 - arquivos das semanas\nDigite sua opção: "))
        if ver == 1:
            mostrar_semana(arquivo_dados)
        elif ver == 2:
            mostrar_semana(arquivo_semana)
            print(f"DEVENDO {devendo(arquivo_semana)} HORAS")

    if x == 7:
        break







