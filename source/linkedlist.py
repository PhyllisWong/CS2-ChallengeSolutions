#!python

import pdb
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        # pdb.set_trace()
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        new_node.next = None

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        # reassign the tail to the new node
        self.tail = new_node
        # print("HERE!!!{}".format(self.tail.next))
        # self.tail.next = None


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        # reassign the head to the new node
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        current = self.head
        # If the linked list is not empty
        while current is not None:
            if current.data == quality(item):
                return current
            current = current.next
        if current is None:
            raise ValueError('Item not found: {}'.format(item))

    # def delete(self, item):
    #     """Delete the given item from this linked list, or raise ValueError.
    #     TODO: Best case running time: O(???) Why and under what conditions?
    #     TODO: Worst case running time: O(???) Why and under what conditions?"""
    #     # TODO: Loop through all nodes to find one whose data matches given item
    #     # TODO: Update previous node to skip around node with matching data
    #     # TODO: Otherwise raise error to tell user that delete has failed
    #     # Hint: raise ValueError('Item not found: {}'.format(item))
    #     current = self.head
    #     previous = None
    #     # If the linked list is not empty
    #     while current is not None:
    #         if current.find(item):
    #             # Item found at the end
    #             if previous and not current.get_next():
    #                 previous.set_next(current.get_next())
    #             # Item found in the middle
    #             elif previous and current.get_next():
    #                 previous.set_next(current.get_next())
    #             # item found at the head
    #             else:
    #                 self.head = current.get_next()
    #         previous = current
    #         current = current.get_next()
    #     else:
    #         raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print(ll)
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
