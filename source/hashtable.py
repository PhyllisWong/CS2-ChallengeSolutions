#!python
from linkedlist import LinkedList

# run time variables: b = buckets, n = entries, l = length
class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) because you search for the key until found."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) because you search for the key until found."""
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
            for key, val in bucket.items():
                # Collect all values in each bucket
                all_values.append(val)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) Because you search through every item."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) Because you search through each item in each bucket."""
        counter = 0
        # Loop through all buckets
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            counter += bucket.length()
        return counter

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) best case, first item / O(n) worse case,
        last item or isn't found."""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket - return boolean
        data = bucket.find(lambda item: item[0] == key)
        return data is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(1) best case, first item / O(n) worse case,
        last item or isn't found."""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        key_val = bucket.find(lambda item: item[0] == key)
        if key_val is not None:
            key, value = key_val
            return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) best case, first item / O(n) worse case,
        last item or isn't found."""
        # Find bucket where given key belongs
        index = self._bucket_index(key) # O(1) time
        bucket = self.buckets[index] # O(1) time

        key_val = bucket.find(lambda item: item[0] == key) # O(l) for l items in list
        if key_val is not None:
            bucket.delete(key_val) #O(l) length of list
        bucket.append((key, value)) #O(1) constant time

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(1) best case, first item / O(n) worse case,
        last item or isn't found."""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        node = bucket.find(lambda item: item[0] == key)
        # If found, delete entry associated with given key
        if node is not None:
            bucket.delete(node)
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
