#IMPORTANDO BIBLIOTICAS
import os #BIBLIOTECA SENDO USADA PARA LIMPAR O TERMINAL DURANTE A EXECUÇÃO EM ALGUMAS PARTES DO ALGORITMO
from random import randint #BIBLIOTECA SENDO USADA PARA GERAR UM NÚMERO INTEIRO ALEATÓRIO
#VARIAVEIS
#DO TIPO VETOR
catalogo=['1..Bandana','2..Jaqueta','3..Camisa','4..Calça','5..Botas','6..Finalizar compra','7..Sair']
coresbandana=['AZUL','VERMELHA','AMARELA','PRETA']
tamanhojaqueta=['PP','P','M','G','GG']
tamanhocamisa=['PP','P','M','G','GG']
tamanhocalca=['36','38','40','42','44','46','48']
tamanhobota=['36~37','38~39','40~41','42~43','44~45','46~47']
carrinho=[]
#DO TIPO FLOAT
precobandana=24.9
precojaqueta=249.9
precocamisa=49.9
precocalca=99.9
precobota=149.9
total=0
totalparcelado=0
'''
FERRAMENTAS UTILIZADAS:
ESCREVA e LEIA:OK
SE...ENTÃO...SENÃO:OK
Conectivos E e OU: OK
ESCOLHA...CASO:OK
ENQUANTO:OK
PARA:OK
VETOR:OK
'''
#COMEÇO DO PROGRAMA
#UTILIZANDO O 'ENQUANTO' PARA MANTER O LOOP ATÉ FINALIZAR O PROGRAMA
while True:
    #CRIANDO UMA VARIÁVEL BOOLEANA PARA AUXILIAR NA FINALIZAÇÃO DE ALGUNS LOOPS DURANTE O PROGRAMA
    aux=False
    #UTILIZA UMA FUNÇÃO DA BIBLIOTECA 'os' PARA LIMPAR O TERMINAL
    os.system("cls")
    #UTILIZANDO O 'ESCREVAL' PARA INTRODUZIR O INICIO DO PROGRAMA
    print("""
   *       )           )       (
 (  `   ( /(  *   ) ( /(   (   )\ )        (
 )\))(  )\()` )  /( )\())  )\ (()/(   (  ( )\ (
((_)()\((_)\ ( )(_)((_)\ (((_) /(_))  )\ )((_))
(_()((_) ((_(_(_())  ((_))\___(_)) _ ((_((_)_((_)
|  \/  |/ _ |_   _| / _ ((/ __| | | | | || _ | __|
| |\/| | (_) || |  | (_) | (__| |_| |_| || _ | _|
|_|  |_|\___/ |_|   \___/ \___|____\___/ |___|___|
    ___                                .'-----\\ _
    \  \                              //      #``.) __
     \  \_________                     __--~~--_-\\/ |)
      \           ~~-              _-~~         -_``.|)
|\_.--~~~~~~~~~~-._  \________   _~   Harley-   |   \\
|/   (} _..._/*/   \          ~\~      Davidson |    ``.--~~~~~--__
/___-~~~    /=/~-_  ~~~--------~~--------------/    .-~\\ _________~
  *     ---/=/    \  \       /[]===_____===_  ||   /  __``.    / \   *
      / __/=/_\____\__\     /[]###/===  \###\ ||  /__/    \\ /
 |   | [ |*|___________~~~~~==/ ##\_____/## \ \|  |  |------*------|  |
      \ ~~___________________/ /_##+++++++*  | |           /  |
  *     ---\_)________________/___________\_/ /    *   \ /     \ /   *
    *           *     \_)____________________/       *    ~~~~~    *
       -------                                           -------
Bem Vindo à HARLEY BH MOTOCLUBE
Produtos licenciados e exclusivos Harley Davidson
Todos os produtos são confeccionados com as cores e estampas da marca Harley Davidson
Segue em lista nossos produtos""")
    #'ESCREVA' MOSTRANDO TODOS OS ITENS DO CATÁLOGO
    print(catalogo)
    #SE TIVER ITENS NA VETOR 'CARRINHO' UTILIZA O 'PARA' E MOSTRA OS ITENS NO CARRINHO
    for i in range(len(carrinho)):
        #ESCREVE A POSIÇÃO INDICANDO O INDICE DO 'VETOR' E O SEU CONTEUDO
        print("Carrinho:<",i,">",carrinho[i])
    #'LEIA' SENDO UTILIZADO PARA PEGAR O QUE O USUÁRIO DIIGTAR E COLOCAR EM UMA VARIÁVEL INTEIRA CHAMADA MENU
    menu=int(input("O que quer fazer hoje:\n"))
    #'ESCOLHA..CASO' UTILIZANDO O QUE FOI ESCRITO NA VARIÁVEL MENU PARA NAVEGAR AS OPÇÕES DO ALGORITMO
    match menu:
        case 1:
            #'ENQUANTO' PARA MOSTRAR AS OPÇÕES DESSE ÍNDICE ENQUANTO O USUÁRIO DIGITAR ALGO DIFERENTE DAS OPÇÕES MOSTRADAS
            while True:
                #USO DO 'ESCREVAL'
                print(catalogo[0])
                #USO DO 'ESCREVAL'
                print(coresbandana)
                #'LEIA' ARMAZENANDO O QUE A PESSOA DIGITOU
                escolhabandana=input("Diga qual cor você quer:\n")
                #UTILIZANDO O 'PARA' VERIFICANDO SE DENTRO DO VETOR EXISTE O QUE A PESSOA DIGITOU
                for i in range(len(coresbandana)):
                    #ARMAZENA DENTRO DA VARIÁVEL O ITEM QUE O ÍNDICE DE ESTÁ TRABALHO
                    estoquebandana=coresbandana[i]
                    #UTILIZANDO O 'SE..ENTAO' PARA COMPARAR O QUE FOI DIGITAR COM O ITEM QUE ESTÁ DENTRO DO VETOR
                    if estoquebandana==escolhabandana.upper():
                        #'SE' FOREM IGUAIS '==' TORNA A VARIVÁVEL BOOLEANA VERDADEIRA
                        aux=True
                #'SE' A VARIÁVEL BOOLEANA FOR VERDADEIRA
                if aux==True:
                    #FINALIZA O LOOP UTILIZANDO O 'BREAK'
                    break
            #'ESCREVAL' MOSTRANDO A VARIÁVEL 'FLOAT' DO VALOR QUE SERÁ CALCULADO
            print("O preço da bandana é:R$",precobandana)
            #USO DO 'LEIA' PARA ARMAZERAR UM VALOR INTEIRO À VARIÁVEL
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            #UTILIZANDO O 'ESCOLHA..CASO' PARA DEFINIR SE A PESSOA QUER CONTINUAR OU NÃO O PROCESSO
            match comprar:
                #'CASO 1' COLOCA NA ULTIMA POSIÇÃO LIVRE DO CARRINHO A IDENTIFICAÇÃO DO ITEM, O ITEM QUE FOI VERIFICADO SE EXISTE E O PREÇO DO ITEM
                case 1:
                    carrinho.append('Bandana '+escolhabandana.upper()+' R$'+str(precobandana))
                    #FAZ A SOMA DO VALOR DA BANDANA NO VALOR FINAL PARA O CLIENTE
                    total=total+precobandana
                #'OUTRO CASO' VOLTA AO MENU PRINCIPAL PELA FALTA DE CONTINUAÇÃO DO PROCESSO
        case 2: #VIDE CASO 1 PARA EXPLICAÇÃO DO FUNCIONAMENTO
            while True:
                print(catalogo[1])
                print(tamanhojaqueta)
                escolhajaqueta=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhojaqueta)):
                    estoquejaqueta=tamanhojaqueta[i]
                    if estoquejaqueta == escolhajaqueta.upper():
                        aux=True
                if aux==True:
                    break
            print("O preço da jaqueta é:R$",precojaqueta)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('Jaqueta '+escolhajaqueta.upper()+' R$'+str(precojaqueta))
                    total=total+precojaqueta
        case 3: #VIDE CASO 1 PARA EXPLICAÇÃO DO FUNCIONAMENTO
            while True:
                print(catalogo[2])
                print(tamanhocamisa)
                escolhacamisa=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhocamisa)):
                    estoquecamisa=tamanhocamisa[i]
                    if estoquecamisa==escolhacamisa.upper():
                        aux=True
                if aux==True:
                    break
            print("O preço da camisa é:R$",precocamisa)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('Camisa '+escolhacamisa.upper()+' R$'+str(precocamisa))
                    total=total+precocamisa
        case 4: #VIDE CASO 1 PARA EXPLICAÇÃO DO FUNCIONAMENTO
            while True:
                print(catalogo[3])
                print(tamanhocalca)
                escolhacalca=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhocalca)):
                    estoquecalca=tamanhocalca[i]
                    if estoquecalca==escolhacalca:
                        aux=True
                if aux==True:
                    break
            print("O preço a calça é:R$",precocalca)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('Calça '+escolhacalca+' R$'+str(precocalca))
                    total=total+precocalca
        case 5: #VIDE CASO 1 PARA EXPLICAÇÃO DO FUNCIONAMENTO
            while True:
                print(catalogo[4])
                print(tamanhobota)
                escolhabota=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhobota)):
                    estoquebota=tamanhobota[i]
                    if estoquebota==escolhabota:
                        aux=True
                if aux==True:
                    break
            print(escolhabota)
            print("O preço da bota é:R$",precobota)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('bota '+escolhabota+' R$'+str(precobota))
                    total=total+precobota
        case 6:
            while True:
                #USO DO 'ESCREVAL'
                print(catalogo[5])
                #USO DO 'PARA' NAVEGAR OS ITENS DO 'VETOR':'CARRINHO'
                for i in range(len(carrinho)):
                    #USO DO 'ESCREVAL' MOSTRANDO OS ITENS DO CARRINHO COM O ÍNDICE
                    print("Carrinho:<",i,">",carrinho[i])
                #USO DO 'ESCREVAL' PARA MOSTRAR O TOTAL DA COMPRA
                print("O total da sua compra é:R$"+str(total))
                #USO DO 'ESCREVAL'
                print("""Estamos trabalho com cartão de crédito e dinheiro
Pagamentos no dinheiro tem desconto de 10%
Pagamentos no cartão de crédito e avista tem desconto de 5%
Pagamentos no cartão de crédito parcelado tem acrescimo de 1,5% por parcela""")
                #USO DO 'LEIA' PARA PEGAR O TIPO DO PAGAMENTO
                pagamento=int(input("Como deseja pagar?\n1..Cartão\n2..Dinheiro\n"))
                #'SE' O PAGAMENTO FOR IGUAL 1
                if pagamento==1:
                    #USO DO 'LEIA' PARA PEGAR O NÚMERO DE PARCELAS
                    parcelas=int(input("Diga o número de parcelas:"))
                    #SE O TIPO DO PAGAMENTO FOR CARTÃO UTILIZA O CONECTIVO 'E' PARA DEFINIR SE DUAS CONDIÇÕES SÃO ACEITAS
                    if pagamento==1 and parcelas<=1:
                        #USO DO 'ESCREVAL'
                        print("O seu total é:R$"+str(total)+"\nCom o desconto de 5%:R$"+(str(round(total-(total*(5/100)),2))))
                        #USO DO  'LEIA' PARA DEFINIR SE VAI CONTINUAR O PROCESSO
                        confirmar=input("Confirmar? <SIM> <NÂO>\n")
                        #USO DO 'SE' E DO CONECTIVO 'OU' PARA ACEITAR DOIS TIPOS DE 'LEIA'
                        if confirmar=="SIM" or confirmar=="sim":
                                    #MUDA O VALOR DA VARIÁVEL AUXILIAR
                                    aux=True
                    #USO DO 'SENAO' PARA SE AS CONDIÇÕES ANTERIORES FOREM NÃO ATENDIDAS VERIFICAR SE ESSAS CONDIÇÃO SAO ATENDIDAS
                    elif pagamento==1 and parcelas > 1:
                        #FAZ O CÁLCULO DO ACRESCIMO DOS JUROS DA OPÇÃO
                        #USO DO 'ESCREVAL' PARA MOSTRAR O TOTAL POR PARCELAS E O TOTAL FINAL COM OS JUROS
                        totalparcelado=(total/parcelas)+((total/parcelas)*(1.5/100))
                        print("Cada parcela saira por:R$"+str(round(totalparcelado,2)))
                        total=totalparcelado*parcelas
                        print("E o total final ficará em:R$"+str(round(total,2)))
                         #USO DO  'LEIA' PARA DEFINIR SE VAI CONTINUAR O PROCESSO
                        confirmar=input("Confirmar? <SIM> <NÂO>\n")
                        #USO DO 'SE' E DO CONECTIVO 'OU' PARA ACEITAR DOIS TIPOS DE 'LEIA'
                        if confirmar=="SIM" or confirmar=="sim":
                                    #MUDA O VALOR DA VARIÁVEL AUXILIAR
                                    aux=True
                else:
                    #USO DO 'ESCREVAL' PARA MOSTRAR OS VALORES DESSA CONDIÇÃO
                    print("O seu total é:R$"+str(total)+"\nCom o desconto de 10%:R$"+(str(round(total-(total*(10/100)),2))))
                     #USO DO  'LEIA' PARA DEFINIR SE VAI CONTINUAR O PROCESSO
                    confirmar=input("Confirmar? <SIM> <NÂO>\n")
                    #USO DO 'SE' E DO CONECTIVO 'OU' PARA ACEITAR DOIS TIPOS DE 'LEIA'
                    if confirmar=="SIM" or confirmar=="sim":
                        #MUDA O VALOR DA VARIÁVEL AUXILIAR
                        aux=True
                #USO DO 'SE' PARA VERIFICAR SE A VARIÁVEL BOOLEANA ATENDE O VALOR
                if aux==True:
                    #'SE' A VARIVÁVEL FOR VERDADEIRA UTILIZA O 'ALEATÓRIO' IMPORTADO DA BIBLIOTECA PARA PEGAR UM NÚMERO ALEATÓRIO
                    sorteio=randint(1,10)
                    #print(sorteio) UTILIZA O 'ESCREVAL' PARA MOSTRAR O NÚMERO PARA TESTE
                    #USO DO 'ESCREVAL'
                    print("Como promoção pela inauguração da loja, temos uma brincadeira:\nAdvinhe o número de 1 a 10 e ganhe um prêmio!")
                    #USO DO 'LEIA' PARA PEGAR O NÚMERO QUE O USUÁRIO DIGITAR
                    chute=int(input("Diga um número para tentar a sorte:"))
                    #USO DO 'SE' PARA COMPARAR O NÚMERO DIGITADO PELO USUÁRIO E O NÚMERO GERADO PELO SORTEIRO
                    if chute==sorteio:
                        #USO DO 'ESCREVAL'
                        print("O número sorteado foi:",sorteio)
                        print("Parabéns, você ganhou uma camisa exclusiva da loja!!!")
                    #USO DO 'SENÃO'
                    else:
                        print("Que pena, você não acertou!")
                    #USO DO 'BREAK' PARA ENCERRAR ESTE LOOP
                    break
            #USO DO 'ESCREVAL'
            print("Obrigado por comprar conosco e volte sempre")
            #USO DO BREAK PARA ENCERRAR O PROGRAMA
            break
        case 7:
            #USO DO 'ESCREVAL'
            print(catalogo[6])
            print("Obrigado por visitar nossa loja!!!")
            #FINALIZA O PROGRAMA USANDO O 'BREAK'
            break