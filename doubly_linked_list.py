class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

    def remove_tail(self):
        if self.head is None:
            pass

        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1

        else:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
            self.length -= 1


    def add_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.head = self.tail

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1

    def remove_head(self):
        if self.head is None:
            pass

        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1

        else:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            self.length -= 1

    def insert(self, pos, value):
        node = Node(value)
        if pos > (self.length - 1):
            return
        elif pos == 0 and self.head is None:
            self.head = node
            self.tail = node
        elif pos == 0:
            self.add_head(value)

        count = 0
        cur = self.head
        while count < (pos - 1):
            cur = cur.next
            count += 1

        node.prev = cur
        node.next = cur.next
        cur.next.prev = node
        cur.next = node

        self.length += 1

    def remove(self, pos):
        if self.head is None:
            return
        elif pos > (self.length - 1):
            return
        count = 0
        cur = self.head
        while count < (pos - 1):
            cur = cur.next
            count += 1
        cur.next.prev = None
        cur.next = cur.next.next
        cur.next.prev = cur

    def print_forwards(self):
        cur = self.head
        linked_list_string = ""

        if cur is None:
            print("")
        elif cur.next is None:
            print("[" + str(self.head.value) + "]")
        else:
            while cur.next is not None:
                linked_list_string += "[" + str(cur.value) + "] ->"
                cur = cur.next

            linked_list_string += "[" + str(cur.value) + "]"
            print(linked_list_string)

    def print_backwards(self):
        cur = self.tail
        linked_list_string = ''

        if cur is None:
            print('')
        elif cur.prev is None:
            print('[' + str(self.tail.value) + ']')

        else:
            while cur.prev is not None:
                linked_list_string += "[" + str(cur.value) + "] ->"
                cur = cur.prev

            linked_list_string += "[" + str(cur.value) + "]"
            print(linked_list_string)



if __name__ == '__main__':
    x = DoublyLinkedList()
    x.add_tail(5)
    x.add_tail(4)
    x.add_head(8)
    print('This is test 1')
    x.print_forwards()
    x.print_backwards()
    x.insert(1, 13)
    print('this is test 2')
    x.print_forwards()
    x.print_backwards()
    x.remove(1)
    print('this is test 3')
    x.print_forwards()
    x.print_backwards()
