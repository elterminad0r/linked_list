# Linked lists
My Python linked list implementation. This is my expanded implementation from the HackerRank challenged. Note it's kind of half finished and untested so probably broken in all manner of fun ways. It's recursive so won't be able to handle any serious load due to Python's lack of tail call optimisation. It also overloads the `__or__` operator, which put together with recursion produces some slightly Haskell-inspired levels of conciseness:

```Python
def take(head, n):
    if n > 0:
        if head.next:
            return head | head.next.take(n - 1)
        raise IndexError
    return NULL
```

`demo.py` executes several examples (with a nice for loop and a safe application of eval). Here are a couple:

    s1.head_item()                  = 57
    s1.tail()                       = <45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.last()                       = 67
    s1.init()                       = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30>
    s1.drop(11)                     = <8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.take(15)                     = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90>
    s1[14]                          = 90
    s1.setitem(5, -1)               = <57, 45, 55, 58, 78, -1, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.insert_at_tail(-1)           = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67, -1>
    s1.insert_at_head(-1)           = <-1, 57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.insert_at_n(-1, 10)          = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, -1, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.delete_node(18)              = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 67>
    s1.reverse()                    = <67, 30, 70, 39, 33, 90, 79, 58, 8, 59, 18, 84, 43, 84, 95, 78, 58, 55, 45, 57>
    s2.merge(s3)                    = <0, 1, 2, 3, 4, 5>

NB it's Python 3.6, as it uses f-strings. Should be easy enough to use .format instead.
