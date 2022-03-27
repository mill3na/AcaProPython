from csv import excel
import imp
from pandas import array
from multiline_strings import *
from time import sleep

menu_principal = ["Guia do usuário", "Informações sobre o processo de desenvolvimento", "Buscar referências", "Formatar referência", "Formatar referência e salvar automaticamente", "Exibir fontes confiáveis para pesquisa acadêmica", "Sair"]

menu_referencias = ["Livro", "Revistas ou periódicos", "Artigos em eventos", "Websites", "Monografias, dissertações ou teses", "Voltar"]

def exibe_menu(menu):
    print("\n")
    for index, opcao in enumerate(menu):
        print(f"[{index + 1}] {opcao}.")

def exibe_texto_formatado(mensagem, cor = "branco"):
    if cor == "amarelo":
        print(f"\033[33m{mensagem}\033[m\n\n")
    elif cor == "vermelho":
        print(f"\033[31m{mensagem}\033[m\n\n")
    elif cor == "verde":
        print(f"\033[32m{mensagem}\033[m\n\n")
    elif cor == "azul":
        print(f"\033[34m{mensagem}\033[m\n\n")
    elif cor == "roxo":
        print(f"\033[35m{mensagem}\033[m\n\n")
    elif cor == "ciano":
        print(f"\033[36m{mensagem}\033[m\n\n")
    else:
        print(f"{mensagem}\n\n")
    
def criar_arquivo_txt(nome_do_arquivo = "Referencias formatadas"):
    try: 
        novo_arquivo = open(nome_do_arquivo, "a")
        novo_arquivo.close()
        return nome_do_arquivo
    except:
        print("Algo deu errado na criação do arquivo. Tente novamente.")
    
def escrever_no_arquivo_txt(texto_a_ser_inserido, nome_do_arquivo = "Referencias formatadas"):
    try:
        arquivo_txt = open(nome_do_arquivo, "a")
        arquivo_txt.write(f"\n\n{texto_a_ser_inserido}")
        arquivo_txt.close()
        exibe_texto_formatado("Referência salva com sucesso! :)", "azul")
    except:
        print("Não foi possível salvar a referência! Por favor, armazene os dados em outro local para que a referência não seja perdida.")    
    
def seleciona_opcao_menu_principal(menu):
    continue_loop = True
    formatacao =  ""
    while(continue_loop):
        exibe_menu(menu)
        try:
            opcao_menu = int(input("\nDigite a sua opção: "))
            if opcao_menu == len(menu):
                    print("\nSaindo do sistema. Até logo!\n\n")
                    sleep(1)
                    break
            
            elif (int(opcao_menu) > len(menu) or int(opcao_menu) <= 0):
                exibe_texto_formatado("\nOpção inválida! Tente novamente.\n\n", "vermelho")
            
            else:
                if opcao_menu == 1:
                    imprime_multiline_string(guia_do_usuario_completo)
                    
                elif opcao_menu == 2:
                    exibe_texto_formatado("\n\nInformações sobre o processo de desenvolvimento", "verde")
                    imprime_multiline_string(processo_de_desenvolvimento)
                    sleep(1)
                    
                elif opcao_menu == 3:
                    exibe_texto_formatado("\n\nBuscar referências", "verde")
                    print(buscar_referencias)
                    sleep(1)
                    
                elif opcao_menu == 4:
                    exibe_texto_formatado("\n\nFormatar referência", "verde")
                    texto_formatado = formatar_referencias(menu_referencias)
                    exibe_texto_formatado(texto_formatado, "amarelo")
                    sleep(1)
                    
                elif opcao_menu == 5:
                    exibe_texto_formatado("\n\nFormatar referência e salvar automaticamente", "verde")
                    texto_formatado = formatar_referencias(menu_referencias)
                    exibe_texto_formatado(texto_formatado, "amarelo")
                    nome_do_arquivo = criar_arquivo_txt()
                    escrever_no_arquivo_txt(texto_formatado, nome_do_arquivo)
                    sleep(1)
                    
                elif opcao_menu == 6:
                    exibe_texto_formatado("\n\nExibir fontes confiáveis para pesquisa acadêmica", "verde")
                    print(fontes_pesquisa_academica)
                    sleep(1)
                    
                    
        except ValueError:
            exibe_texto_formatado("\nVocê digitou algo no formato errado. Por favor, tente novamente, digitando números inteiros.\n\n", "vermelho")
            print()
            
        except:
            print(Exception)
 
def imprime_multiline_string (multiline_string, first_element=0):
    for opcao in range(first_element, len(multiline_string)):
        print(multiline_string[opcao])
        sleep(1)
        continua = input("Continuar? [digite N para interromper]  ")
        if continua.upper() == "N":
            print("Saindo da seção. Até mais!")
            sleep(1)
            break

def formatar_referencias (menu):
    formatacao = ""
    continua_loop = True
    while(continua_loop):
        exibe_menu(menu)
        try:
            opcao_menu = int(input("\nDigite a sua opção: "))
            if opcao_menu == len(menu):
                    print("\n\nVoltando ao menu principal...")
                    sleep(1)
                    continua_loop = False
            
            elif (int(opcao_menu) > len(menu) or int(opcao_menu) <= 0):
                exibe_texto_formatado("\nOpção inválida! Tente novamente.\n\n", "vermelho")
            
            else:
                if opcao_menu == 1:
                    exibe_texto_formatado("\n\nLivro", "verde")
                    formatacao = quantidade_de_autores()
                    sleep(1)
                    continua_loop = False
                
                elif opcao_menu == 2:
                    exibe_texto_formatado("\n\nRevistas ou periódicos", "verde")
                    formatacao = revistasOuPeriodicos()
                    sleep(1)
                    continua_loop = False
                
                elif opcao_menu == 3:
                    exibe_texto_formatado("\n\nArtigos em eventos", "verde")
                    formatacao = artigo_em_evento()
                    sleep(1)
                    continua_loop = False
                
                elif opcao_menu == 4:
                    exibe_texto_formatado("\n\nWebsites", "verde")
                    formatacao = tipo_de_site()
                    sleep(1)
                    continua_loop = False
                
                else:
                    exibe_texto_formatado("\n\nMonografias, dissertações ou teses", "verde")
                    formatacao = monografia_dissertacao_tese()
                    sleep(1)
                    continua_loop = False
               
        except ValueError:
            print("\nVocê digitou algo no formato errado. Por favor, tente novamente, digitando números inteiros.\n\n")
            
        except:
            print(Exception)       
    return formatacao
                 
def nome_e_sobrenome():
    nome = input("Digite o primeiro nome do autor: ")
    sobrenome = input("Digite o sobrenome do autor: ")
    return f"{sobrenome.upper()}, {nome.capitalize()}"

def informacoes_basicas_livro():
    tituloDaObra = input("Digite o título do livro: ").capitalize()
    localPublicação = input("Digite o local de publicação: ").capitalize()
    editora = input("Digite a editora: ").capitalize()
    anoPublicação = input("Digite o ano de publicação: ")
    temSubtitulo = input("Esse livro tem subtítulo [S/N]? ")
    temEdicao = input("Essa obra tem edição [S/N]? ")
    
    if (temSubtitulo.upper() == "S") and (temEdicao.upper() == "S"):
        subtituloObra = input("Digite o subtitulo da obra: ").capitalize()
        edicaoObra = input("Digite a edição (somente o número): ")
        return f"{tituloDaObra}: {subtituloObra}. {edicaoObra}. ed. {localPublicação}: {editora}, {anoPublicação}."
    
    
    elif (temSubtitulo.upper() == "S") and (temEdicao.upper() == "N"):
        subtituloObra = input("Digite o subtitulo da obra: ").capitalize()
        return f"{tituloDaObra}: {subtituloObra}. {localPublicação}: {editora}, {anoPublicação}."
    
    
    elif (temSubtitulo.upper() == "N") and (temEdicao.upper() == "S"):
        edicaoObra = input("Digite a edição (somente o número): ")
        return f"{tituloDaObra}. {edicaoObra}. ed. {localPublicação}: {editora}, {anoPublicação}."
     
    else:
       return f"\033[1m{tituloDaObra}\033[m. {localPublicação}: {editora}, {anoPublicação}."

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
            formatacao = livro_dois_autores()
            continua_loop = False
        elif quantidade_autores == 3:
            formatacao = livro_tres_autores()
            continua_loop = False
        elif quantidade_autores > 3:
            formatacao = livro_muitos_autores()
            continua_loop = False
        else:
            print("\nOpção inválida. Tente novamente. \n\n")
    print(formatacao)
    return formatacao

def livro_um_autor():
    nome_e_sobrenome_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"\n{nome_e_sobrenome_autor}. {complemento_referencia}" 

def livro_dois_autores():
    print("\nPrimeiro autor\n")
    nome_e_sobrenome_primeiro_autor = nome_e_sobrenome()
    print("\nSegundo autor\n")
    nome_e_sobrenome_segundo_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"\n{nome_e_sobrenome_primeiro_autor}; {nome_e_sobrenome_segundo_autor}. {complemento_referencia}" 

def livro_tres_autores():
    print("\nPrimeiro autor\n")
    nome_e_sobrenome_primeiro_autor = nome_e_sobrenome()
    print("\nSegundo autor\n")
    nome_e_sobrenome_segundo_autor = nome_e_sobrenome()
    print("\nTerceiro autor\n")
    nome_e_sobrenome_terceiro_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"\n{nome_e_sobrenome_primeiro_autor}; {nome_e_sobrenome_segundo_autor}; {nome_e_sobrenome_terceiro_autor}. {complemento_referencia}" 

def livro_muitos_autores():
    nome_e_sobrenome_autor = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_livro()
    return f"\n{nome_e_sobrenome_autor} et al. {complemento_referencia}"

def livro_autor_desconhecido():
    tituloObra = input("Digite o título do livro: ")
    localPublicação = input("Digite o local de publicação: ")
    editora = input("Digite a editora: ")
    anoPublicação = input("Digite o ano de publicação: ")
        
    return f"\n{tituloObra.upper()}. {localPublicação}: {editora}, {anoPublicação}."

def informacoes_basicas_revista_periodico():
    titulo_artigo = input("Digite o título do artigo: ").capitalize()
    titulo_revista = input("Digite o título da revista: ").capitalize()
    local_publicacao = input("Digite o local de publicação: ").capitalize()
    numero_volume = int(input("Digite o número do volume: "))
    paginas_inicial_final = input("Digite as páginas inicial e final <x - y>: ")
    ano_publicacao = int(input("Digite o ano de publicação: "))
    
    tem_mes_publicacao = input("Você tem acesso ao mês de publicação[S/N]? ")
    
    if tem_mes_publicacao.upper == "S":
        mes_publicacao = input("Digite o mês de publicação: ")
        return f"{titulo_artigo}. {titulo_revista}, {local_publicacao}, {numero_volume}, {paginas_inicial_final}, {mes_publicacao}, {ano_publicacao}."
    return f"\n{titulo_artigo}. {titulo_revista}, {local_publicacao}, {numero_volume}, {paginas_inicial_final}, {ano_publicacao}."

def revistasOuPeriodicos():
    nomeSobrenome = nome_e_sobrenome()
    complemento_referencia = informacoes_basicas_revista_periodico()
    return f"\n{nomeSobrenome}. {complemento_referencia}"
        
def informacoes_basicas_artigo_evento():
    titulo_trabalho_apresentado = input("Digite o título do trabalho apresentado: ").capitalize()
    titulo_evento = input("Digite o título do evento: ").upper()
    numero_evento = int(input("Digite o número do evento: "))
    ano_realizacao = int(input("Digite o ano de realização: "))
    cidade_realizacao = input("Digite a cidade de realização: ").capitalize()
    titulo_documento = input("Digite o título / tipo do documento (anais, resumos etc): ").capitalize()
    local_publicacao = input("Digite o local de publicação: ").capitalize()
    editora = input("Digite a editora: ").capitalize()
    ano_publicacao = int(input("Digite o ano de publicação: "))
    paginais_inicial_final = input("Digite as páginas inicial e final <x - y>: ")
    return f"{titulo_trabalho_apresentado}. In: {titulo_evento}, n° {numero_evento}, {ano_realizacao}, {cidade_realizacao}. {titulo_documento}. {local_publicacao}: {editora}, {ano_publicacao}. p. {paginais_inicial_final}"
    
def artigo_em_evento():
    nome_sobrenome = nome_e_sobrenome()
    informacoes_basicas = informacoes_basicas_artigo_evento()
    return f"\n{nome_sobrenome}. {informacoes_basicas}."

def informacoes_basicas_monografia_dissertacao_tese():
    titulo_trabalho = input("Digite o título do trabalho: ").capitalize()
    ano_apresentacao = input("Digite o ano de apresentação: ")
    numero_paginas = int(input("Digite o total de páginas: "))
    categoria = input("Digite a categoria (área de concentração): ").capitalize()
    instituição = input("Digite a instituição: ").capitalize()
    local_publicacao = input("Digite o local de publicação: ").capitalize()
    ano_defesa = int(input("Digite o ano de defesa: "))

    temSubtitulo = input("Esse trabalho tem subtítulo [S/N]? ")
    
    if temSubtitulo.upper() == "S":
        subtitulo_trabalho = input("Digite o subtítulo: ")
        return f"\n{titulo_trabalho}: {subtitulo_trabalho}. {ano_apresentacao}. {numero_paginas}. {categoria} - {instituição}, {local_publicacao}, {ano_defesa}."
    
    else:
        return f"{titulo_trabalho}. {ano_apresentacao}. p. {numero_paginas}. {categoria} - {instituição}, {local_publicacao}, {ano_defesa}."

def monografia_dissertacao_tese():
    nome_sobrenome = nome_e_sobrenome()
    informacoes_complementares = informacoes_basicas_monografia_dissertacao_tese()
    return f"\n\n{nome_sobrenome}. {informacoes_complementares}"

def tipo_de_site():
    tipo_site = input("Digite o tipo de site de acordo com o padrão a seguir: \n[J]: Referências de sites de jornal;\n[R]: Referências de site de revistas eletrônicas;\n[P]: Referências de sites de publicação periódica;\n[I]: Referências de página inicial de sites;\n[E]: Referências de endereços eletrônicos ou enciclopédias.\n ")
        
    if tipo_site.upper() == "J":
        print("\n\nJornal")
        print(site_de_jornal())
        
    elif tipo_site.upper() == "R":
        print("\n\nRevistas eletrônicas")
        print(sites_revistas_eletronicas)  
              
    elif tipo_site.upper() == "P":
        print("\n\nPublicações periódicas")
        print(sites_publicacoes_periodicas())
        
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

def dia_mes_ano(acesso_ou_publicacao):
        dia = int(input(f"Digite o dia de {acesso_ou_publicacao} com dois algarismos: "))
        mes = input(f"Digite o mês de {acesso_ou_publicacao}: ")
        ano = input(f"Digite o ano de {acesso_ou_publicacao}: ")
               
        return dia, mes, ano

def site_de_jornal():
    try:
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
            return f"\n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {cidade_publicacao}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."

        
        elif autoria_conhecida.upper() == "S" and cidade_publicacao.upper() == "S" and secao.upper() == "N":
            autoria_conhecida = nome_e_sobrenome()
            cidade_publicacao = input("Digite a cidade de publicação: ")
            return f"\n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
        
        elif autoria_conhecida.upper() == "S" and cidade_publicacao.upper() == "N" and secao.upper() == "S":
            autoria_conhecida = nome_e_sobrenome()
            secao = input("Digite a seção da sua pesquisa: ")
            return f"\n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
        
        elif autoria_conhecida.upper() == "S" and cidade_publicacao.upper() == "N" and secao.upper() == "N":
            autoria_conhecida = nome_e_sobrenome()
            return f"\n{autoria_conhecida}. {titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}.  Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
        
        elif autoria_conhecida.upper() == "N" and cidade_publicacao.upper() == "S" and secao.upper() == "S":
            cidade_publicacao = input("Digite a cidade de publicação: ")
            secao = input("Digite a seção da sua pesquisa: ")
            return f"\n{titulo_materia}. {nome_jornal}, {cidade_publicacao}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
        
        elif autoria_conhecida.upper() == "N" and cidade_publicacao.upper() == "S" and secao.upper() == "N":
            cidade_publicacao = input("Digite a cidade de publicação: ")
            return f"\n{titulo_materia}. {nome_jornal}, {cidade_publicacao}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
        
        elif autoria_conhecida.upper() == "N" and cidade_publicacao.upper() == "N" and secao.upper() == "S":
            secao = input("Digite a seção da sua pesquisa: ")
            return f"\n{titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Seção {secao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
        else:
            return f"\n{titulo_materia}. {nome_jornal}, {dia_publicacao} {mes_publicacao}. {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_acesso} {mes_acesso}. {ano_acesso}."
    except:
        exibe_texto_formatado("Algo deu errado ao formatar a referência do jornal!", "vermelho")
        
def sites_revistas_eletronicas():
    nome_autor = nome_e_sobrenome()
    titulo_do_artigo = input("Digite o título do artigo: ")
    titulo_da_revista = input("Digite o título da revista: ")
    local_publicacao = input("Digite o local de publicação: ")
    volume_exemplar = int(input("Digite o número do exemplar: ")) 
    numero_exemplar = int(input("Digite o número do exemplar: "))
    paginas_inicial_final = input("Digite as páginas inicial e final <x - y>: ")
    mes_publicacao = input("Digite o mês de publicação: ")
    ano_publicacao = int(input("Digite o ano de publicação: "))
    url = input("Cole aqui a url (link) da pesquisa: ")
    dia_mes_ano_acesso = dia_mes_ano()
    return f"\n{nome_autor}. {titulo_do_artigo}. {titulo_da_revista}, {local_publicacao}, v. {volume_exemplar}, n. {numero_exemplar}, p. {paginas_inicial_final}, {mes_publicacao}, {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_mes_ano_acesso}."

def sites_publicacoes_periodicas():
    titulo_materia = input("Digite o título da matéria: ")
    nome_site = input("Digite o nome do site: ")
    ano_publicacao = int(input("Digite o ano de publicação: "))
    url = input("Cole aqui a url (link) da pesquisa: ")
    dia_mes_ano_acesso = dia_mes_ano()
        
    tem_autor = input("Você tem acesso ao nome do autor [S/N]? ")
    if tem_autor.upper() == "S":
        nome_do_autor = nome_e_sobrenome()
            
        return f"\n{nome_do_autor}. {titulo_materia}. {nome_site}, {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_mes_ano_acesso}."
        
    else:
        return "\n\(tituloMateria.uppercased()). \(nomeSite), \(anoPublicacao). Disponível em: \(url). \(diaMesAno)"  
    
def pagina_inicial():
        autor_organizacao = input("Digite o nome do autor ou organização: ")
        nome_site = input("Digite o nome do site: ")
        ano_publicacao = int(input("Digite o ano de publicação: "))
        ementa = input("Digite a descrição da pesquisa: ")
        url = input("Cole aqui a url (link) da pesquisa: ")
        dia_mes_ano_acesso = dia_mes_ano()
        
        return f"\n{autor_organizacao.upper()}, {nome_site}, {ano_publicacao}. {ementa}. Disponível em: {url}. Acesso em: {dia_mes_ano_acesso}."
    
def dicionariosOuEnciclopedias():
        titulo_verbete_conceito = input("Digite o título do verbete/conceito: ")
        nome_da_enciclopedia_dicionario = input("Digite o nome da enciclopédia/dicionário: ")
        autor_editora = input("Digite o responsável pela publicação ou a editora: ")
        ano_publicacao = int(input("Digite o ano de publicação: "))
        url = input("Cole aqui a url (link) da pesquisa: ")
        dia_mes_ano_acesso = dia_mes_ano()
                
        return f"\n{titulo_verbete_conceito.upper()}. In: {nome_da_enciclopedia_dicionario}. {autor_editora}, {ano_publicacao}. Disponível em: {url}. Acesso em: {dia_mes_ano_acesso}."

  