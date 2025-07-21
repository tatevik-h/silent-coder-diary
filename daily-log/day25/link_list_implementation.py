class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr_indx = 0
        curr = self.head
        while curr and curr_indx <= index:
            if curr_indx == index: return curr.data
            curr_indx += 1
            curr = curr.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        curr_head = self.head
        new_node = Node(val)
        new_node.next = curr_head
        self.head = new_node  
        if not self.tail:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        curr_indx = 0
        while curr and curr_indx < index - 1:
            curr = curr.next
            curr_indx += 1

        if curr is None:
            return  # Index out of bounds

        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node

        if new_node.next is None:  # Added at tail
            self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return  # Empty list

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None  # List became empty
            return

        curr = self.head
        curr_indx = 0
        while curr and curr_indx < index - 1:
            curr = curr.next
            curr_indx += 1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(2)
obj.addAtTail(2)
obj.addAtIndex(1,1)
obj.deleteAtIndex(1)
