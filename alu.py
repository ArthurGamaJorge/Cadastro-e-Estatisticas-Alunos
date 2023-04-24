# Arthur Gama Jorge - RA: 23578
# Ion Mateus Nunes Oprea - RA: 23135

class Alunos:
    global iniClasse, iniRA, iniNome, iniNota1, iniNota2, iniNota3, iniNota4
    global fimClasse, fimRA, fimNome, fimNota1, fimNota2, fimNota3, fimNota4
    global tamClasse, tamRA, tamNome, tamNota1, tamNota2, tamNota3, tamNota4

    tamClasse = 4
    tamRA = 5
    tamNome = 20
    tamNota = 4

    iniClasse = 0 
    fimClasse = iniClasse + tamClasse - 1
    iniRA = fimClasse + 1
    fimRA = iniRA + tamRA - 1
    iniNome = fimRA + 1
    fimNome = iniNome + tamNome - 1
    iniNota1 = fimNome + 1
    fimNota1 = iniNota1 + tamNota -1 
    iniNota2 = fimNota1 + 1
    fimNota2 = iniNota2 + tamNota - 1
    iniNota3 = fimNota2 + 1
    fimNota3 = iniNota3 + tamNota - 1
    iniNota4 = fimNota3 + 1
    fimNota4 = iniNota4 + tamNota - 1

    def __init__(self):                            # Declarar atributos da classe
        self._Classe = " "                         # String
        self._RA = " "                             # String
        self._Nome = " "                           # String
        self._Nota1 = 0.0                          # Float 
        self._Nota2 = 0.0                          # Float 
        self._Nota3 = 0.0                          # Float 
        self._Nota4 = 0.0                          # Float 

    @property 
    def Classe(self):                              # Retorna o valor da classe
        return self._Classe
    
    @Classe.setter
    def Classe(self, novoValor):                   # Recebe e testa o valor da classe
        self._Classe=novoValor.ljust(tamClasse,' ')[0:tamClasse] # Ajusta tamanho da classe

    @property 
    def RA(self):
        return self._RA
    
    @RA.setter
    def RA(self, novoValor):
        if novoValor == "":
            raise Exception("RA não pode ser vazio")
        self._RA=novoValor.ljust(tamRA,'0')[0:tamRA]

    @property 
    def Nome(self):
        return self._Nome
    
    @Nome.setter
    def Nome(self, novoValor):
        if novoValor == "":
            raise Exception("Nome não pode ser vazio")
        self._Nome=novoValor.ljust(tamNome,' ')[0:tamNome]

    @property
    def Nota1(self):
        return self._Nota1                        # Retorna valor da nota 1
    
    @Nota1.setter 
    def Nota1(self, novoValor):                   # Recebe e testa o valor da nota 1
        if novoValor < 0 or novoValor > 10:
            raise Exception("Nota deve estar entre 0 e 10")  # Dispara exceção
        
        self._Nota1 = novoValor                   # Armazena o valor caso válido

    @property
    def Nota2(self):
        return self._Nota2
    
    @Nota2.setter
    def Nota2(self, novoValor):
        if novoValor < 0 or novoValor > 10:
            raise Exception("Nota deve estar entre 0 e 10")
        
        self._Nota2 = novoValor

    @property
    def Nota3(self):
        return self._Nota3
    
    @Nota3.setter
    def Nota3(self, novoValor):
        if novoValor < 0 or novoValor > 10:
            raise Exception("Nota deve estar entre 0 e 10")
        
        self._Nota3 = novoValor

    @property
    def Nota4(self):
        return self._Nota4
    
    @Nota4.setter
    def Nota4(self, novoValor):
        if novoValor < 0 or novoValor > 10:
            raise Exception("Nota deve estar entre 0 e 10")
        
        self._Nota4 = novoValor

    def LerRegistro(self, arquivo):
        if arquivo != None:   # Caso o arquivo tenha sido aberto
            dados = arquivo.readline()   # Lê uma linha do arquivo
            if dados != "":   # Caso a linha não seja vazia
                self.Classe = dados[iniClasse:fimClasse+1]  # Atribui os dados às variáveis
                self.RA = dados[iniRA:fimRA+1]
                self.Nome = dados[iniNome:fimNome+1]
                self.Nota1 = float(dados[iniNota1:fimNota1+1])
                self.Nota2 = float(dados[iniNota2:fimNota2+1])
                self.Nota3 = float(dados[iniNota3:fimNota3+1])
                self.Nota4 = float(dados[iniNota4:])
                return True
            return False
        
    def AtribuirDados(self, Classe, RA, Nome, Nota1, Nota2, Nota3, Nota4): # Atribui dados no cadastro
        self.Classe = Classe
        self.RA = RA
        self.Nome = Nome
        self.Nota1 = Nota1
        self.Nota2 = Nota2
        self.Nota3 = Nota3
        self.Nota4 = Nota4

    def ParaArquivo(self): # Formatar para o arquivo de saída
        return f"{self.Classe:}{self.RA}{self.Nome}{self.Nota1:4.1f}{self.Nota2:4.1f}{self.Nota3:4.1f}{self.Nota4:4.1f}\n"
    
    def EscreverRegistro(self, saida):
        if saida != None:    # Se o arquivo de saida foi aberto
            saida.write(self.ParaArquivo())  # Escreve no arquivo
        else: 
            raise Exception("Arquivo de saída não foi aberto")  # Dispara exceção

    def ExcluirCadastro(self, arquivo, RA):
        if arquivo != None:  # Arquivo foi abertos
            dados = arquivo.readline()  # Le uma linha 
            if dados != "":
                self.RA = dados[iniRA:fimRA+1]
                if self._RA != RA:
                    self.Classe = dados[iniClasse:fimClasse+1]
                    self.Nome = dados[iniNome:fimNome+1]
                    self.Nota1 = float(dados[iniNota1:fimNota1+1])
                    self.Nota2 = float(dados[iniNota2:fimNota2+1])
                    self.Nota3 = float(dados[iniNota3:fimNota3+1])
                    self.Nota4 = float(dados[iniNota4:])
                    return True
                self._RA = ""
                return True
        return False
