"""
DICIONÁRIO é uma estrutura de dados nativa da linguagem Python capaz de armazenar múltiplos valores em uma
única variável, por meio de pares de chave-valor (key-value).
Um dicionário é delimitado por chaves {}. Diferentemente da lista, que tem posições numeradas, o dicionário
possui posições NOMEADAS. Cada uma das posições nomeadas de um dicionário (ou seja, cada par de chave-valor)
é chamada de PROPRIEDADE.
"""

pessoa = {
    # "chave": valor
    "nome": "Orozimbo Oliveira Osório",
    "sexo": "M",
    "idade": 72,
    "peso": 76,
    "altura": 1.66,
    "aposentado": True,
    "filhos": ["Zeferino", "Adamastor", "Gercina"]
}

# Acessando o valor das prioridades
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Aposentado?", pessoa["aposentado"])

print("-" *80)

# Calculando o IMC (Indice de massa corporal)
imc = pessoa["peso"] / pessoa["altura"] ** 2

# Nas f-strings delimitadas por aspas duplas, é necessário usar
# aspas simples nos nomes das proriedades, e vice-versa
print(f"O IMC de {pessoa['nome']} é {imc}")

################################################################################

# Usando dicionários para representar formas geométricas

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     # Retangulo
}

forma2 = {
    "base": 6,
    "altura": 3,
    "tipo": "T"     #Trianglo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     # Elipse/Circulo
}    

forma4 = {
    "legume": 10,
    "fruta": 6.2,
    "tipo": "T"     # Elipse/Circulo
}

forma5 = {
    "base": "batata",
    "altura": False,
    "tipo": "E"     # Elipse/Circulo
}

from math import pi

def calc_area(forma):
    """
    Funças que calcula a área de uma forma geométrica, 
    dados a base, altura, e o tipo passado dentro de um dicionário
    """
    match forma["tipo"]:
        case "R":   # Retangulo
            return forma["base"] * forma["altura"]
        case "T":   # Triangulo
            return forma["base"] * forma["altura"] / 2
        case "E":   # Elipse/Circulo
            return (forma["base"] / 2) * (forma["altura"] / 2) * pi
        
        case _: # Forma Inválida
            return None
        
print("-" *80)

# Testes com a função calc_area()

print(f"Base: {forma1['base']}; altura: {forma1['altura']}; tipo: {forma1['tipo']}; área: {calc_area(forma1)}")       
print(f"Base: {forma2['base']}; altura: {forma2['altura']}; tipo: {forma2['tipo']}; área: {calc_area(forma2)}")       
print(f"Base: {forma3['base']}; altura: {forma3['altura']}; tipo: {forma3['tipo']}; área: {calc_area(forma3)}")   
#print(f"Base: {forma4['base']}; altura: {forma4['altura']}; tipo: {forma4['tipo']}; área: {calc_area(forma4)}")       
#print(f"Base: {forma5['base']}; altura: {forma5['altura']}; tipo: {forma5['tipo']}; área: {calc_area(forma5)}")           