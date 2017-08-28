from linked_list import *

demo_exps = """\
s1_l
s1.long_repr()
str(s1)
repr(s1)
NULL
Node.fromlist([0, 2, 4])
Node.fromlist([1, 3, 5])
s2
s3
s4
len(s1)
s1.head_item()
s1.tail()
s1.last()
s1.init()
s1.drop(11)
s1.take(15)
s1[14]
s1.setitem(5, -1)
s1.insert_at_tail(-1)
s1.insert_at_head(-1)
s1.insert_at_n(-1, 10)
s1.delete_node(18)
s1.reverse()
s2.merge(s3)
s4.index(2)
s4.index(29)
s4.count(0)
s4.count(10)
4 in s3
7 in s3
s1.overwritestart(s2)
(list(s1) == s1_l)
(Node.fromlist(s1_l) == s1)
(s2 == s1)
(Node.fromlist([1] * 20) == s1)\
""".split("\n")

if __name__ == "__main__":
    import random

    s1_l = [random.randrange(100) for _ in range(20)]
    s1 = Node.fromlist(s1_l)
    s2 = Node.fromlist([0, 2, 4])
    s3 = Node.fromlist([1, 3, 5])
    s4 = Node.fromlist([0, 3, 2, 4, 0, 0, 2, 4, 5])

    max_exp = str(max(len(i) for i in demo_exps))

    for expr in demo_exps:
        print(f"{expr: <{max_exp}} = {eval(expr)}")
