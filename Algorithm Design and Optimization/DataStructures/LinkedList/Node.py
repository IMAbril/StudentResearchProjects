class Node:
    """
    [ENG] Base class to represent a node in a linked list.
    Compatible with singly linked lists, doubly linked lists, and circular linked lists.

    [ESP] Clase base para representar un nodo en una lista enlazada.
    Compatible con listas simplemente enlazadas, doblemente enlazadas y circulares.
    """
    
    def __init__(self, data):
        """
        [ENG] Initializes a node with a value and a reference to the previous and next nodes.
        [ESP] Inicializa un nodo con un valor y una referencia al nodo previo y al siguiente.

        :param data: The value stored in the node. / El valor almacenado en el nodo.
        """

        self.value = data
        self.next = None  # Points to the next node (for singly and circular linked lists).
                          # Apunta al siguiente nodo (para listas simplemente enlazadas y circulares).
        self.prev = None  # Points to the previous node (for doubly linked lists).
                          # Apunta al nodo previo (para listas doblemente enlazadas).
    
    def __repr__(self):
        """
        [ENG] Returns a string representation of the node.
        
        [ESP] Retorna una representación en cadena del nodo.

        :return: A string with the node's data. / Una cadena con los datos del nodo.
        """
        return f"Node({self.data})"

