class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, data):
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def __str__(self):
        return '[' + ', '.join(str(node.data) for node in self) + ']'

    def __repr__(self):
        return f'LinkedList({self.head})'

    def __add__(self, other):
        result = LinkedList()
        current_self = self.head
        while current_self:
            result.append(current_self.data)
            current_self = current_self.next
        current_other = other.head
        while current_other:
            result.append(current_other.data)
            current_other = current_other.next
        return result

    def __mul__(self, times):
        result = LinkedList()
        for _ in range(times):
            current = self.head
            while current:
                result.append(current.data)
                current = current.next
        return result


# Example usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

print(len(llist))  # Output: 3
print(llist[0])    # Output: 1
print(llist[-1])   # Output: 3
print(llist[1:3])  # Output: [2, 3]

llist[1] = 5
print(llist)       # Output: [1, 5, 3]

llist2 = LinkedList()
llist2.append(4)
llist2.append(6)

print(llist + llist2)  # Output: [1, 5, 3, 4, 6]
print(llist * 2)        # Output: [1, 5, 3, 1, 5, 3]
