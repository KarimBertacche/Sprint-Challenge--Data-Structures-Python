from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check whether the current storage length is less than the capacity
        if len(self.storage) < self.capacity:
            # place the item to the tail of the queue
            self.storage.add_to_tail(item)
            # and add the least used item in the head as the current for future removal
            self.current = self.storage.head
        # else if storage has reached the capacity
        elif len(self.storage) == self.capacity:
            # make the new least used item the next item in the list after the head
            # by keeping track of it in the current
            self.current = self.current.next
            # remove the item from the storage head
            self.storage.remove_from_head()
            # place the item to the tail of the queue
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
