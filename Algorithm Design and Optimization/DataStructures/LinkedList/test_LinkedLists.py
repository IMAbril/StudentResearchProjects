import pytest
from SinglyLinkedList import SinglyLinkedList
from DoublyLinkedList import DoublyLinkedList
from CircularLinkedList import CircularLinkedList

# ----- Fixtures to initialize lists -----
@pytest.fixture
def singly_linked_list():
    return SinglyLinkedList()

@pytest.fixture
def doubly_linked_list():
    return DoublyLinkedList()

@pytest.fixture
def circular_linked_list():
    return CircularLinkedList()

# ----- Test for SinglyLinkedList -----
def test_insert(singly_linked_list):
    singly_linked_list.insert(1)
    singly_linked_list.insert(2)
    singly_linked_list.insert(3)
    assert singly_linked_list.head.value == 1
    assert singly_linked_list.head.next.value == 2
    assert singly_linked_list.head.next.next.value == 3

def test_insert_at_position(singly_linked_list):
    singly_linked_list.insert(1)
    singly_linked_list.insert(3)
    singly_linked_list.insert_at_position(2, 1)
    assert singly_linked_list.head.next.value == 2

def test_reverse(singly_linked_list):
    singly_linked_list.insert(1)
    singly_linked_list.insert(2)
    singly_linked_list.insert(3)
    singly_linked_list.reverse()
    assert singly_linked_list.head.value == 3

def test_delete(singly_linked_list):
    singly_linked_list.insert(1)
    singly_linked_list.insert(2)
    singly_linked_list.insert(3)
    singly_linked_list.delete(2)
    assert singly_linked_list.head.next.value == 3

def test_delete_at_position(singly_linked_list):
    singly_linked_list.insert(1)
    singly_linked_list.insert(2)
    singly_linked_list.insert(3)
    singly_linked_list.delete_at_position(1)
    assert singly_linked_list.head.next.value == 3

def test_search(singly_linked_list):
    singly_linked_list.insert(1)
    singly_linked_list.insert(2)
    singly_linked_list.insert(3)
    assert singly_linked_list.search(2)
    
    with pytest.raises(ValueError, match="4 is not in the list"):
        singly_linked_list.search(4)

def test_get_size(singly_linked_list):
    singly_linked_list.insert(1)
    singly_linked_list.insert(2)
    assert singly_linked_list.get_size() == 2

# ----- Test for DoublyLinkedList -----
def test_insert_doubly(doubly_linked_list):
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    assert doubly_linked_list.head.value == 1
    assert doubly_linked_list.tail.value == 2

def test_insert_at_position_doubly(doubly_linked_list):
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(3)
    doubly_linked_list.insert_at_position(2, 1)
    assert doubly_linked_list.head.next.value == 2

def test_reverse_doubly(doubly_linked_list):
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)
    doubly_linked_list.reverse()
    assert doubly_linked_list.head.value == 3

def test_delete_doubly(doubly_linked_list):
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)
    doubly_linked_list.delete(2)
    assert doubly_linked_list.head.next.value == 3

def test_get_size_doubly(doubly_linked_list):
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    assert doubly_linked_list.get_size() == 2

def test_recursive_search(doubly_linked_list):
    doubly_linked_list.insert(10)
    doubly_linked_list.insert(20)
    doubly_linked_list.insert(30)

    found_node = doubly_linked_list.recursive_search(20)
    assert found_node.value == 20

    found_node = doubly_linked_list.recursive_search(30)
    assert found_node.value == 30

    with pytest.raises(ValueError, match="40 is not in the list."):
        doubly_linked_list.recursive_search(40)

# ----- Test for CircularLinkedList -----
def test_insert_circular(circular_linked_list):
    circular_linked_list.insert(1)
    circular_linked_list.insert(2)
    assert circular_linked_list.head.value == 1
    assert circular_linked_list.head.next.value == 2
    assert circular_linked_list.tail.next == circular_linked_list.head  # Circular check

def test_insert_at_position_circular(circular_linked_list):
    circular_linked_list.insert(1)
    circular_linked_list.insert(3)
    circular_linked_list.insert_at_position(2, 1)
    assert circular_linked_list.head.next.value == 2

def test_reverse_circular(circular_linked_list):
    circular_linked_list.insert(1)
    circular_linked_list.insert(2)
    circular_linked_list.insert(3)
    circular_linked_list.reverse()
    assert circular_linked_list.head.value == 3

def test_delete_circular(circular_linked_list):
    circular_linked_list.insert(1)
    circular_linked_list.insert(2)
    circular_linked_list.insert(3)
    circular_linked_list.delete(2)
    assert circular_linked_list.head.next.value == 3

def test_get_size_circular(circular_linked_list):
    circular_linked_list.insert(1)
    circular_linked_list.insert(2)
    assert circular_linked_list.get_size() == 2
