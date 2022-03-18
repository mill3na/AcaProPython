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
# from multiline_strings import imprime_guia_do_usuario
        
# for resultado in search ('"dean lewis" google', stop=5):
#     print (resultado)


menu_principal = ["Guia do usuário", "Informações sobre o processo de desenvolvimento", "Buscar referências", "Formatar referência", "Formatar referência e salvar automaticamente", "Exibir fontes confiáveis para pesquisa acadêmica", "Sair"]

def exibe_menu(menu):
    
    for index, opcao in enumerate(menu):
        print(f"[{index + 1}] {opcao}.")

def seleciona_opcao_menu_principal(menu):
    continue_loop = True
    
    while(continue_loop):
        exibe_menu(menu)
        try:
            opcao_menu = int(input("Digite a sua opção: "))
            if opcao_menu == len(menu):
                    print("\nSaindo do sistema. Até logo!\n\n")
                    break
            
            elif (int(opcao_menu) > len(menu) or int(opcao_menu) <= 0):
                print("\nOpção inválida! Tente novamente.\n\n")
            
            else:
                print(f"Opção escolhida: {menu[opcao_menu]}")
                if opcao_menu == 1:
                    imprime_guia_do_usuario(guia_do_usuario_completo)
                elif opcao_menu == 2:
                    print("Informações sobre o processo de desenvolvimento")
                elif opcao_menu == 3:
                    print("Buscar referências")
                elif opcao_menu == 4:
                    print("Formatar referência")
                elif opcao_menu == 5:
                    print("Formatar referência e salvar automaticamente")
                else:
                    print("Exibir fontes confiáveis para pesquisa acadêmica")
                    
        except ValueError:
            print("\nVocê digitou algo no formato errado. Por favor, tente novamente, digitando números inteiros.\n\n")
            break
        except:
            print(Exception)
            
seleciona_opcao_menu_principal(menu_principal)