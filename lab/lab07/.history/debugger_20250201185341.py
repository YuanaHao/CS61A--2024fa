def without(s, i):
    """Return a new linked list like s but without the element at index i.

    >>> s = Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 0)
    Link(5, Link(7, Link(9)))
    >>> without(s, 2)
    Link(3, Link(5, Link(9)))
    >>> without(s, 4)           # There is no index 4, so all of s is retained.
    Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 4) is not s  # Make sure a copy is created
    True
    """
    if i < 0:
        return Link(s.first, s.rest)
    
    # 处理删除第一个元素的情况
    if i == 0:
        return Link(s.rest.first, s.rest.rest)
    
    # 创建新的链表
    result = Link(s.first)
    current = result
    curr_s = s.rest
    pos = 1
    
    # 复制到目标位置之前的元素
    while curr_s is not Link.empty and pos < i:
        current.rest = Link(curr_s.first)
        current = current.rest
        curr_s = curr_s.rest
        pos += 1
    
    # 如果索引有效，跳过要删除的元素
    if curr_s is not Link.empty and curr_s.rest is not Link.empty:
        current.rest = Link(curr_s.rest.first, curr_s.rest.rest)
    
    return result

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
if __name__ == "__main__":
    s = Link(3, Link(5, Link(7, Link(9))))
    without(s, 0)