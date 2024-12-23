import unittest

from mergeTwoLists import MergeTwoLists, ListNode

# Función auxiliar para convertir una lista de Python a una lista enlazada
# Función auxiliar para convertir una lista de Python a una lista enlazada
def to_linked_list(lst):
    if not lst:  # Si la lista está vacía, devolvemos None
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Función auxiliar para convertir una lista enlazada a una lista de Python
def to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Clase de pruebas unitarias
class TestMergeTwoLists(unittest.TestCase):
    
    def setUp(self):
        self.merge = MergeTwoLists()
    
    def test_merge_lists(self):
        # Casos de prueba
        list1 = to_linked_list([1, 2, 4])
        list2 = to_linked_list([1, 3, 4])
        merged = self.merge.mergeTwoLists(list1, list2)
        self.assertEqual(to_list(merged), [1, 1, 2, 3, 4, 4])
        
    def test_merge_empty_lists(self):
        # Prueba cuando ambas listas están vacías
        list1 = to_linked_list([])
        list2 = to_linked_list([])
        merged = self.merge.mergeTwoLists(list1, list2)
        self.assertEqual(to_list(merged), [])
        
    def test_merge_one_empty_list(self):
        # Prueba cuando una lista está vacía
        list1 = to_linked_list([1, 2, 3])
        list2 = to_linked_list([])
        merged = self.merge.mergeTwoLists(list1, list2)
        self.assertEqual(to_list(merged), [1, 2, 3])
        
    def test_merge_single_element_lists(self):
        # Prueba con listas de un solo elemento
        list1 = to_linked_list([1])
        list2 = to_linked_list([2])
        merged = self.merge.mergeTwoLists(list1, list2)
        self.assertEqual(to_list(merged), [1, 2])
        
    def test_merge_sorted_lists(self):
        # Prueba con listas ya ordenadas
        list1 = to_linked_list([2, 4, 6])
        list2 = to_linked_list([1, 3, 5])
        merged = self.merge.mergeTwoLists(list1, list2)
        self.assertEqual(to_list(merged), [1, 2, 3, 4, 5, 6])

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
