# Milena Maia, 09/03/2022.

# AcaPro: um programa em linha de comando para quem desenvolve produções acadêmicas. As opções de uso incluem:

# 1. Formatar referências para diferentes fontes (com salvamento automático)
# 2. Buscar eixos de pesquisa
# 3. Fontes confiáveis para pesquisa
# 4. Bloco de notas

# E muito mais. Consulte as informações de uso ao longo da execução. :)

import imp
from multiline_strings import *
from googlesearch import search
from time import sleep

        
# for resultado in search ('"dean lewis" google', stop=5):
#     print (resultado)


menu_principal = ["Guia do usuário", "Informações sobre o processo de desenvolvimento", "Buscar referências", "Formatar referência", "Formatar referência e salvar automaticamente", "Exibir fontes confiáveis para pesquisa acadêmica", "Sair"]


def chamada_funcoes_menu(opcao_menu):
    if opcao_menu == "Guia do usuário":
        guia_do_usuário()
    elif opcao_menu == "Informações sobre o processo de desenvolvimento":
        print("Aqui.")

def exibe_menu(menu):
    
    for index, opcao in enumerate(menu):
        print(f"[{index + 1}] {opcao}.")
    
    continue_loop = True
    
    while(continue_loop):
        try: 
            opcao_menu = int(input("Digite a sua opção: "))
            if opcao_menu == len(menu):
                print("Saindo do sistema. Até logo!")
           
            elif (int(opcao_menu) > len(menu) or int(opcao_menu) <= 0):
                print("Opção inválida! Tente novamente.")
           
            else:
                print(f"Opção escolhida: {menu[opcao_menu]}")
                opcao_menu -= 1
                chamada_funcoes_menu(menu[opcao_menu])                    
                continue_loop = False
                
        except ValueError:
            print("Você digitou algo no formato errado. Por favor, tente novamente, digitando números inteiros.")
            break
        except:
            print(Exception)
                
                


        
        
def guia_do_usuário():
    print(aca_pro)
    sleep(2)
    print(bem_vindo)
    print(primeiros_passos)
    sleep(2)
    print(inf_processo_desenvolvimento1)
    sleep(2)


    
exibe_menu(menu_principal)

    