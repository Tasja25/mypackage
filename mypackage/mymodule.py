def top_n(items, n):
    """ Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object
        n(int): number of items to return

    Return:
        array: top n items, in desc order

    Examples:
        >>> top_n(8,3,1,2,7,4, 3)
        [8,7,4]
"""

for i in range(n):  #Keep sorting until we have the top n items
    for j in range(len(items)-1-i):

        if items[j] > items[j+1]:   #If this item is bigger than the next item...
            items[j], items[j+1] = items[j+1],items[j]  #Swap the two

#Get last 2 items
top_n = items[-n:]

#return in descending order
return top_n[::-1]


