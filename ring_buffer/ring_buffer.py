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
            # grab the older item from the head
            oldest_item = self.storage.head
            # remove the item from the storage head
            self.storage.remove_from_head()
            # place the newly added item to the tail of the queue
            self.storage.add_to_tail(item)
            # oldest item is the current 
            if oldest_item is self.current:
                # then make the current the tail of the storage
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # grab the starting node
        initial_node = self.current
        # append the value from the starting node to the list buffer
        list_buffer_contents.append(initial_node.value)
        # if the starting node as a next
        if initial_node.next is not None:
            # use that has the following node
            next_node = initial_node.next
        else:
            # else use the head of the storage
            next_node = self.storage.head

        # while there are other node keep iterating
        while next_node != initial_node:
            # append the very next node value on each iteration to the buffer list
            list_buffer_contents.append(next_node.value)
            # check if there is a next otherwise make storage head it
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head
        
        # return list of buffer
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
