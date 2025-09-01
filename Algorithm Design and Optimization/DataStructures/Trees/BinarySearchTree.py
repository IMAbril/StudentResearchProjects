import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
from BSTNode import BSTNode
from matplotlib import pyplot as plt

class BST:
    """
    [ENG] Binary search tree data structure class.
    The root attribute references the first node in the tree.
    
    [ESP]
    """
    def __init__(self):
        """ 
        [ENG] Initialize the root attribute.
        
        [ESP] Inicializa el atributo raíz.
        """
        self.root = None

    def search(self, data):
        """
        [ENG] Return the node containing the data. If there is no such node
        in the tree, including if the tree is empty, raise a ValueError.
        
        [ESP]
        """

        # Define a recursive function to traverse the tree.
        def _step(current):
            """
            [ENG] Recursively step through the tree until the node containing
            the data is found. If there is no such node, raise a Value Error.
            
            [ESP] 
 
            """
            if current is None:                     # Base case 1: dead end.
                raise ValueError(str(data) + " is not in the tree.")
            if data == current.value:               # Base case 2: data found!
                return current
            if data < current.value:                # Recursively search left.
                return _step(current.left)
            else:                                   # Recursively search right.
                return _step(current.right)

        # Start the recursion on the root of the tree.
        return _step(self.root)

def insert(self, data):
    """
    [ENG] Insert a new node containing the specified data.
    
    [ESP] Inserta un nuevo nodo con el dato especificado.

    :param data: /El valor a insertar en el árbol.
    :raises ValueError: /si el valor ya está en el árbol.
    """

    def _insert_recursively(node, data):
        """ 
        [ENG]

        [ESP]
        """
        if data == node.value:
            raise ValueError(f"{data} is already in the tree.")
        elif data < node.value:
            if node.left is None:
                node.left = BSTNode(data)
                node.left.prev = node  
            else:
                _insert_recursively(node.left, data)
        else:
            if node.right is None:
                node.right = BSTNode(data)
                node.right.prev = node 
            else:
                _insert_recursively(node.right, data)

    if self.root is None:
        self.root = BSTNode(data)
    else:
        _insert_recursively(self.root, data)

def remove(self, data):
    """
        [ENG] Remove the node containing the specified data.

        [ESP] 

        :param data: 
        
        Raises:
            ValueError: if there is no node containing the data, including if
                the tree is empty.

        Examples:
            >>> print(12)                       | >>> print(t3)
            [6]                                 | [5]
            [4, 8]                              | [3, 6]
            [1, 5, 7, 10]                       | [1, 4, 7]
            [3, 9]                              | [8]
            >>> for x in [7, 10, 1, 4, 3]:      | >>> for x in [8, 6, 3, 5]:
            ...     t1.remove(x)                | ...     t3.remove(x)
            ...                                 | ...
            >>> print(t1)                       | >>> print(t3)
            [6]                                 | [4]
            [5, 8]                              | [1, 7]
            [9]                                 |
                                                | >>> print(t4)
            >>> print(t2)                       | [5]
            [2]                                 | >>> t4.remove(1)
            [1, 3]                              | ValueError: <message>
            >>> for x in [2, 1, 3]:             | >>> t4.remove(5)
            ...     t2.remove(x)                | >>> print(t4)
            ...                                 | []
            >>> print(t2)                       | >>> t4.remove(5)
            []                                  | ValueError: <message>
    """


    def __str__(self):
        """String representation: a hierarchical view of the BST.

        Example:  (3)
                  / \     '[3]          The nodes of the BST are printed
                (2) (5)    [2, 5]       by depth levels. Edges and empty
                /   / \    [1, 4, 6]'   nodes are not printed.
              (1) (4) (6)
        """
        if self.root is None:                       # Empty tree
            return "[]"
        out, current_level = [], [self.root]        # Nonempty tree
        while current_level:
            next_level, values = [], []
            for node in current_level:
                values.append(node.value)
                for child in [node.left, node.right]:
                    if child is not None:
                        next_level.append(child)
            out.append(values)
            current_level = next_level
        return "\n".join([str(x) for x in out])

    def draw(self):
        """Use NetworkX and Matplotlib to visualize the tree."""
        if self.root is None:
            return

        # Build the directed graph.
        G = nx.DiGraph()
        G.add_node(self.root.value)
        nodes = [self.root]
        while nodes:
            current = nodes.pop(0)
            for child in [current.left, current.right]:
                if child is not None:
                    G.add_edge(current.value, child.value)
                    nodes.append(child)

        # Plot the graph. This requires graphviz_layout (pygraphviz).
        nx.draw(G, pos=graphviz_layout(G, prog="dot"), arrows=True,
                with_labels=True, node_color="C1", font_size=8)
        plt.show()
