from dataclasses import dataclass

class DoublyLinkedList:
    """
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos
    (chamados nodos ou nós) não estão fisicamente adjacentes
    uns dos outros, mas ligados de forma lógica por ponteiros
    que indicam o nodo anterior e nodo seguinte da 
    sequência. Não possui restrição de acesso: inserções,
    exclusões e consultas podem ser executadas em qualquer
    posição da lista.
    """
    #-----------------------------------------------------
    @dataclass
    class Node:
        """
        Classe interna que tem somente dados (por isso, o
        decorator @dataclass), representando uma unidade
        de informação armazenada pela lista duplamente 
        encadeada
        """
        prev: int | None = None
        data: any   # Qualquer tipo de dado
        next: int | None = None
    #------------------------------------------------------------------------------

    def __init__(self):
        """ Construtor da classe principal DoublyLinkedList """
        self.__head = None  # Ponteiro para o primeiro nodo da lista
        self.__tail = None  # Ponteiro para o último nodo da lista
        self.__count = 0     # Qunatidade de nodos da lista
    
    def __find_node(self, pos):
        """
        Método PRIVADO que encontra um nodo na posição especificada
        """
        # 1° caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2° caso: posição final (self.__count - 1)
        if pos == self.__count - 1: return self.__tail

        # 3° caso: posição intermediária

        # Se 'pos' estiver na primeira metade da lista,
        # faz o percurso a partir de self.__head, seguindo
        # o ponteiro next
        if pos <= self.__count // 2:
            node = self.__head
            for _ in range(1, pos + 1): node = node.next
            return node
        
        # Se não, a posição estando na segunda metade da lista
        # faz o percurso reverso a partir de self.__tail,
        # usando o ponteiro prev
        else:
            node = self.__tail
            for _ in range(self.__count - 2, pos -1, -1):
                node = node.prev
            return node    

    def insert(self, pos, val):
        """
        Método que insere na posição 'pos' o valor 'val' 
        """
        # Se a posição passada for negativa, emite um erro
        if pos < 0:
            raise Exception("ERRO: posição não pode ser negativa")
        
        # Criamos um novo nodo para armazenar 'val' e também
        # os ponteiros 'prev' e 'next', ambos apontando
        # inicialmente para None
        new = self.Node(data = val)

        # 1° caso: a lista está vazia, e 'new' será, ao mesmo tempo
        # tanto o primeiro quanto o último nodo
        if self.__count == 0:
            self.__head = new
            self.__tail = new

        # 2° caso: inserção no início da lista (posição 0)
        elif pos == 0:
            new.next = self.__head
            self.__head.prev = new
            self.__head = new

        # 3° caso: inserção no final da lista
        # OBS.: consideramos como posição final da lista
        # qualquer uma que seja >= self.__cont
        elif pos >= self.__count:
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new

        # 4° caso: inserção em posição intermediária
        # Não temos acesso direto às posições intermediárias.
        # Para encontrá-la, precisamos partir de uma das
        # extremidades (__head ou __tail) e percorrer a lista
        # até encontrar o nodo que, atualmente, ocupa a 
        # posição onde o novo nodo será inserido. Essa busca
        # será feita por outro método (acima), ___find_node()
        else:
            # Busca o nodo que atualmente ocupa a
            # posição de inserção 
            current = self.__find_node(pos)
            # Determina o nodo anterior à posição
            before = current.prev
            # Efetua o encaixe do novo nodo na sequência
            before.next = new
            new.prev = before
            new.next = current
            current.prev = new  

        self.__count += 1    