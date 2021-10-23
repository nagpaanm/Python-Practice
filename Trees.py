'''
Created on Oct. 22, 2021

@author: Anmol Nagpal
'''

"""
Tree terminology.

- Set of 'nodes' (possibly with values or labels), with directed
'edges' between some pairs of nodes.
- One node is distinguished as 'root'
- Each non-root node has exactly one 'parent'
- A 'path' is a sequence of nodes n1; n2;...;nk, where there is an
edge from ni to ni+1, i < k
- The 'length' of a path is the number of edges in it
- There is a unique path from he root to each node. In the case of the
root itself this is just n1, if the root is node n1
- There are no 'cycles'; no paths that form loops
- 'Leaf': node with no children
- 'Internal node:' node with one or more children
- 'Subtree': tree formed by any tree node together with its descendants
and edges leading to them
- 'Height': 1 + the maximum path length in a tree. A node also has a
height, which is 1 + the maximum path length of the tree rooted at that 
node
- 'Depth': length of the path from the root to a node, so the root 
itself has depth 0
- 'Arity', branching factor: maximum number of children for any node

"""


class Tree:
    def __init__(self, value=None, children=None):
        """
        Create Tree self with content 'value' and 0 or more children
        
        :param value: value contained in this tree
        :type value: object
        :param children: possibly empty lost of children
        :type children: list[Tree]
        """
        self.value = value
        # copy children if not None
        self.children = children.copy() if children else []
        

def leaf_count(t):
    """
    Return the number of leaves in Tree t.
    """
    
    if len(t.children) == 0:
        # t is a leaf
        return 1
    else:
        return sum([leaf_count(c) for c in t.children])

def height(t):
    """
    Return 1 + the length path of t. I.e return the height of tree, t.
    """
    
    if len(t.children) == 0:
        # t is a leaf
        return 1
    else:
        return 1 + max([height(c) for c in t.children])

def arity(t):
    """
    Return the maximum branching factor (arity) of tree t.
    """
    if len(t.children) == 0:
        # t is a leaf
        return 0
    else:
        # t is an internal node
        return max([len(t.children)] + [arity(n) for n in t.children] )

def count(t):
    """
    Return the number of nodes in t
    """
    if len(t.children) == 0:
        # t is a leaf
        return 1
    return 1 + sum([count(c) for c in t.children])

if __name__ == '__main__':
    tree2 = Tree(2)
    tree3 = Tree(3)
    tree4 = Tree(4)
    tree5 = Tree(5, [tree4])
    tree6 = Tree(6, [tree5])
    tree1 = Tree(1, [tree2, tree3, tree6])
    
    """
            1
          / | \
         2  3  6
                \
                 5
                  \
                   4
    """
    print("Leaves: ", leaf_count(tree1))
    print("Height: ", height(tree1))
    print("Arity: ", arity(tree1))
    print("Count: ", count(tree1))