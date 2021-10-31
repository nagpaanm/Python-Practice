'''
Created on Oct. 24, 2021

@author: Anmol Nagpal
'''

"""
Binary Trees:

- arity = 2


Binary Search Trees (BST):
    - a BST with one node has height 1
    - a BST with 3 nodes may have height 2
    - a BST with 7 nodes may have height 3
    - a BST with 15 nodes may have height 4
    - a BST with 'n' nodes may have height [logn]
    
If the BST is 'balanced', then we can check whether an element is present
in about logn node accesses

"""

class BinaryTree:
    """
    A Binary Tree, i.e. arity = 2.
    """
    def __init__(self, data, left=None, right=None):
        """
        Create BinaryTree self with data & children left & right.
        
        :param data: data of this node
        :type data: object
        :param left: left child
        :type left: BinaryTree|None
        :param right: Right child
        :type right: BinaryTree|None
        """
        
        self.data, self.left, self.right = data, left, right
        
    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.
        
        :param other: object to check equivalence to self
        :type other: any
        :rtype: bool
        
        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        
        return type(self) == type(other) and \
                self.data == other.data and \
                self.left == other.left and \
                self.right == other.right
    
    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self) 
        inorder. Indent by indent.
        
        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        # recursive call
        right_tree = (self.right.__str__(indent + "    ") if self.right else "")
        left_tree = (self.left.__str__(indent + "    ") if self.left else "")
        return (right_tree + "{}{}\n".format(indent, str(self.data)) + left_tree)
    
    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to 
        produce an equivalent BinaryTree.
        
        :rtype: str
        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.data),
                                               repr(self.left),
                                               repr(self.right))
    
    def __contains__(self, value):
        """
        Return whether tree rooted at node contains value.
        
        :param object value: value to search for
        :type value: object
        :rtype: bool
        
        >>> BinaryTree(5, BinaryTree(7, BinaryTree(4, BinaryTree(3))), BinaryTree(9)).__contains__(3)
        True
        """
#         if self.data == value:
#             return True
#         if self.left:
#             if self.left.__contains__(value):
#                 return True
#         if self.right:
#             if self.right.__contains__(value):
#                 return True
#         return False
        
        # note: 'in' is equivalent to __contains__
        return (self.data == value or
                (self.left and value in self.left) or
                (self.right and value in self.right))
        
def evaluate(b):
    """
    Evaluate the expression rooted at b. If b is a leaf,
    return its float data. Otherwise, evaluate b.left and
    b.right and combine them with b.data.
    
    Assume: -- b is a non-empty binary tree
            -- interior nodes contain data in {"+", "-", "*", "/"}
            -- interior nodes always have two children
            -- leaves contain float data
            
    :param b: binary tree representing arithmetic expression
    :type b: BinaryTree
    :rtype: float
    
    >>> b = BinaryTree(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
    >>> evaluate(b)
    12.0
    """
    if b.left == None and b.right == None:
        return b.data
    else:
        return float(eval(str(evaluate(b.left)) + str(b.data) + str(evaluate(b.right))))
    
def insert(b, node):
    """
    Insert a new node to the binary search tree and return the new tree object.
    
    Assume node is the root of a Binary Search Tree.
    :param node: root of a binary search tree.
    :type node: BinaryTree
    :param data: data to insert into BST, if necessary.
    :type data: object
    >>> b = BinaryTree(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """
    if b.left is None and node < b.data:
        b.left = BinaryTree(node)
        return b
    if b.right is None and node >= b.data:
        b.right = BinaryTree(node)
        return b
    else:
        if node < b.data:
            insert(b.left, node)
        else:
            insert(b.right, node)
    return b

def bst_contains(node, value):
    """
    Return whether tree rooted at node contains value.
    
    Assume node is the root of a Binary Search Tree.
    
    :param node: node of a Binary Search Tree
    :type node: BinaryTree|None
    :param value: value to search for
    :type value: object
    :rtype: bool
    
    >>> bst_contains(None, 5)
    False
    >>> bst_contains(BinaryTree(7, BinaryTree(5), BinaryTree(9)), 5)
    True
    """
    
    if node is None:
        return False
    if value == node.data:
        return True
    if value < node.data:
        return bst_contains(node.left, value)
    else:
        return bst_contains(node.right, value)
    
def inorder_visit(root, act):
    """
    Visit each node of the binary tree rooted at root in order and act.
    
    Inorder traversal:
        - visit the left subtree inorder
        - visit this node itself
        - visit the right subtree inorder
        
    :param root: binary tree to visit
    :type root: BinaryTree
    :param act: function to execute on visit
    :type act: (BinaryTree)->object
    :rtype: None
    
    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> def f(node): print(node.data)
    >>> inorder_visit(b, f)
    2
    4
    6
    8
    12
    """
    if root is not None:
        inorder_visit(root.left, act)
        act(root)
        inorder_visit(root.right, act)

def preorder_visit(root, act):
    """
    Visit each node of the binary tree rooted at root in preorder and act.
    
    Preorder Traversal:
        - visit this node itself
        - visit the left subtree preorder
        - visit the right subtree preorder
    
    :param root: binary tree to visit
    :type root: BinaryTree
    :param act: function to execute on visit
    :type act: (BinaryTree)->object
    :rtype: None
    
    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> def f(node): print(node.data)
    >>> preorder_visit(b, f)
    8
    4
    2
    6
    12
    """
    if root is not None:
        act(root)
        preorder_visit(root.left, act)
        preorder_visit(root.right, act)

def postorder_visit(root, act):
    """
    Visit each node of the binary tree rooted at root in postorder and act.
    
    Postorder Traversal:
        - visit the left subtree postorder
        - visit the right subtree postorder
        - visit this node itself
    
    :param root: binary tree to visit
    :type root: BinaryTree
    :param act: function to execute on visit
    :type act: (BinaryTree)->object
    :rtype: None
    
    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> def f(node): print(node.data)
    >>> postorder_visit(b, f)
    2
    6
    4
    12
    8
    """
    if root is not None:
        postorder_visit(root.left, act)
        postorder_visit(root.right, act)
        act(root)
        
def level_order(b, act):
    """
    
    Level order traversal:
        - visit this node
        - visit this nodes's children
        - visit this node's grandchildren
        - visit this nodes great grandchilderen
        - ...
        
    I.e. Breadth-First-Traversal (BFS)
    """

def bst_find_right_most(b):
    """
    Find the right most node in a binary tree, b.
    """
    if b.right is None:
        return b
    else:
        bst_find_right_most(b.right)

def bst_find_left_most(b):
    """
    Find the left most node in a binary tree, b
    """
    if b.left is None:
        return b
    else:
        bst_find_right_most(b.left)
        
def bst_delete(b, data):
    """
    Delete data in BST rooted at root and return the tree;
    
    2 cases:
    
    case 1) The 'current' node has no left child
        - Simply connect the parent with the right child of the current node
    
    case 2) The 'current' node has a left child
        - Let 'right_most' point to the node that contains the largest element
        in the left subtree of the 'current' node
        - let 'parent_of_right_most' point to the parent node of the 'right_most'
        node
        
        Then:
        1) Replace the element value in the 'current' node with the one in the 
        'right_most' node
        2) Connect the 'parent_of_right_most' node with the left child of the
        'right_most' node
    
    Note: 'current' node is the node to delete

    :param root: root of a binary search tree.
    :type root: BinaryTree
    :param data: data to delete from BST, if exists.
    :type data: object

    >>> b = BinaryTree(5)
    >>> b1 = insert(b, 3)
    >>> b1 = insert(b1, 8)
    >>> b1 = bst_delete(b1, 3)
    >>> print(b1)
        8
    5
    <BLANKLINE>
    >>> b4 = BinaryTree(5)
    >>> b4 = insert(b4, 3)
    >>> b4 = insert(b4, 8)
    >>> b4 = bst_delete(b4, 5)
    >>> print(b4)
        8
    3
    <BLANKLINE>
    """
    if b is None:
        return
    elif data > b.data:
        b.right = bst_delete(b.right, data)
    elif data < b.data:
        b.left = bst_delete(b.left, data)
    else: # b.data == data
        if b.left is None:
            b = b.right;
        else: 
            right_most = bst_find_right_most(b.left)
            b.data = right_most.data
            if b.left is None:
                b.left = right_most.left
            else:
                temp = b.left
                replace_left = right_most.left
                if replace_left is not None:
                    left_most = bst_find_left_most(replace_left)
                    left_most.left = temp
                    b.left = replace_left
                else:
                    b.left = right_most.left
            
            # or 
            #b.left = bst_delete(b.left, right_most.data)
            
    return b
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
        
        