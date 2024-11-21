from lib.binary_search_tree import BinarySearchTree

abb = BinarySearchTree()

abb.insert(28)
abb.insert(39)
abb.insert(18)
abb.insert(32)
abb.insert(35)
abb.insert(27)

# Percurso em-ordem
# print é a função (action) que será executada quando
# o percurso visitar o nó raiz
print('Em-ordem:')
abb.in_order_traversal(print)
print("-" *80)

print('Pré-ordem:')
abb.pre_order_traversal(print)
print("-" *80)

print('Pós-ordem:')
abb.post_order_traversal(print)
print("-" *80)