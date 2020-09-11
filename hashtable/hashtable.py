class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# singly linked list


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return current

    def update_or_else_insert_at_head(self, key, value):
        # check if the key is already in the linked list
        # find the node
        current = self.head
        while current is not None:
            # if key is found, change the value
            if current.key == key:
                current.value = value
                # exit function immediately
                return
            current = current.next

        # if we reach the end of the list, it's not here!
        # make a new node, and insert at head
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

    def update_or_else_insert_at_tail(self):
        # walk through and check if key is here
        # if not, make a new node and insert at tail
        pass

    def delete(self):
        pass


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = max(MIN_CAPACITY, capacity)
        self.hash_map = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        #     algorithm fnv-1 is
        # hash := FNV_offset_basis do

        # for each byte_of_data to be hashed
        #     hash := hash × FNV_prime
        #     hash := hash XOR byte_of_data

        # return hash
        # Your code here
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed_var = FNV_offset_basis

        string_bytes = key.encode()

        for b in string_bytes:
            hashed_var = hashed_var * FNV_prime
            hashed_var = hashed_var ^ b

        return hashed_var

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # hash = 5381
        # for x in key:
        #     hash = ((hash << 5) + hash) + ord(x)
        # return hash & 0xFFFFFFFF

        hash_var = 5381
        string_bytes = key.encode()

        for x in string_bytes:
            hash_var = ((hash_var << 5) + hash_var) + x

        return hash_var

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Your code here

        """
        # no collisions
        # idx = self.hash_index(key)
        # self.hash_map[idx] = value
        """

        # with collisions

        hash_index = self.hash_index(key)
        if not self.hash_map[hash_index]:  # Nothing there, put a node
            self.hash_map[hash_index] = HashTableEntry(key, value)
        else:
            current_node = self.hash_map[hash_index]
            while current_node.key != key and current_node.next:
                current_node = current_node.next
            # update existing
            if current_node.key == key:
                current_node.value = value
            else:
                current_node.next = HashTableEntry(key, value)  # add at end

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        """
        # no collisions
        # idx = self.hash_index(key)
        # self.hash_map[idx] = None
        """
        # Your code here
        # hashed_index = self.hash_index(key)
        # self.hash_map[hashed_index] = None
        # hashed_index = self.hash_index(key)
        # if self.hash_map[hashed_index]:
        #     self.hash_map[hashed_index] = None
        # else:
        #     current_node = self.hash_map[hashed_index]
        #     while current_node and current_node.key == key:
        #         current_node.value = None
        # with collisions below

        hash_index = self.hash_index(key)
        if self.hash_map[hash_index]:
            current_node = self.hash_map[hash_index]
            prev = current_node
            while current_node.key != key and current_node.next:
                prev = current_node
                current_node = current_node.next
            # update existing
            if current_node.key == key:
                prev.next = current_node.next
                current_node.value = None
        else:
            print("Error: key not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        """
        # no collisions
        # idx = self.hash_index(key)
        # return self.hash_map[idx]
        """
        # Your code here
        # hashed_index = self.hash_index(key)
        # if self.hash_map[hashed_index]:
        #     return self.hash_map[hashed_index]
        # else:
        #     current_node = self.hash_map[hashed_index]
        #     while current_node and current_node.key == key:
        #         return current_node.value

        hash_index = self.hash_index(key)
        if self.hash_map[hash_index]:
            current_node = self.hash_map[hash_index]
            while current_node.key != key and current_node.next:
                current_node = current_node.next
            # update existing
            if current_node.key == key:
                return current_node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        old_hash_map = self.hash_map
        self.hash_map = [None] * new_capacity
        self.capacity = new_capacity
        for element in old_hash_map:
            current = element
            while current:
                self.put(element.key, element.value)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
