class Node:
    def __init__(self, data, next_node):
       self.data = data
       self.next = next_node

    @classmethod
    def build(cls, it):
        for i in it:
            return cls(i, cls.build(it))
        return NULL

    @classmethod
    def fromlist(cls, l):
        return cls.build(iter(l))

    def __or__(head, other):
        return Node(head.data, other)

    def __iter__(head):
        if head:
            yield head.data
            yield from head.next

    def __str__(head):
        return "<{}>".format(", ".join(map(str, head)))

    def long_repr(head):
        return "Node(data={}, next_node={})".format(head.data, head.next.long_repr() if head.next else "NULL")

    def __repr__(head):
        return "Node(data={}, next_node={})".format(head.data, "..." if head.next else "NULL")

    def __eq__(head, other):
        return (not (head and other)) or (head.data == other.data and head.next == other.next)

    def __getitem__(head, n):
        if n == 0:
            return head.data
        return head.next[n - 1]

    def __len__(head):
        if head:
            if head.next:
                return 1 + len(head.next)
            return 1
        return 0

    def __bool__(head):
        return head.next is not None

    def __contains__(head, target):
        if head:
            return head.data == target or target in head.next
        return 0

    def head_item(head):
        return head.data

    def tail(head):
        return head.next

    def last(head):
        if head.next:
            return head.next.last()
        return head.data

    def init(head):
        if head.next:
            return head | head.next.init()
        return NULL

    def drop(head, n):
        if n == 0:
            return head
        if head.next:
            return head.next.drop(n - 1)
        raise IndexError

    def take(head, n):
        if n > 0:
            if head.next:
                return head | head.next.take(n - 1)
            raise IndexError
        return NULL

    def insert_at_tail(head, data):
        if head.next:
            return head | head.next.insert_at_tail(data)
        return head | Node(data, NULL)

    def insert_at_head(head, data):
        return Node(data, head)

    def insert_at_n(head, data, n):
        if head:
            if n == 0:
                return Node(data, head)
            return head | head.next.insert_at_n(data, n - 1)
        raise IndexError

    def delete_node(head, n):
        if n == 0:
            return head.next
        if head.next:
            return head | head.next.delete_node(n - 1)
        raise IndexError

    def reverse(head):
        if head.next:
            start = head.next.reverse()
            return start.insert_at_tail(head.data)
        if head:
            return head
        return NULL

    def merge(head, other):
        if not head:
            return other
        if not other:
            return head
        if head.data < other.data:
            return head | other.merge(head.next)
        return other | head.merge(other.next)

    def index(head, item):
        if head:
            if head.data == item:
                return 0
            else:
                i = head.next.index(item)
                if i == -1:
                    return i
                return 1 + i
        return -1

    def count(head, item):
        if head:
            if head.data == item:
                return 1 + head.next.count(item)
            return head.next.count(item)
        return 0

    def setitem(head, n, new_val):
        if head:
            if n == 0:
                return Node(new_val, head.next)
            return head | head.next.setitem(n - 1, new_val)
        raise IndexError

    def overwritestart(head, other):
        if other:
            if head:
                return Node(other.data, head.next.overwritestart(other.next))
            raise IndexError
        return head
    
    def overwritesub(head, n, other):
        if n == 0:
            return head.overwritestart(other)
        if head:
            return head.next.overwritesub(n - 1, other)
        raise IndexError

    def add_to_end(head, other):
        if not head.next:
            return head | other
        return head | head.next.add_to_end(other)

    def filter(head, predicate):
        if head:
            if predicate(head.data):
                return head | head.next.filter(predicate)
            return head.next.filter(predicate)
        return NULL
    
    def map(head, f):
        if head:
            return Node(f(head.data), head.next.map(f))

    def reduce(head, f):
        if head.next:
            return f(head.data, head.next.reduce(f))
        return head.data

NULL = Node(None, None)
