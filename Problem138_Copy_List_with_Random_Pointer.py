"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        newhead = Node(0)
        pre = newhead
        node_list = dict()
        pointer = head
        while pointer:
            node = Node(pointer.val)
            node_list[pointer] = node
            pre.next = node
            pre = node
            pointer = pointer.next
        pre.next = None
        pointer = head
        while pointer:
            if not pointer.random:
                node_list[pointer].random=None
            else:
                node_list[pointer].random = node_list[pointer.random]
            pointer = pointer.next
        return newhead.next
