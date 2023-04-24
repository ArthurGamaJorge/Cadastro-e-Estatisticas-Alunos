# Arthur Gama Jorge - RA: 23578
# Ion Mateus Nunes Oprea - RA: 23135

class produtorio : # Cria classe produtorio
    
    def __init__(self):                                                 # Declarar atributos da classe
        self._produto = 1.0                                             # Float
        self._QuantosValoresMultiplicados = 0                           # Inteiro
        self.MediaGeometrica = 0.0                                      # Float


    @property
    def produto(self):                                                  # Retorna atributo do produto
        return self._produto

    @produto.setter                                                     # Recebe novo valor do produto e o testa
    def produto(self, novoValor):
        if self._produto < 0:                                                                       
            raise Exception("Nota não pode ser negativa")               # Dispara exceção 
        
        self._produto = novoValor                                       # Armazena se o valor for aceitável

    @property
    def quantos(self):                              # Retorna atributo do QuantosValoresMultiplicados
         return self._QuantosValoresMultiplicados
    
    @quantos.setter                                 # Recebe novo valor do QuantosValoresMultiplicados e o testa
    def quantos(self, novoValor):                  
        if self._QuantosValoresMultiplicados <= 0:                    
            raise Exception("A quantidade não pode ser menor que 0")       # Dispara exceção
        
        self._QuantosValoresMultiplicados = novoValor                   # Armazena se o valor for aceitável
         
        
    def multiplicar(self, valorAMultiplicar):
        self._QuantosValoresMultiplicados += 1                          # Contagem 
        self._produto = self._produto * valorAMultiplicar               # Produtório
        
        self.MediaGeometrica = self._produto ** (1/self._QuantosValoresMultiplicados) # Calcula valor da média geométrica

