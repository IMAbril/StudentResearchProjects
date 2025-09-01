from BaseLinkedList import BaseLinkedList
from Node import Node

class DoublyLinkedList(BaseLinkedList):
    """
    [ENG] Implementation of a doubly linked list.
    Each node has references to both the next and previous nodes.

    [ESP] Implementación de una lista doblemente enlazada.
    Cada nodo tiene referencias tanto al siguiente como al anterior.
    """

    def insert(self, data):
        """
        [ENG] Inserts a new node with the given data at the end of the list.

        [ESP] Inserta un nuevo nodo con los datos proporcionados al final de la lista.

        :param data: The value to store in the new node. / El valor a almacenar en el nuevo nodo.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.tail = new_node
            new_node.prev = current  # Link back to the previous node
        self.size += 1
    
    def insert_at_position(self, data, position):
        """
        [ENG] Inserts a new node at a specified position in the doubly linked list.

        [ESP] Inserta un nuevo nodo en una posición específica de la lista doblemente enlazada.

        :param data: The value to store in the new node. / El valor a almacenar en el nuevo nodo.
        :param position: The index where the new node will be inserted (0-based). / El índice donde se insertará el nuevo nodo (basado en 0).
        """
        if position < 0 or position > self.size:
            raise IndexError("Invalid position / Posición inválida")

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            new_node.prev = current
            current.next = new_node

        self.size += 1

    def reverse(self):
        """
        [ENG] Reverses the doubly linked list.

        [ESP] Invierte la lista doblemente enlazada.
        """
        current = self.head
        prev = None

        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev  # Move to the next node (previously next)

        if prev:
            self.head = prev.prev  # Update head to new first node

    def delete(self, data):
        """
        [ENG] Deletes the first occurrence of a node containing the given data.

        [ESP] Elimina la primera aparición de un nodo que contiene los datos proporcionados.

        :param data: The data to search and remove from the list. / Los datos a buscar y eliminar de la lista.
        """
        if self.is_empty():
            return
        
        if self.head.value == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None  # Update previous reference
            self.size -= 1
            return

        current = self.head
        while current and current.value != data:
            current = current.next

        if current:
            if current.next:
                current.next.prev = current.prev  # Link next node to previous node
            if current.prev:
                current.prev.next = current.next  # Link previous node to next node
            self.size -= 1

    def delete_at_position(self, position):
        """
        [ENG] Deletes a node at a specific position.

        [ESP] Elimina un node en una posición específica.

        :param position: The index where the node will be removed (0-based). / El índice donde se eliminará el nodo (basado en 0).

        """
        if not self.head:
            return

        if position == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # If list becomes empty
            return

        current = self.head
        for _ in range(position):
            if not current.next:
                return  # Position out of bounds
            current = current.next

        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev  # Update tail if needed

    def search(self, data):
        """
        [ENG] Searches for a node containing the given data.

        [ESP] Busca un nodo que contiene los datos proporcionados.

        :param data: The data to search for. / Los datos a buscar.
        :return: The node if found, otherwise None. / El nodo si se encuentra, de lo contrario None.
        """
        current = self.head
        while current:
            if current.value == data:
                return current
            current = current.next
        raise ValueError(str(data) + " is not in the list")
    
    def recursive_search(self, data):
        """
        [ENG] Searches for a node containing the given data with a recursive implementation.

        [ESP] Busca un nodo que contiene los datos proporcionados con una implementación recursiva.

        :param data: The data to search for. / Los datos a buscar.
        :return: The node if found, otherwise None. / El nodo si se encuentra, de lo contrario None.
        """        

        def recursive_search_inner_func(node, data):
            """
            [ENG] Recursively searches for the node containing the given data.
            [ESP] Busca recursivamente el nodo que contiene los datos proporcionados.

            :param node: The current node being checked. / El nodo actual que se está verificando.
            :param data: The data to search for. / Los datos a buscar.
            :return: The node if found, otherwise raises ValueError. / El nodo si se encuentra, de lo contrario lanza ValueError.
            """
            if node is None:
                raise ValueError(f"{data} is not in the list.")  # Base case: Not found
            if node.value is data:
                return node  # Base case: Found
            return recursive_search_inner_func(node.next, data)  # Recursive call
   
        return recursive_search_inner_func(self.head, data)  # Start from the head
    
    def display(self):
        """
        [ENG] Displays the elements of the linked list in forward order.

        [ESP] Muestra los elementos de la lista enlazada en orden ascendente.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements) + " <-> None")

    def display_backward(self):
        """
        [ENG] Displays the elements of the linked list in reverse order.

        [ESP] Muestra los elementos de la lista enlazada en orden descendente.
        """
        elements = []
        current = self.head
        if not current:
            print("None")
            return

        while current.next:  # Move to the last node
            current = current.next

        while current:  # Traverse backward
            elements.append(str(current.value))
            current = current.prev
        print(" <-> ".join(elements) + " <-> None")
