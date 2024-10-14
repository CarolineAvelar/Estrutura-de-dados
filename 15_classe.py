"""
Classe é uma estrutura que representa cpnjuntamente dados e
algoritmos. Uma classe pode ser comparado a uma "assadeira",
com a qual se pode produzir diferentes tiós de "assados",
variando os "ingrefientes" (dados) da receita e o "modo de
fazer" (algoritmos). Apesar dessas variações, todos os objetos 
criados a partir de uma mesma classe terão sempre algumas
características comuns, impostas por ela.
"""
from math import pi

class FormaGeometrica:
    """
    Por convenção, nomes de classe seguem o formato PascalCase
    (primeira lletra de cada palavra em maiusculo).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, representando os algoritmos). Uma função especial,
    chamada __init__, é chamada sempre que se tenta riar um novo objeto
    a partir de uma classe. Essa função especial é chamada de CONSTRUTOR
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas MÉTODOS; seu primeiro parâmetro
        é sempre self, representando o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """
    
def _init_(self, base, altura, tipo):
        """ Método Construtor """
        self.set_base(base)
        self.set_altura(altura)
        self.set_tipo(tipo)
    
def set_base(self, val):
    """Métodos Setter para o Atributo __base"""
    # Valida se a base é numérica e maior que zero
    if type(val) not in [int, float] or val <= 0:
        raise Exception("ERRO: 'base' deve ser numérica e maior que zero.")
        
        # Sobreviveu a validação, armazena val no atributo
        self.__base = val
    # Métodos Setter para o Atributo __altura
def set_altura(self, val):
    # Valida se a altura é numérica e maior que zero
    if type(val) not in [int, float] or val <= 0:
        raise Exception ("ERRO: 'altura' deve ser numérica e maior que zero.")
    # Sobreviveu a validação, armazena val no atributo
    self.__altura = val

    # Métodos Setter para o Atributo __tipo
def set_tipo(self, val):
    # Valida o tipo de forma
    if val not in["R", "T", "E"]:
        raise Exception ("ERRO: 'tipo' deve ser 'R', 'T' ou 'E'.")
    # Sobreviveu a validação, armazena val no atributo
    self.__tipo = val

def get_base(self):
    """ Método getter para o atributo __base """
    return self.__base
    
def get_altura(self):
    """ Método getter para o atributo __altura """
    return self.__altura
    
def get_tipo(self):
    """ Método getter para o atributo __tipo """
    return self.__tipo

def calc_area(self):
    """ Método que calcula a area da forma geométrica a partir
        do valor dos atributos __base, __altura e __tipo
    """
    if self.__tipo == "R":
        return self.__base * self.__altura
    elif self.__tipo == "T":
        return self.__base * self.__altura / 2
    else:
        return (self.__base / 2) * (self.__altura / 2) * pi
    
def __str__(self):
    """Prove uma representação do objeto com string"""
    return f"[FormaGeometrica] base: {self.__base}, altura: {self.__altura}, tipo: {self.__tipo}, área: {self.calc_area()}"    


####################################################################################################################

# Criando uma forma geométrica a partir da classe
forma1 = FormaGeometrica(20, 12.5, "R")

# Nesse ponto, o objeto já existe, podemos modificar seus atributos
# forma1.base = "tomate"
# forma1.altura = -7
# forma1.tipo = "W"
forma1.set_base(4.5)
forma1.set_altura(12)
forma1.set_tipo("E")


print(f"Dados da forma1: base = {forma1.get_base()}, altura = {forma1.get_altura()}, tipo = {forma1.get_tipo()}, área = {forma1.calc_area()}")    