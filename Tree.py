from collections import deque
class Node:
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children
    def dfs(self):
        self.__dfsHelper(self)
    def __dfsHelper(self, tree):
        print(tree.data)
        if tree.children != None:
            for child in tree.children:
                self.__dfsHelper(child)
    
    def dfs_iterative(self):
        tree = self
        stack  = [tree]
        while len(stack):
            t = stack.pop()
            print(t.data)
            if t.children != None:
                stack += reversed(t.children)
                    
    def bfs(self):
        queue = deque()
        queue.append(self)
        while len(queue):
            node = queue.popleft()
            print(node.data)
            if node.children != None:
                queue += node.children

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.children = [b,c,d]
    b.children = [e,f]
    a.dfs()
    stack = [1,3]
    stack += reversed([6,7,8])
    print(stack)
    a.dfs_iterative()