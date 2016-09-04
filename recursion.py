# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """

    # Degenerative base case: If the index to print goes beyond the
    # length of the list, we know we're done printing.
    if i > len(my_list)-1:
        return

    # Until we hit the base case, print the list element at the
    # passed index, and recurse with an incremented i argument.
    print my_list[i]
    print_item(my_list, i+1)


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """

    # Base Case: If we hit a tree that is none, then we've reached the
    # end of a path. 
    if tree is None:
        return

    # If we actually have a tree to print, print its data.
    else:
        print tree.data

    # Once we've printed the tree, advance in the tree by looping
    # over its children and printing them, recursively.
    for child in tree.children:
        print_all_tree_data(child)



# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """

    # Base case: we always know the length of an empty list! (It's 0.)
    if my_list == []:
        return 0

    # Otherwise, we know there's at least one thing in it, so add 1 and
    # call recursively on a section of the list that doesn't contain the element
    # we just looked at.
    else:
        return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """

    # Base case: If a tree is none, we're at the end of a path. This one
    # doesn't count, so pass back 0 to the prev call.
    if tree is None:
        return 0

    # Otherwise, we should count this node, and the length of its
    # list of children.
    else:
        return 1 + len(tree.children)

    # Now, for each child in the list, do the same thing.
    for child in tree.children:
        num_nodes(child)

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
