# Arthur Gama Jorge - RA: 23578
# Ion Mateus Nunes Oprea - RA: 23135

class Somatoria:  # Cria classe somatória
    def __init__(self):                        # Declarar atributos da classe
        self._soma = 0.0                       # Float
        self._quantosValoresSomados = 0        # Int
        self._Inverso = 0.0                    # Float
        self.SomaInverso = 0.0                 # Float
        self.SomaPonderada = 0.0               # Float
        self.SomaPesoAleatorio = 0.0           # Float
        self.MaiorMedia = 0.0                  # Float
        self.MenorMedia = 10.0                 # Float

    @property
    def soma(self):                            # Retorna valor da soma
        return self._soma
    
    @soma.setter
    def soma(self, novoValor):                 # Recebe novo valor da soma e testa
        if self._soma < 0:     
            raise Exception("Não se pode ter nota negativa")  # Dispara exceção 
        
        self._soma = novoValor                 # Armazena se o valor for aceitável

    @property
    def quantos(self):
        return self._quantosValoresSomados     # Retorna valor da quantidade
    
    @quantos.setter
    def quantos(self, novoValor):              # Recebe novo valor da quantidade e testa
        if self._quantosValoresSomados <= 0:
            raise Exception("A quantidade não pode ser menor que 0")  # Dispara exceção
        
        self._quantosValoresSomados = novoValor # Armazena se o valor for aceitável

    @property
    def Inverso(self):                            # Retorna valor da soma
        return self._Inverso
    
    @soma.setter
    def Inverso(self, novoValor):                 # Recebe novo valor da soma e testa
        if novoValor <= 0:
            raise Exception("Não se pode dividir por 0 nem ter nota negativa")
        
        self._Inverso = novoValor                # Armazena se o valor for aceitável


    def somar(self, valorASomar : float):
        self.soma += valorASomar              # Somatoria
        self._quantosValoresSomados += 1       # Contagem
        
        if valorASomar > self.MaiorMedia:        #calcula se será a maior media, a menor ou nenhuma das duas
            self.MaiorMedia = valorASomar
        elif valorASomar < self.MenorMedia:
            self.MenorMedia = valorASomar
        
    def mediaAritmetica(self) -> float :
        return self._soma / self._quantosValoresSomados  # Calcula média aritimética

    def SomarInverso(self, Media):    # Classe somar inverso já que não foi permitido usar atributo soma
        self._quantosValoresSomados += 1
        self.Inverso = Media
        self.SomaInverso += self._Inverso
        self.MediaHarmonica = self._quantosValoresSomados / self.SomaInverso
    
    def SomarPonderado(self, media, pesoAleatorio):
        self.SomaPonderada += media * pesoAleatorio
        self.SomaPesoAleatorio += pesoAleatorio
        self.MediaPonderada = self.SomaPonderada / self.SomaPesoAleatorio
