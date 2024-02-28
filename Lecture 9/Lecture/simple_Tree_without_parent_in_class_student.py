class TreeWithoutParent:
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

    def __str__(self):
        return str(self._element)

def PreOrderTraversal(tree):
    # base case
    if tree == None: 
        return []
    # TODO (use recursion to traverse and return node visit ordering)
    else:
        list = []
        list += [tree._element]
        if tree._left:
            list += PreOrderTraversal(tree._left)

        if tree._right:
            list += PreOrderTraversal(tree._right)

        return list
    
def PostOrderTraversal(tree):
    # base case
    if tree == None: 
        return []
    # TODO (use recursion to traverse and return node visit ordering)
    else:
        list = []

        if tree._left:
            list += PostOrderTraversal(tree._left)

        if tree._right:
            list += PostOrderTraversal(tree._right)

        list += [tree._element]

        return list
def InOrderTraversal(tree):
    # base case
    if tree == None: 
        return []
    # TODO (use recursion to traverse and return node visit ordering)
    else:
        list = []

        if tree._left:
            list += InOrderTraversal(tree._left)

        list += [tree._element]

        if tree._right:
            list += InOrderTraversal(tree._right)

        return list

### Uncomment the following code if you want to print the tree.
### We assume that you had variables:  _left, _right, _element in the TreeWithoutParent Class.

#"""
def pretty_print(A):
    levels = 3      # Need a function to calculate levels. Use 3 for now.
    print_internal([A], 1, levels)

def print_internal(this_level_nodes, current_level, max_level):
    if (len(this_level_nodes) == 0 or all_elements_are_None(this_level_nodes)):
        return  # Base case of recursion: out of nodes, or only None left

    floor = max_level - current_level
    endgeLines = 2 ** max(floor - 1, 0)
    firstSpaces = 2 ** floor - 1
    betweenSpaces = 2 ** (floor + 1) - 1
    print_spaces(int(firstSpaces))
    next_level_nodes = []
    for node in this_level_nodes:
        if (node is not None):
            print(node._element, end = "")
            next_level_nodes.append(node._left)
            next_level_nodes.append(node._right)
        else:
            next_level_nodes.append(None)
            next_level_nodes.append(None)
            print_spaces(1)

        print_spaces(betweenSpaces)
    print()
    for i in range(1, endgeLines + 1):
        for j in range(0, len(this_level_nodes)):
            print_spaces(firstSpaces - i)
            if (this_level_nodes[j] == None):
                    print_spaces(endgeLines + endgeLines + i + 1);
                    continue
            if (this_level_nodes[j]._left != None):
                    print("/", end = "")
            else:
                    print_spaces(1)
            print_spaces(i + i - 1)
            if (this_level_nodes[j]._right != None):
                    print("\\", end = "")
            else:
                    print_spaces(1)
            print_spaces(endgeLines + endgeLines - i)
        print()

    print_internal(next_level_nodes, current_level + 1, max_level)

def all_elements_are_None(list_of_nodes):
    for each in list_of_nodes:
        if each is not None:
            return False
    return True

def print_spaces(number):
    for i in range(int(number)):
        print("  ", end = "")



#"""

if __name__ == '__main__':
    print("\nUsing Tree Data Structure Without a parent")

    ## Create a expression tree for this expression:  3*2 + 5-2"
    ## Please refer to slide 43 to construct the tree by creating nodes and store elements in self._element, 
    ## Then, connect nodes by assignment node instances to self._left and self._right
    ## TODO:
    node_1 = TreeWithoutParent('3')
    node_2 = TreeWithoutParent('2')
    node_3 = TreeWithoutParent('*', node_1, node_2)
    node_4 = TreeWithoutParent('5')
    node_5 = TreeWithoutParent('2')
    node_6 = TreeWithoutParent('-', node_4, node_5)
    tree = TreeWithoutParent('-', node_3, node_6)


    pretty_print(tree) #Call pretty_print to print the tree

    print("\nPreOrder:")
    print(PreOrderTraversal(tree))       # Expect: ['+', '*', '3', '2', '-', '5', '2']
    print("\nPostOrder:")
    print(PostOrderTraversal(tree))      # Expect: ['3', '2', '*', '5', '2', '-', '+']
    print("\nInOrder:")
    print(InOrderTraversal(tree))        # Expect: ['3', '*', '2', '+', '5', '-', '2']
