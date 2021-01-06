"""
File: cursorBasedListTester.py

Menu-driven tester for Cursor-Based List implementation
"""

from cursor_based_list import CursorBasedList

def testList():
    myList = CursorBasedList()
    while True:
        print("\n===============================================================")
        print("Current List:",myList)
        if myList.isEmpty():
            print("Empty list")
        else:
            print("length:",len(myList), " Current item:", myList.getCurrent())
            print('Header: ', myList.getHeader(), 'Trailer: ', myList.getTrailer())
        print("\nTest Positional List Menu:")
        print("A - insertAfter")
        print("B - insertBefore")
        print("C - getCurrent")
        print("E - isEmpty")
        print("F - First")
        print("L - Last")
        print("N - Next")
        print("P - Previous")
        print("R - remove")
        print("U - replace")
        print("X - eXit testing")
        response = input("Menu Choice? ").upper()
        if response == 'A':
            item = input("Enter the new item to insertAfter: ")
            myList.insertAfter(item)
        elif response == 'B':
            item = input("Enter the new item to insertBefore: ")
            myList.insertBefore(item)
        elif response == 'C':
            item = myList.getCurrent()
            print("The current item in the list is:",item)
        elif response == 'E':
            print("isEmpty returned:", myList.isEmpty())
        elif response == 'F':
            myList.first()
        elif response == 'L':
            myList.last()
        elif response == 'N':
            myList.next()
        elif response == 'P':
            myList.previous()
        elif response == 'R':
            item = myList.remove()
            print("item removed:",item)
        elif response == 'U':
            item = input("Enter replacement item: ")
            myList.replace(item)
        elif response == 'X':
            break
        else:
            print("Invalid Menu Choice!")

testList()

