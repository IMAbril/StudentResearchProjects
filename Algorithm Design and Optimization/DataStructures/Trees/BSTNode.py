class BSTNode:
    """
    [ENG] A node class for binary search trees. Contains a value, a
    reference to the parent node, and references to two child nodes.
    
    [ESP] Una clase Nodo para árboles binarios de búsqueda. Contiene un valor,
    una referencia al nodo padre y referencias a dos nodos hijos.
    """
    def __init__(self, data):
        """
        [ENG] Construct a new node and set the value attribute. The other
        attributes will be set when the node is added to a tree.
        
        [ESP] Construye un nuevo nodo y establece el atributo de valor. 
        Los demás atributos se establecerán cuando el nodo se añada a un árbol.

        :param data:  The value stored in the node. / El valor almacenado en el nodo. 
        """
        self.value = data
        self.prev = None        # A reference to this node's parent node.
        self.left = None        # self.left.value < self.value
        self.right = None       # self.value < self.right.value

    def __repr__(self):
        """
        [ENG] Returns a string representation of the node.
        
        [ESP] Retorna una representación en cadena del nodo.

        :return: A string with the node's data. / Una cadena con los datos del nodo.
        """
        return f"BSTNode({self.value})"
