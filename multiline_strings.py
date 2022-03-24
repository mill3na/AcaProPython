from time import sleep


aca_pro = '''




      ___      ___    ___       _  __    _ ___    ____       
    /  _  \  /  _ |  /  _  \   |  `_ \  | `___| /  _  \      
   |  (_|  ||  (__  |  (_|  |  | (_)  | | |    |  (_)  |     
    \ __,_ | \____|  \ __,_ |  | .__ /  |_|     \ ___ /     
                               |_|                           
             Auxiliar de produção acadêmica                  




'''

bem_vindo = '''
Seja bem vindo ao guia do usuário. Aqui você encontra todas as informações pertinentes para fazer uso correto dessa aplicação. 
    
    Você pode usar esse programa para te auxiliar nas seguintes coisas: 
        	- Consultar informações sobre o processo de desenvolvimento de produções acadêmicas
         
            - Buscar referências ou eixos de pesquisa, caso esteja travado ou sem inspiração
            
            - Formatar referências para sua produção acadêmica e falicitar sua vida (é só dar Ctrl + c e 
                Ctrl + v, no final (: 
                
            - Formatar referência e salvar automaticamente em um documento de texto, para que você não perca esses dados em casos extraordinários
            
            - Exibir fontes confiáveis para pesquisa acadêmica, caso você não saiba bem onde pesquisar.


    '''
    
primeiros_passos = '''

     ► Primeiros passos _______________
    
        Ao iniciar a execução, é importante que você esteja em um ambiente que aceite dados de entrada. Por exemplo: o output do VsCode não aceita entrada de dados por parte do usuário, e o programa precisa de algumas informações para funcionar como deve. Você pode colocar o script para rodar no cmd ou terminal integrado sem se preocupar, pois vai ser sucesso.
        
        O primeiro menu te dá as seguintes opções:
                    
            [1]: Guia do usuário

            [2]: Formatar referências

            [3]: Buscar eixos de pesquisa

            [4]: Tipos de referência
            
            [5]: Processo de desenvolvimento

            [5]: Sair
        
        A última opção do primeiro menu é "Sair", e isso interrompe a execução desse script, ok? Outra coisa a se lembrar é: sempre acesse as opções pelo número antes dela.
        
        De acordo com a opção escolhida, um novo menu abrirá e/ou novas informações podem ser solicitadas. A lógica é basicamente a mesma para tudo que segue após isso. 
        
        Sempre tente digitar as coisas certinho, sem erros de português, pois isso pode levar o código a caminhos que você não queria originalmente. 

Agora, vamos ver cada opção, separadamente.
    
    
    '''

guia_do_usuário = '''
     ► Guia do usuário _______________
     
     O Guia do usuário exibirá o manual do programa (este aqui), e informa ao usuário como usar corretamente todas as funcionalidades que o AcaPro tem a oferecer. Depois de exibir este guia, o programa será encerrado.


'''

formatar_referencias = '''

     ► Formatar referências _______________

        Ao chegar aqui, outro menu será exibido: 

            [1]: Livro

            [2]: Revista ou artigo de periódico

            [3]: Artigo em evento

            [4]: Websites

            [5]: Monografia, dissertação ou tese.

            Cada opção escolhida levará à uma nova parte do programa, que solicitará informações diferentes. Sempre se atente ao tipo de entrada que o programa solicita, certo? Elas podem ser do tipo inteiro ou do tipo string (texto). Por exemplo, ao solicitar a formatação de uma referência retirada de um livro, o programa perguntará a quantidade de autores, e você deve digitar um inteiro. Logo depois, dependendo da resposta, ele pergunta o nome dos autores, e você deve digitar uma String (texto).

            Quando o nome do autor for solicitado, digite somente o primeiro, e não o nome completo. O sobrenome será solicitado em seguida.

            O AcaPro é preparado para ajustar alguns pequenos detalhes do seu texto, como a utilização da primeira letra maiúscula, mas erros de digitação devem ser evitados, pois não temos corrigir nomes próprios ou de revistas, por exemplo, certo? Sempre tome o cuidado de oferecer as informações corretas.


'''

eixos_de_pesquisa = '''

     ► Buscar eixos de Pesquisa _______________

        Nesta seção, o AcaPro irá te sugerir algumas grandes áreas e palavras chave que podem ajudar a encontrar um bom tema. Depois da exibição de sugestões, o programa é encerrado.


'''

tipos_de_referência = '''

     ► Tipos de referêncua _______________

        Ao escolher esta opção, será exibido um mini guia sobre cada tipo de referência que o AcaPro formata (e não todas as existentes). Esta seção é ideal para quem não tem certeza em que tipo de material está fazendo as suas pesquisas.

        Aqui também são exibidos vários sites que podem ser usados para pesquisar referências realmente confiáveis, de pesquisadores e publicações cuidadosamente avaliadas.
        
        
'''

inf_processo_desenvolvimento1 = '''

     ► Informações sobre o processo de desenvolvimento _______________
    
        Desenvolver trabalhos acadêmicos é uma coisa bem séria e importante, mas nem sempre é fácil começar. Então, esse mini guia vai te mostrar como facilitar esse processo.
        
        A primeira coisa a se lembrar é: tudo é formal e tem que ser em um formato específico, delimitado pela ABNT. "Ah, mas esse meu trabalho nem precisa.", você pode me dizer. Tudo bem, mas uma pode ser que precise, e quanto mais você praticar, mais fácil vai ser. Então, que tal um mini passo a passo? 
         
         
    '''
    
inf_processo_desenvolvimento2 = '''

    0. Passo mais importante de todos os tempos
    
    Escolha um bom orientador. Um BOM MESMO. 
    Tenha uma rede de apoio. Você (muito) provavelmente vai precisar, em algum momento.

    
'''

inf_processo_desenvolvimento3 = '''

    1. Saiba o que você está escrevendo.
    
    É uma resenha? Um artigo? Uma dissertação? Um relatório?
    Defina o tipo de texto e busque as referências certas para que ele seja bem estruturado, combinado? Se tem dúvida, pergunte ao seu professor orientador.
    
    É importante também buscar as plataformas certas para formatar seu texto. Word, Overleaf, Docs... Não apele para um comum que peque nas funcionalidades, escolha um bom editor de texto para não ter dor de cabeça no final. 
    
    
    '''

inf_processo_desenvolvimento4 = ''''

    2. Define teu tema sem medo de ser feliz!
    
    Faz pesquisa, vê notícia, observa os conteúdos que são mais comentados (e que têm mais referência) e pensa em uma grande área. Tenta relacionar com o que você gosta de estudar que fica muito mais massa. Temas multidisciplinares são muito bons também, mas define esse negócio direito, tá? Vai se ambientando primeiro e, dependendo do que você encontrar / se identificar, define um tema, e, depois, um subtema.
    
    O subtema é legal pra afunilar mais a tua pesquisa! Se isso não estiver explícito no tema (nicho, afunilamento), um subtema é bem legal pra deixar bem claro.
    
    
'''

inf_processo_desenvolvimento4 = ''''

    3. Hora de começar a escrever.
    
    Achou informações sufucientes pra se embasar (pelo menos um pouco) e já decidiu tudo que precisava ser decidido? Então, tá esperando o quê? Começa a escrever tendo em mente tudo aquilo que foi pesquisado e sem medo de voltar a consultar tuas fontes de novo. Mas, pelo amor de tudo que é mais lindo nesse mundo, não comete plágio! Cuidado com essas referências, coloca os créditos direitinho, porque não é nada legal pegar o trabalho dos outros, beleza? 
    
    Importante se atentar à formatação desde o início também (pelo menos o basicão), pra não te estressar muito no final, pode ser?
    
    Revisa o texto 5 mil vezes se for preciso (e vai ser preciso / vai valer a pena), e sempre conte com a ajuda do seu orientador.
    
    
'''

inf_processo_desenvolvimento5 ='''

    4. Últimos detalhes pro lançamento do foguete!
    
    Aquela revisada básica e tal. Cansou muito, enjoou do teu próprio trabalho? Pede pra um amigo de confiança (e crítico na medida) ler pra dar uma força. Conte com a sua rede de apoio.
    


'''

inf_processo_desenvolvimento6 = '''
    5. Finaliza com sucesso.
    
    Tudo certinho? Então massa demais. Parabéns, você conseguiu!!!
    
'''

sair = '''

     ► Sair _______________

        Escolher essa opção encerra o programa. Esperamos que você volte a usá-lo!
'''

guia_do_usuario_completo = [aca_pro, bem_vindo, primeiros_passos, guia_do_usuário, formatar_referencias, eixos_de_pesquisa, tipos_de_referência, inf_processo_desenvolvimento1, inf_processo_desenvolvimento2, inf_processo_desenvolvimento3, inf_processo_desenvolvimento4, inf_processo_desenvolvimento5, inf_processo_desenvolvimento5, inf_processo_desenvolvimento6]


processo_de_desenvolvimento = [inf_processo_desenvolvimento1, inf_processo_desenvolvimento2, inf_processo_desenvolvimento3, inf_processo_desenvolvimento4, inf_processo_desenvolvimento5, inf_processo_desenvolvimento5, inf_processo_desenvolvimento6]

fontes_pesquisa_academica = '''

Para fazer um bom trabalho, é importante se basear em fontes realmente confiáveis. A seguir, você encontra um apanhado de sites que podem te ajudar a encontrar suas referências:

    - Scielo
    - Google acadêmico
    - ERIC
    - Portal da Capes
    - Academia.edu
    - BDTD
    - Redalyc
    - Biblioteca digital de tedes e dissertações da USP
    - LUME (UFRGS)
    
'''

buscar_referencias = '''

Está com dúvida sobre como pesquisar o seu assunto? Quel tal usar alguma dessas palavras chave?

    - estudo de caso
    - notícias
    - contexto internacional
    - impactos
    - motivação
    - problemática
    - legislação
    - desafios
    - perpspectivas
    
'''