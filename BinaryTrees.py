'''
Created on Oct. 24, 2021

@author: Anmol Nagpal
'''

"""
Bnary Trees:

- arity = 2

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
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
        
        