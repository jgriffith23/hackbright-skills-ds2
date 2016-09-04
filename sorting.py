#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    # We don't want to go all the way to the end, or we'll get
    # an IndexError
    for index in range(len(lst) - 1):

        # Start with the swap tracker set to false. Innocent until proven
        # guilty.
        omg_we_swapped_bodies = False

        # Once we bubble a number all the way to the end, we don't want
        # to touch it again, so subtract the original index.
        for subindex in range(len(lst) - 1 - index):
            # Get the next two numbers in the list.
            lindsay = lst[subindex]
            jamie = lst[subindex + 1]

            if lindsay > jamie:
                # The number on the left is bigger, so swap the two
                # numbers. Freaky Friday (2003) ensues for these numbers.
                lindsay, jamie = jamie, lindsay

                # I realize that this isn't the most efficient way to set these
                # list elements, but I found a funny metaphor and really wanted
                # to keep it. This is our last assessment!
                lst[subindex] = lindsay
                lst[subindex + 1] = jamie

                # Every day I'm bubblin'...Or, we bubbled something, so
                # set the tracker.
                omg_we_swapped_bodies = True

        # If we didn't make a swap, then the list is sorted. Just bail out of
        # the loop early.
        if not omg_we_swapped_bodies:
            break

    return lst


# So, there's an episode of Star Trek: Voyager where two characters get
# merged into one...http://memory-alpha.wikia.com/wiki/Tuvix_(episode)
def merge_lists(tuvok, neelix):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    # Create an empty list to contain the merged list.
    tuvix = []

    # Since we know the lists are sorted, we can stop as soon
    # as either one is empty.
    while len(tuvok) > 0 and len(neelix) > 0:

        # Append the larger of the values at each list's index 0
        # to the merged list.
        if tuvok[0] > neelix[0]:
            tuvix.append(neelix[0])
            neelix.pop(0)

        else:
            tuvix.append(tuvok[0])
            tuvok.pop(0)

    # When we're done, extend the merged list with whatever's left in the
    # original lists, in case one had leftover elements.
    tuvix.extend(tuvok)
    tuvix.extend(neelix)
    return tuvix

##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    pass




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print