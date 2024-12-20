from typing import Optional

class Node:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional['Node'] = None
        self.right_child: Optional['Node'] = None

    def insert(self, node: 'Node') -> bool:
        # if node.start <= self.end:  # Check for overlap on the right
        # Corrected overlap logic
        if not (node.end <= self.start or node.start >= self.end):  
            return False  

        #  binary tree traversal logic was not correct, debugged and corrected it.
        # if node.start <= self.end:
        #     if not self.right_child:
        #         self.right_child = node
        #         return True
        #     return self.left_child.insert(node)
        # elif node.end >= self.start:
        #     if not self.left_child:
        #         self.left_child = node
        #         return True
        #     return self.left_child.insert(node)

        # Correct binary tree traversal logic
        if node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        elif node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node)


class Calendar:
    def __init__(self):
        self.root: Optional[Node] = None

    def book(self, start: int, end: int) -> bool:
        new_node = Node(start, end)
        if not self.root:
            self.root = new_node
            return True
        return self.root.insert(new_node)


calendar = Calendar()

# test cases
print(calendar.book(5, 10))  # True (First event added)
print(calendar.book(8, 13))  # False (Overlaps with [5, 10))
print(calendar.book(10, 15)) # True (Back-to-back scheduling is allowed)
print(calendar.book(2, 5))   # True (Fits before [5, 10))
print(calendar.book(3, 7))   # False (Overlaps with [5, 10))
