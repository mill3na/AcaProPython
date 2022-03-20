import imp
from pandas import array

from pyrsistent import T

from multiline_strings import *
from time import sleep

menu_principal = ["Guia do usuário", "Informações sobre o processo de desenvolvimento", "Buscar referências", "Formatar referência", "Formatar referência e salvar automaticamente", "Exibir fontes confiáveis para pesquisa acadêmica", "Sair"]

menu_referencias = ["Livro", "Revistas ou periódicos", "Artigos em eventos", "Websites", "Monografias, dissertações ou teses", "Voltar"]

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
                print(f"\nOpção escolhida: {menu[opcao_menu]}")
                if opcao_menu == 1:
                    inprime_multiline_string(guia_do_usuario_completo)
                elif opcao_menu == 2:
                    print("Informações sobre o processo de desenvolvimento")
                    inprime_multiline_string(processo_de_desenvolvimento)
                elif opcao_menu == 3:
                    print("Buscar referências")
                elif opcao_menu == 4:
                    print("Formatar referência")
                    formatar_referencias(menu_referencias)
                    print(formatar_referencias)
                elif opcao_menu == 5:
                    print("Formatar referência e salvar automaticamente")
                elif opcao_menu == 6:
                    print("Exibir fontes confiáveis para pesquisa acadêmica")
                    
        except ValueError:
            print("\nVocê digitou algo no formato errado. Por favor, tente novamente, digitando números inteiros.\n\n")
            
        except:
            print(Exception)
 
def inprime_multiline_string (multiline_string, first_element=0):
    for opcao in range(first_element, len(multiline_string)):
        print(opcao)
        sleep(1)
        continua = input("Continuar? [S/N]  ")
        if continua.upper() == "N":
            print("Saindo da seção. Até mais!")
            sleep(1)
            break

def formatar_referencias(menu):
    continua_loop = True
    formatacao = ""
    while(continua_loop):
        exibe_menu(menu)
        try:
            opcao_menu = int(input("Digite a sua opção: "))
            if opcao_menu == len(menu):
                    print("Voltando ao menu principal...")
                    sleep(1)
            
            elif (int(opcao_menu) > len(menu) or int(opcao_menu) <= 0):
                print("\nOpção inválida! Tente novamente.\n\n")
            
            else:
                print(f"\nOpção escolhida: {menu[opcao_menu]}")
                if opcao_menu == 1:
                    print("Livro")
                    formatacao = quantidade_de_autores()
                    print(formatacao)
                elif opcao_menu == 2:
                    print("Revistas ou periódicos")
                    formatacao = revistasOuPeriodicos()
                    print(formatacao)
                elif opcao_menu == 3:
                    print("Artigos em eventos")
                    formatacao = artigo_em_evento()
                    print(formatacao)
                elif opcao_menu == 4:
                    print("Websites")
                else:
                    print("Monografias, dissertações ou teses")
                    formatacao = monografia_dissertacao_tese()
                    print(formatacao)
        except ValueError:
            print("\nVocê digitou algo no formato errado. Por favor, tente novamente, digitando números inteiros.\n\n")
            
        except:
            print(Exception)
            
def nome_e_sobrenome():
    nome = input("Digite o nome do autor: ")
    sobrenome = input("Digite o sobrenome do autor: ")
    return f"{sobrenome.upper()}, {nome.title()}"

def informacoes_basicas_livro():
    tituloDaObra = input("Digite o título do livro: ").title()
    localPublicação = input("Digite o local de publicação: ").title()
    editora = input("Digite a editora: ").title()
    anoPublicação = input("Digite o ano de publicação: ")
    temSubtitulo = input("Esse livro tem subtítulo [S/N]? ")
    temEdicao = input("Essa obra tem edição [S/N]? ")
    
    if (temSubtitulo.upper() == "S") and (temEdicao.upper() == "S"):
        subtituloObra = input("Digite o subtitulo da obra: ").title()
        edicaoObra = input("Digite a edição (somente o número): ")
        return f"{tituloDaObra}: {subtituloObra}. {edicaoObra}. ed. {localPublicação}: {editora}, {anoPublicação}."
    
    
    elif (temSubtitulo.upper() == "S") and (temEdicao.upper() == "N"):
        subtituloObra = input("Digite o subtitulo da obra: ").title()
        return f"{tituloDaObra}: {subtituloObra}. {localPublicação}: {editora}, {anoPublicação}."
    
    
    elif (temSubtitulo.upper() == "N") and (temEdicao.upper() == "S"):
        edicaoObra = input("Digite a edição (somente o número): ")
        return f"{tituloDaObra}. {edicaoObra}. ed. {localPublicação}: {editora}, {anoPublicação}."
    
    
    else:
        return f"{tituloDaObra}. {localPublicação}: {editora}, {anoPublicação}."
    
def quantidade_de_autores():
    formatacao = ""
    quantidade_autores = int(input("Digite a quantidade de autores. Use 0 para autor desconhecido:  "))
    continua_loop = True
    while (continua_loop):
        if quantidade_autores == 0:
            formatacao = livro_autor_desconhecido()
            continua_loop = False
        elif quantidade_autores == 1:
            formatacao = livro_um_autor()
            continua_loop = False
        elif quantidade_autores == 2:
            formatacao = livro_dois_autores
            continua_loop = False
        elif quantidade_autores == 3:
            formatacao = livro_tres_autores
            continua_loop = False
        elif quantidade_autores > 3:
            formatacao = livro_muitos_autores
            continua_loop = False
        else:
            print("\nOpção inválida. Tente novamente. \n\n")
    return formatacao

def livro_um_autor():
    nome_e_sobrenome_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"Referência formatada: \n{nome_e_sobrenome_autor}. {complemento_referencia}" 

def livro_dois_autores():
    print("\nPrimeiro autor\n")
    nome_e_sobrenome_primeiro_autor = nome_e_sobrenome()
    print("\nSegundo autor\n")
    nome_e_sobrenome_segundo_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"Referência formatada: \n{nome_e_sobrenome_primeiro_autor}; {nome_e_sobrenome_segundo_autor}. {complemento_referencia}" 

def livro_tres_autores():
    print("\nPrimeiro autor\n")
    nome_e_sobrenome_primeiro_autor = nome_e_sobrenome()
    print("\nSegundo autor\n")
    nome_e_sobrenome_segundo_autor = nome_e_sobrenome()
    print("\nTerceiro autor\n")
    nome_e_sobrenome_terceiro_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"Referência formatada: \n{nome_e_sobrenome_primeiro_autor}; {nome_e_sobrenome_segundo_autor}; {nome_e_sobrenome_terceiro_autor}. {complemento_referencia}" 

def livro_muitos_autores():
    nome_e_sobrenome_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"Referência formatada: \n{nome_e_sobrenome_autor} et al. {complemento_referencia}"


def livro_autor_desconhecido():
    tituloObra = input("Digite o título do livro: ")
    localPublicação = input("Digite o local de publicação: ")
    editora = input("Digite a editora: ")
    anoPublicação = input("Digite o ano de publicação: ")
        
    return f"Referência formatada: \n {tituloObra.upper()}. {localPublicação}: {editora}, {anoPublicação}."


def informacoes_basicas_revista_periodico():
    titulo_artigo = input("Digite o título do artigo: ").title()
    titulo_revista = input("Digite o título da revista: ").title()
    local_publicacao = input("Digite o local de publicação: ").title()
    numero_volume = int(input("Digite o número do volume: "))
    paginas_inicial_final = input("Digite as páginas inicial e final <x - y>: ")
    ano_publicacao = int(input("Digite o ano de publicação: "))
    
    tem_mes_publicacao = input("Você tem acesso ao mês de publicação[S/N]? ")
    
    if tem_mes_publicacao.upper == "S":
        mes_publicacao = input("Digite o mês de publicação: ")
        return f"{titulo_artigo}. {titulo_revista}, {local_publicacao}, {numero_volume}, {paginas_inicial_final}, {mes_publicacao}, {ano_publicacao}."
    return f"{titulo_artigo}. {titulo_revista}, {local_publicacao}, {numero_volume}, {paginas_inicial_final}, {ano_publicacao}."

def revistasOuPeriodicos():
    nomeSobrenome = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_revista_periodico()
    return f"\nReferência formatada:\n{nomeSobrenome}. {complemento_referencia}"
        
def informacoes_basicas_artigo_evento():
    titulo_trabalho_apresentado = input("Digite o título do trabalho apresentado: ").title()
    titulo_evento = input("Digite o título do evento: ").upper()
    numero_evento = int(input("Digite o número do evento: "))
    ano_realizacao = int(input("Digite o ano de realização: "))
    cidade_realizacao = input("Digite a cidade de realização: ").title()
    titulo_documento = input("Digite o título / tipo do documento (anais, resumos etc): ").title()
    local_publicacao = input("Digite o local de publicação: ").title()
    editora = input("Digite a editora: ").title()
    ano_publicacao = int(input("Digite o ano de publicação: "))
    paginais_inicial_final = input("Digite as páginas inicial e final <x - y>: ")
    return f"{titulo_trabalho_apresentado}. In: {titulo_evento}, n° {numero_evento}, {ano_realizacao}, {cidade_realizacao}. {titulo_documento}. {local_publicacao}: {editora}, {ano_publicacao}. p. {paginais_inicial_final}"
    

def artigo_em_evento():
    nome_sobrenome = nome_e_sobrenome()
    informacoes_basicas = informacoes_basicas_artigo_evento()
    return f"Referência formatada\n{nome_e_sobrenome}. {informacoes_basicas}."

def informacoes_basicas_monografia_dissertacao_tese():
    titulo_trabalho = input("Digite o título do trabalho: ").title()
    ano_apresentacao = input("Digite o ano de apresentação: ")
    numero_paginas = int(input("Digite o total de páginas: "))
    categoria = input("Digite a categoria (área de concentração): ").title()
    instituição = input("Digite a instituição: ").title()
    local_publicacao = input("Digite o local de publicação: ").title()
    ano_defesa = int(input("Digite o ano de defesa: "))

    temSubtitulo = input("Esse trabalho tem subtítulo [S/N]? ")
    
    if temSubtitulo.uppercased() == "S":
        subtituloTrabalho = input("Digite o subtítulo: ")
        return f"{titulo_trabalho}: {subtituloTrabalho}. {ano_apresentacao}. {numero_paginas}. {categoria} - {instituição}, {local_publicacao}, {ano_defesa}."
    
    else:
        return f"\(tituloTrabalho). \(anoApresentacao). p. \(numeroPaginas). \(categoria) - \(instituição), \(localPublicacao), \(anoDefesa)."

def monografia_dissertacao_tese():
    nome_sobrenome = nome_e_sobrenome()
    informacoes_complementares = informacoes_basicas_monografia_dissertacao_tese()
    return f"\nReferência formatada:\n{nome_sobrenome}. {informacoes_complementares}"

def tipo_de_site():
    tipo_site = input("Digite o tipo de site de acordo com o padrão a seguir: \n[J]: Referências de sites de jornal;\n[R]: Referências de site de revistas eletrônicas;\n[P]: Referências de sites de publicação periódica;\n[I]: Referências de página inicial de sites;\n[E]: Referências de endereços eletrônicos ou enciclopédias ")
        
    if tipo_site.upper() == "J":
        print("\n\nJornal")
        print(siteDeJornal())
        
    elif tipo_site.upper() == "R":
        print("\n\nRevistas eletrônicas")
        print(siteDeRevistasEletronicas())
        
    elif tipo_site.upper() == "P":
        print("\n\nPublicações periódicas")
        print(sitesDePublicacoesPeriodicas())
        
    elif tipo_site.upper() == "I":
        print("\n\nPágina inicial de sites")
        print(pagina_inicial())
        
    elif tipo_site.upper() == "E":
        print("\n\nEnciclopédias ou dicionários")
        print(dicionariosOuEnciclopedias())
        
    else:
        print("Opção inválida. ")

def formata_mes(mes_acesso):
    return f"{mes_acesso[0:3].lower()}"

def dia_mes_ano():
        dia = int(input("Digite o dia de acesso com dois algarismos: "))
        mes = input("Digite o mês de acesso: ")
        ano = input("Digite o ano de acesso: ")
               
        return dia, mes, ano

def site_de_jornal():
    titulo_materia = input("Digite o título da matéria: ")
    nome_jornal = input("Digite o nome do jornal: ")
    url = input("Digite a url: ")
    dia_publicacao, mes_publicacao, ano_publicacao = dia_mes_ano()
    dia_acesso, mes_acesso, ano_acesso = dia_mes_ano()
    mes_acesso = formata_mes()
    
    autoria = input("Você tem acesso ao nome do autor da matéria [S/N]? ")
    cidade = input("Você tem acesso à cidade de publicação [S/N]? ")
    secao = input("Sua pesquisa está contida em alguma seção [S/N]?")
    if autoria_conhecida.upper() == "S" and cidade_publicacao.upper() == "S" and secao.upper() == "S":
        autoria_conhecida = nome_e_sobrenome()
        cidade_publicacao = input("Digite a cidade de publicação: ")
        secao = input("Digite a seção da sua pesquisa: ")
        return f"Referência formatada: \n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {cidade_publicacao}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."

    
    elif autoria_conhecida.upper() == "S" and cidade_publicacao.upper() == "S" and secao.upper() == "N":
        autoria_conhecida = nome_e_sobrenome()
        cidade_publicacao = input("Digite a cidade de publicação: ")
        return f"Referência formatada: \n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
    
    elif autoria_conhecida.upper() == "S" and cidade_publicacao.upper() == "N" and secao.upper() == "S":
        autoria_conhecida = nome_e_sobrenome()
        secao = input("Digite a seção da sua pesquisa: ")
        return f"Referência formatada: \n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
    
    elif autoria_conhecida.upper() == "S" and cidade_publicacao.upper() == "N" and secao.upper() == "N":
        autoria_conhecida = nome_e_sobrenome()
        return f"Referência formatada: \n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}.  Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
    
    elif autoria_conhecida.upper() == "N" and cidade_publicacao.upper() == "S" and secao.upper() == "S":
        cidade_publicacao = input("Digite a cidade de publicação: ")
        secao = input("Digite a seção da sua pesquisa: ")
        return f"Referência formatada: \n{titulo_materia}. {nome_jornal}, {cidade_publicacao}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
    
    elif autoria_conhecida.upper() == "N" and cidade_publicacao.upper() == "S" and secao.upper() == "N":
        cidade_publicacao = input("Digite a cidade de publicação: ")
        return f"Referência formatada: \n{titulo_materia}. {nome_jornal}, {cidade_publicacao}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
    
    elif autoria_conhecida.upper() == "N" and cidade_publicacao.upper() == "N" and secao.upper() == "S":
        secao = input("Digite a seção da sua pesquisa: ")
        return f"Referência formatada: \n{titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
    else:
        return f"Referência formatada: \n{titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."