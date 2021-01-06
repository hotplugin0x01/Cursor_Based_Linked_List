"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  <PUT YOUR NAME HERE>
"""

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list."""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            # raise AttributeError("Empty list has no next item")
            return False
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            # raise AttributeError("Empty list has no previous item")
            return False
        return self._current.getPrevious() != self._header
    
    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no first item")
        self._current = self._header.getNext()

    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no last item")
        self._current = self._trailer.getPrevious()

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        if not self.hasNext():
            raise AttributeError('List has no further next item!')
        self._current = self._current.getNext()

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one iten"""
        if not self.hasPrevious():
            raise AttributeError('List has no further previous item!')
        self._current = self._current.getPrevious()

    def insertAfter(self, item):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self.isEmpty():
            n = Node2Way(item)
            n.setNext(self._trailer)
            self._trailer.setPrevious(n)

            n.setPrevious(self._header)
            self._header.setNext(n)
            self._current = n
            self._size +=1
            return

        n = Node2Way(item)
        n.setPrevious(self._current)
        n.setNext(self._current.getNext())
        self._current.getNext().setPrevious(n)
        self._current.setNext(n)
        self._current = n
        self._size +=1

        if not self.hasNext():
            self._trailer.setPrevious(n)


    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self.isEmpty():
            n = Node2Way(item)
            n.setNext(self._trailer)
            self._trailer.setPrevious(n)

            n.setPrevious(self._header)
            self._header.setNext(n)
            self._current = n
            self._size +=1
            return

        n = Node2Way(item)
        n.setNext(self._current)
        n.setPrevious(self._current.getPrevious())
        self._current.getPrevious().setNext(n)
        self._current.setPrevious(n)
        self._current = n
        self._size +=1

        if not self.hasPrevious():
            self._header.setNext(n)


    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        if self.isEmpty():
            raise AttributeError("Empty list has no current item")
        return self._current.getData()

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no current item")

        removed = self._current
        self._current.getPrevious().setNext(self._current.getNext())

        if self.hasNext():
            self._current.getNext().setPrevious(self._current.getPrevious())
            self._current = self._current.getNext()

        elif self.hasPrevious():
            self._current.getNext().setPrevious(self._current.getPrevious())
            self._current = self._current.getPrevious()

        else:
            self._current.getNext().setPrevious(self._current.getPrevious())
            self._current = None
    
        self._size -=1
        removed.setNext(None)
        removed.setPrevious(None)
        removed_value = removed.getData()
        del removed
        return removed_value       

    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Uderflow! List has no current item")

        self._current.setData(newItemValue)

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        """ Returns the number of items in the list."""
        return self._size

    def __str__(self):
        """Includes items from first through last."""
        lst = ''
        counter = self._header.getNext()
        while counter.getData() != None:
            lst += str(counter.getData()) + ' '
            counter = counter.getNext()
        return lst

# ---------------------Further Methods Added-------------------------------------
    def __iter__(self):
        counter = self._header.getNext()
        while counter.getData() != None:
            yield counter.getData()
            counter = counter.getNext()

    def HeaderNode(self):
        return self._header.getNext()

    def TrailerNode(self):
        return self._trailer.getPrevious()

    def getHeader(self):
        return self.HeaderNode().getData()

    def getTrailer(self):
        return self.TrailerNode().getData()