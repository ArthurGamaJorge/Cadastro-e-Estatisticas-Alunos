# Arthur Gama Jorge - RA: 23578
# Ion Mateus Nunes Oprea - RA: 23135

import os
from tkinter import filedialog
from alu import Alunos
from soma import Somatoria
from produtorio import produtorio
from math import sqrt
import random

def Seletor():
    escolha = 1
    os.system('cls') or None
    print("Seja bem vindo(a)! ")
    print("------------------------")
    print("0. Terminar o programa")         # Opções exibidas
    print("1. Cadastro de Alunos")
    print("2. Listar Alunos cadastrados")
    print("3. Excluir Alunos")
    print("4. Estatísticas sobre os dados do arquivo")
    print("------------------------")
    
    while escolha == 1:

        escolha = input("Digite o número da opção que você deseja executar: ")
        
        match escolha:                      # Seletor
            case "0" : print("Programa encerrado!")
            case "1" : Cadastro()
            case "2" : ListarAlunos()
            case "3" : Excluir()
            case "4" : Estatisticas()
            case _:                          #Caso nenhuma opção válida for digitada
                print("Não existe essa opção. Digite novamente. ")
                escolha = 1
                
                
def Cadastro():
    print("Janela pode ter sido aberta atrás do console")
    tiposDeArquivos = (                  #Tipos de arquivos
        ("Arquivo de texto", "*.TXT"),
        ("Arquivo de dados", "*.DAT"),
        ("Outro tipo de arquivo", "*.*")
    )
    nomeDoArquivo = filedialog.askopenfilename(           #abrir caixa de seleção de arquivos
        title="Selecione o arquivo com os dados",
        initialdir=".",
        filetypes=tiposDeArquivos
    )

    if nomeDoArquivo != "":  # Se o arquivo foi escolhido
        arquivoSaida = open(nomeDoArquivo, "a")  # Abre arquivo no modo append (escreve na última linha)
        Classe = "1"
        UmAlu = Alunos()
        
        while Classe != "": 
            os.system('cls') or None   # Limpa a tela
            Escrever(1, 15, "Cadastro de alunos") 
            Escrever(3, 5, "Classe [max: 4 digitos ex: 1Inf, 3TA] (aperte apenas enter para encerrar): ")
            Classe = input()
            if Classe != "" :
                Escrever(5, 5, "RA do aluno (max: 5 digitos)   : ")
                RA = input()
                Escrever(6, 5, "Nome do aluno (max: 20 digitos): ")
                Nome = input()
                Escrever(7, 5, "Nota 1                         : ")
                Nota1 = float(input())
                Escrever(8, 5, "Nota 2                         : ")
                Nota2 = float(input()) 
                Escrever(9, 5, "Nota 3                         : ")
                Nota3 = float(input())
                Escrever(10, 5, "Nota 4                         : ")
                Nota4 = float(input())
                
                
                UmAlu.AtribuirDados(Classe, RA, Nome, Nota1, Nota2, Nota3, Nota4)  # Atribui as variáveis os inputs
                UmAlu.EscreverRegistro(arquivoSaida)  # Escreve no arquivo o cadastro feito

        arquivoSaida.close()  # fecha o arquivo de saída
      
    
def ListarAlunos():
    print("Janela pode ter sido aberta atrás do console")
    tiposDeArquivos = (                  #Tipos de arquivos
        ("Arquivo de texto", "*.TXT"),
        ("Arquivo de dados", "*.DAT"),
        ("Outro tipo de arquivo", "*.*")
    )
    nomeDoArquivo = filedialog.askopenfilename(           #abrir caixa de seleção de arquivos
        title="Selecione o arquivo com os dados",
        initialdir=".",
        filetypes=tiposDeArquivos
    )


    if nomeDoArquivo != "":   # Se o arqquivo foi escolhdio
        os.system(f'sort \"{nomeDoArquivo}\" /O ordenado.txt')  # Cria arquivo ordenado em ordem 
        arquivoEntrada = open("ordenado.txt", "r")   # Abre o arquivo ordenado em modo de leitura
        
        AprovadosClasse = Somatoria()  # Cria somatória 
        AprovadosGeral = Somatoria()
        RecuperacaoClasse= Somatoria()
        RecuperacaoGeral = Somatoria()
        RetidosClasse = Somatoria()
        RetidosGeral = Somatoria()
        SomaMediaClasse = Somatoria()
        SomaMediaGeral = Somatoria()
        ClasseAnt = "0"
        
        os.system('cls') or None
        print("Classe RA     Nome                  N1     N2     N3      N4     Média    Situação")  # Cabeçalho
        haregistro = True
        UmAlu = Alunos()
        while haregistro:   
            haregistro = UmAlu.LerRegistro(arquivoEntrada)
            if haregistro:  
                Media = (UmAlu.Nota1 + UmAlu.Nota2 + UmAlu.Nota3 + UmAlu.Nota4)/4  # Calcula a média individual
                
                  
                if ClasseAnt != UmAlu._Classe:  # Verifica se mudou de classe
                    if ClasseAnt != '0':  
                        print(f"{ClasseAnt}:")
                        MediaClasse = SomaMediaClasse.mediaAritmetica()  # Calcula a média da classe
                        print(f"Totais: {SomaMediaClasse.quantos} alunos; Media Geral: {MediaClasse:4.2f} Aprovados: {AprovadosClasse.quantos} Recuperação: {RecuperacaoClasse.quantos} Retidos: {RetidosClasse.quantos}\n")
                        SomaMediaClasse = Somatoria()   # Reseta valor da soma e contador
                        AprovadosClasse = Somatoria()
                        RecuperacaoClasse= Somatoria()
                        RetidosClasse = Somatoria()

                SomaMediaClasse.somar(Media)  # Adiciona o valor da média na soma e incrementa o contador
                SomaMediaGeral.somar(Media)
                
                if SomaMediaClasse.quantos == 21:  # Se haver mais de 20 alunos na mesma classe ativar input antes de dar print no resto
                    input("Aperte [Enter] para continuar")

                ClasseAnt = UmAlu._Classe  # Muda classe anterior
                    
                if Media >= 5:  # Calcula quantidade de pessoas em cada situação
                    Situacao = "Aprovado"
                    AprovadosClasse.somar(1)
                    AprovadosGeral.somar(1)
                elif Media < 3:
                    Situacao = "Retido"
                    RetidosClasse.somar(1)
                    RetidosGeral.somar(1)
                elif Media >= 3:
                    Situacao = "Recuperação"
                    RecuperacaoClasse.somar(1)
                    RecuperacaoGeral.somar(1)    
                    
                print(f"{UmAlu._Classe}   {UmAlu._RA}  {UmAlu._Nome}  {UmAlu.Nota1:4.1f}   {UmAlu.Nota2:4.1f}   {UmAlu.Nota3:4.1f}   {UmAlu.Nota4:5.1f}   {Media:5.2f}    {Situacao} ")
        
        #Exibe resultados da última classe
        MediaClasse = SomaMediaClasse.mediaAritmetica()
        print(f"{ClasseAnt}:")
        print(f"Totais: {SomaMediaClasse.quantos} alunos; Media Geral: {MediaClasse:4.2f} Aprovados: {AprovadosClasse.quantos} Recuperação: {RecuperacaoClasse.quantos} Retidos: {RetidosClasse.quantos}\n")       
       
        #Exibe resultados gerais
        MediaGeral = SomaMediaGeral.mediaAritmetica()
        print("Geral:")
        print(f"Totais: {SomaMediaGeral.quantos} alunos; Media Geral: {MediaGeral:4.2f} Aprovados: {AprovadosGeral.quantos} Recuperação: {RecuperacaoGeral.quantos} Retidos: {RetidosGeral.quantos}")
                
    arquivoEntrada.close()  # Fecha arquivo de entrada
    
      
def Excluir():
    print("Janela pode ter sido aberta atrás do console")
    tiposDeArquivos = (                  #Tipos de arquivos
        ("Arquivo de texto", "*.TXT"),
        ("Arquivo de dados", "*.DAT"),
        ("Outro tipo de arquivo", "*.*")
    )
    
    nomeDoArquivo = filedialog.askopenfilename(           #abrir caixa de seleção de arquivos
        title="Selecione o arquivo com os dados",
        initialdir=".",
        filetypes=tiposDeArquivos
    )
    
    if nomeDoArquivo != "":  # Se o arquivo foi aberto
        ArquivoEntrada = open(nomeDoArquivo, "r")  # Abre o arquivo em modo de leitura
        ArquivoSaida = open("temporário.txt", "w")
        
        os.system('cls') or None
        RAexcluir = input("Digite o RA do aluno que deseja excluir o cadastro: ")
        UmAlu = Alunos()
        haregistros = True
        
        while haregistros:
            haregistros = UmAlu.ExcluirCadastro(ArquivoEntrada, RAexcluir)
            if haregistros:
                if UmAlu._RA != "":  # Se foi lido o RA que se deseja apagar
                    UmAlu.EscreverRegistro(ArquivoSaida)  # Escreve no arquivo de saída
            
        ArquivoEntrada.close()
        ArquivoSaida.close()
        
        os.remove(nomeDoArquivo)
        os.rename("temporário.txt", nomeDoArquivo)
        
        
def Estatisticas():
    print("Janela pode ter sido aberta atrás do console")
    tiposDeArquivos = (  # Tipos de arquivos
        ("Arquivo de texto", "*.TXT"),
        ("Arquivo de dados", "*.DAT"),
        ("Outro tipo de arquivo", "*.*")
    )

    nomeDoArquivo = filedialog.askopenfilename(  # abrir caixa de seleção de arquivos
        title="Selecione o arquivo com os dados",
        initialdir=".",
        filetypes=tiposDeArquivos
    )

    if nomeDoArquivo != "":      # se não se pressionou [Cancelar]
        arquivoDeEntrada = open(nomeDoArquivo, "r")     #abre o arquivo com os dados em modo leitura

        UmAlu = Alunos()
        Media = Somatoria()
        SomaElevadaQuadrado = Somatoria()     #Cria somatoria
        MediaPonderada = Somatoria()
        MediaGeometrica = produtorio()
        MediaHarmonica = Somatoria()

        os.system('cls') or None
        haRegistro = True
        while haRegistro:
            haRegistro = UmAlu.LerRegistro(arquivoDeEntrada)    # atualiza a variavel de verificação de registros
            if haRegistro:                                      # verifica se tem um registro
                
                CalcularMedia = (UmAlu.Nota1 + UmAlu.Nota2 + UmAlu.Nota3 + UmAlu.Nota4)/4
                Media.somar(CalcularMedia)                                # calcula a media do aluno
                SomaElevadaQuadrado.somar(CalcularMedia**2)               # atribui os valores na somatoria
                pesoAleatorio = random.randint(1, 5)
                MediaPonderada.SomarPonderado(CalcularMedia, pesoAleatorio)
                MediaGeometrica.multiplicar(CalcularMedia)      # atribui os valores no produtorio
                MediaHarmonica.SomarInverso(1/CalcularMedia)


        RMQ = sqrt(SomaElevadaQuadrado._soma/SomaElevadaQuadrado.quantos)     # calcula a RMQ

        print("-"*60)       # prints dos resultados
        print(f"Estatisticas dos alunos:\n")
        print(f"Raiz Média Quadrática:           {RMQ:2.3f}")
        print(f"Média ponderada das N médias:    {MediaPonderada.MediaPonderada:2.3f}")
        print(f"Média geométrica:                {MediaGeometrica.MediaGeometrica:2.3f}")
        print(f"Média harmônica:                 {MediaHarmonica.MediaHarmonica:2.3f}")
        print(f"Maior média calculada:           {Media.MaiorMedia:2.2f}")
        print(f"Menor média calculada:           {Media.MenorMedia:2.2f}")
        print("-"*60)
        arquivoDeEntrada.close()
        
          
def Escrever(linha, coluna, texto):   # Formata escritura de modo correto
    print(f"\033[{linha};{coluna}H", end="")
    print(f'{texto}', end="")
    
    
if __name__=="__main__":
    Seletor()