from abc import ABC, abstractmethod
# ABC makes a class abstract, preventing its direct instantiation./ABC Convierte una clase en abstracta, evitando su instanciación directa.

class BaseLinkedList(ABC):
    """
    [ENG] Abstract base class for a linked list.
    Provides a general structure for different types of linked lists.

    [ESP] Clase base abstracta para una lista enlazada.
    Proporciona una estructura general para diferentes tipos de listas enlazadas.
    """

    def __init__(self):
        """
        [ENG] Initializes an empty linked list.

        [ESP] Inicializa una lista enlazada vacía.
        """
        self.head = None  # Reference to the first node 
        self.tail = None  # Reference to the last node (used in some implementations).
        self.size = 0     # Number of elements in the list 

    
    @abstractmethod # When a method is decorated with @abstractmethod, it means all subclasses must implement it.
    def insert(self, data):
        """
        [ENG] Inserts a new node into the linked list.

        [ESP] Inserta un nuevo nodo en la lista enlazada.

        :param data: The data to store in the new node. / Los datos a almacenar en el nuevo nodo.
        """
        pass

    @abstractmethod
    def delete(self, data):
        """
        [ENG] Deletes a node containing the given data.

        [ESP] Elimina un nodo que contiene los datos proporcionados.

        :param data: The data to search and remove from the list. / Los datos a buscar y eliminar de la lista.
        """
        pass

    @abstractmethod
    def search(self, data):
        """
        [ENG] Searches for a node containing the given data.

        [ESP] Busca un nodo que contiene los datos proporcionados.

        :param data: The data to search for. / Los datos a buscar.
        :return: The node if found, otherwise None. / El nodo si se encuentra, de lo contrario None.
        """
        pass

    def is_empty(self):
        """
        [ENG] Checks if the linked list is empty.

        [ESP] Verifica si la lista enlazada está vacía.

        :return: True if the list is empty, False otherwise. / True si la lista está vacía, False en caso contrario.
        """
        return self.size == 0

    def get_size(self):
        """
        [ENG] Returns the number of elements in the linked list.

        [ESP] Retorna el número de elementos en la lista enlazada.

        :return: The size of the list. / El tamaño de la lista.
        """
        return self.size

    @abstractmethod
    def display(self):
        """
        [ENG] Displays the linked list elements.

        [ESP] Muestra los elementos de la lista enlazada.
        """
        pass

    

