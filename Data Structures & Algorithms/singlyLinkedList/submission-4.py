class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
            
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = -1
        curr = self.head
        while i < index:
            if not curr.next_node:
                return -1
            curr = curr.next_node
            i += 1 
        
        return curr.value
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node
        if not new_node.next_node:
            self.tail = new_node
    

        

    def insertTail(self, val: int) -> None:
        self.tail.next_node = Node(val)
        self.tail = self.tail.next_node


    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            # move curr to the node before the one being removed
            i += 1 
            curr = curr.next_node
            
        if curr and curr.next_node:
            if curr.next_node == self.tail:
                self.tail = curr
            curr.next_node = curr.next_node.next_node
            return True
        return False


    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next_node
        while curr:
            res.append(curr.value)
            curr = curr.next_node
        
        return res

