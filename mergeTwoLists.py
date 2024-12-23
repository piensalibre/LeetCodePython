
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MergeTwoLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodoInicial = ListNode()
        puntero = nodoInicial
        
        while list1 and list2:
            if list1.val < list2.val:
                puntero.next = list1
                list1 = list1.next
            else:
                puntero.next = list2
                list2 = list2.next
            
            puntero = puntero.next
            
        puntero.next = list1 if list1 else list2
        
        return nodoInicial.next
                    