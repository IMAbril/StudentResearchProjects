from BaseLinkedList import BaseLinkedList
from Node import Node

class CircularLinkedList(BaseLinkedList):
    """
    [ENG] Implementation of a circularly linked list.
    In this list, the last node points back to the first node, creating a circular structure.

    [ESP] Implementación de una lista enlazada circular.
    En esta lista, el último nodo apunta de nuevo al primer nodo, creando una estructura circular.
    """

    def __init__(self):
        """
        [ENG] Initializes an empty circular linked list.

        [ESP] Inicializa una lista circular enlazada vacía.
        """
        super().__init__()

    def insert(self, data):
        """
        [ENG] Inserts a new node with the given data into the circular linked list.
        If the list is empty, the node points to itself. Otherwise, it links to the first node.

        [ESP] Inserta un nuevo nodo con los datos proporcionados en la lista enlazada circular.
        Si la lista está vacía, el nodo apunta a sí mismo. De lo contrario, se enlaza al primer nodo.

        :param data: The value to store in the new node. / El valor a almacenar en el nuevo nodo.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # Points to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.tail = new_node
            new_node.next = self.head  # Points back to the head
        self.size += 1

    def insert_at_position(self, data, position):
        """
        [ENG] Inserts a new node at a specified position in the circular linked list.

        [ESP] Inserta un nuevo nodo en una posición específica de la lista enlazada circular.

        :param data: The value to store in the new node. / El valor a almacenar en el nuevo nodo.
        :param position: The index where the new node will be inserted (0-based). / El índice donde se insertará el nuevo nodo (basado en 0).
        """
        if position < 0 or position > self.size:
            raise IndexError("Invalid position / Posición inválida")

        new_node = Node(data)

        if position == 0:
            if self.is_empty():
                self.head = new_node
                new_node.next = self.head
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                new_node.next = self.head
                current.next = new_node
                self.head = new_node  # Update head to new node
            self.size += 1
            return

        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def reverse(self):
        """
        [ENG] Reverses the circular linked list.

        [ESP] Invierte la lista enlazada circular.
        """
        if self.is_empty() or self.head.next == self.head:
            return
        
        prev = None
        current = self.head
        next_node = None
        first_node = self.head  # Store the first node to update after reversal

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:  # Stop when we complete the circle
                break

        first_node.next = prev  # Fix the last node's reference
        self.head = prev  # Update head to the new first node

    def delete(self, data):
        """
        [ENG] Deletes the first occurrence of a node containing the given data from the circular linked list.

        [ESP] Elimina la primera aparición de un nodo que contiene los datos proporcionados de la lista enlazada circular.

        :param data: The data to search and remove from the list. / Los datos a buscar y eliminar de la lista.
        """
        if self.is_empty():
            return
        
        current = self.head
        if current.value == data:
            if current.next == self.head:  # Only one element
                self.head = None
            else:
                # Find the last node
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next  # Link last node to second node
                self.head = self.head.next  # Move head to the next node
            self.size -= 1
            return
        
        prev = None
        while current and current.value != data:
            prev = current
            current = current.next
            if current == self.head:  # If we complete a full circle
                break
        
        if current:
            prev.next = current.next  # Bypass the node to delete
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
            if self.head.next == self.head:
                self.head = None  # Only one node case
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        current = self.head
        prev = None
        for _ in range(position):
            prev = current
            current = current.next
            if current == self.head:
                return  # Position out of bounds

        prev.next = current.next

    def search(self, data):
        """
        [ENG] Searches for a node containing the given data in the circular linked list.

        [ESP] Busca un nodo que contiene los datos proporcionados en la lista enlazada circular.

        :param data: The data to search for. / Los datos a buscar.
        :return: The node if found, otherwise None. / El nodo si se encuentra, de lo contrario None.
        """
        if self.is_empty():
            return None
        
        current = self.head
        while current:
            if current.value == data:
                return current
            current = current.next
            if current == self.head:  # We completed the circle
                break
        return None

    def display(self):
        """
        [ENG] Displays the elements of the circular linked list.

        [ESP] Muestra los elementos de la lista enlazada circular.
        """
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
            if current == self.head:  # We completed the circle
                break
        print(" -> ".join(elements) + " -> (back to head)")

