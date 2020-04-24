from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.capacity

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

    def choose_next(self, node):
        # if the current pointer as a next
        if node.next is not None:
            # use that has the following node
            next_node = node.next
        else:
            # else use the head of the storage
            next_node = self.storage.head
        return next_node

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # grab the starting node
        initial_node = self.current
        # append the value from the starting node to the list buffer
        list_buffer_contents.append(initial_node.value)
        next_node = self.choose_next(initial_node)

        # while there are other node keep iterating
        while next_node != initial_node:
            # append the very next node value on each iteration to the buffer list
            # if the node value is not None
            if next_node.value is not None:
                list_buffer_contents.append(next_node.value)
            # check if there is a next otherwise make storage head it
            next_node = self.choose_next(next_node)
        
        # return list of buffer
        return list_buffer_contents

# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        # set the storage to be an instance of the class RingBuffer
        self.storage = RingBuffer(capacity)
        # iterate over the new instance of storage for the entire capacity
        for __ in range(0, capacity):
            # and place None as placeholders
            self.storage.append(None)

    def append(self, item):
        # on append run the append method of the RingBuffer class instance
        return self.storage.append(item)

    def get(self):
        # on get run the get method of the RingBuffer class instance
        return self.storage.get()