from BaseLinkedList import BaseLinkedList
from Node import Node

class SinglyLinkedList(BaseLinkedList):
    """
    [ENG] Implementation of a singly linked list.
    Each node has a reference to the next node, but not the previous one.

    [ESP] Implementación de una lista simplemente enlazada.
    Cada nodo tiene una referencia al siguiente nodo, pero no al anterior.
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
        self.size += 1

    def insert_at_position(self, data, position):
        """
        [ENG] Inserts a new node at a specified position.

        [ESP] Inserta un nuevo nodo en una posición específica de la lista enlazada simple.

        :param data: The value to store in the new node. / El valor a almacenar en el nuevo nodo.
        :param position: The index where the new node will be inserted (0-based). / El índice donde se insertará el nuevo nodo (basado en 0).
        """
        if position < 0 or position > self.size:
            raise IndexError("Invalid position / Posición inválida")

        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def reverse(self):
        """
        [ENG] Reverses the singly linked list.

        [ESP] Invierte la lista enlazada simple.
        """
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  # Update head to the new first node

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
            self.size -= 1
            return

        current = self.head
        while current.next and current.next.value != data:
            current = current.next

        if current.next:
            current.next = current.next.next
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
            return

        current = self.head
        prev = None
        for _ in range(position):
            prev = current
            if not current.next:
                return  # Position out of bounds
            current = current.next

        prev.next = current.next

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

    def display(self):
        """
        [ENG] Displays the elements of the linked list.

        [ESP] Muestra los elementos de la lista enlazada.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")
    

