from cursor_based_list import CursorBasedList

# Defining Edit Buffer ADT for Text Editor
class EditBuffer:
    def __init__(self):
        self.List = CursorBasedList()
        self.FileName = None   # Current file
        self.i = -1    # Char pointer

    def __ConvertChars(self, line):
        """Converts a line into chars list."""
        chars_lst = []
        for char in line:
            chars_lst.append(char)
        return chars_lst

    def SetFileName(self, filename):
        self.FileName = filename

    def GetLineSize(self):
        """Returns the length of current line"""
        return len(self.List.getCurrent())

    def GetCurrentLine(self):
        """"PreCondition: List is not empty.
        Returns current line."""
        if not self.IsEmpty():
            line = ''.join(self.List.getCurrent())
            return line
        return 'File is Empty!'

    def GetCurrentChar(self):
        """PreCondition: File is not empty!
        Returns the current char."""
        if not self.GetLineSize() == 0:
            return self.GetCurrentLine()[self.i]
        return 'File is Empty!'

    def EditFile(self, filename):
        """Precondition: File exists in relative path.
        Inserts all lines from file into cursor-based list."""

        # Initializes construtor again incase of file is edited after creating
        self.__init__()
        self.SetFileName(filename)

        lines_lst = []
        # Checks if file exists
        try:
            with open(self.FileName, 'r') as f:
                lines_lst = f.readlines()

        except FileNotFoundError:
            # print(f'{self.FileName} does not exist in directory.')
            return -1

        # Inserting chars lists in nodes
        if len(lines_lst) > 0:
            for line in lines_lst:
                self.InsertLine(line)
        return 0

    def CreateNewFile(self, filename):
        """"Creates a new text file to edit."""
        with open(filename, 'w') as f: pass
        self.EditFile(filename)

    def InsertLine(self, line):
        """Inserts a line in Cursor based list"""
        chars = self.__ConvertChars(line+'\n')
        self.List.insertAfter(chars)

    def InsertChar(self, char):
        """Insert Character at cursor point."""
        if self.IsEmpty():
            self.List.insertAfter([char])
            self.i +=1
        else:
            self.List.getCurrent().insert(self.i+1, char)
            self.i +=1

    def MoveUp(self):
        """PreCondition: List is not empty and 
        current line is not first line.
        Moves current line Up."""
        if self.List.hasPrevious():
            self.List.previous()
        else:
            print('There is no line above!')

    def MoveDown(self):
        """PreCondition: List is not empty and 
        current line is not last line.
        Moves current line Down."""
        if self.List.hasNext():
            self.List.next() 
        else:
            print('That\'s the end of file!')

    
    def MoveRight(self):
        """PreCondition: Line is not empty and char is not last.
        Moves pointer to next char"""
        if not self.IsEmpty() and self.GetLineSize() != 0:
            if self.i == -1 or self.i==0:
                # if self.MoveDown() == 0:
                self.MoveDown()
                self.i = 0
            else:
                self.i +=1
        else:
            print('List/Line is empty!')


    def MoveLeft(self):
        """PreCondition: Line is not empty and char is not first.
        Moves pointer to next char"""
        if not self.IsEmpty() and self.GetLineSize() != 0:
            if self.i == (0-self.GetLineSize()):
                # if self.MoveUp() == 0:
                self.MoveUp()
                self.i = -1
            else:
                self.i -=1
        else:
            print('List/Line is empty!')

    def GoToFirst(self):
        """PreCondition: List is not empty!
        Moves the cursor to first line"""
        if not self.IsEmpty():
            return self.List.first()
        print('List is empty!')

    def GoToLast(self):
        """PreCondition: List is not empty!
        Moves the cursor to last line"""
        if not self.IsEmpty():
            return self.List.last()
        print('List is empty!')

    def DeleteLine(self):
        """PreCondition: List is not empty.
        Deletes the current line."""
        if not self.IsEmpty():
            return self.List.remove()
        print('List is empty!')
            
    def DeleteChar(self):
        """PreCondition: Line is not empty.
        Deletes the current char from line"""
        if not self.IsEmpty() and self.GetCurrentLine() !=0:
            return self.List.getCurrent().remove(self.i)
        print('List/Line is empty!')

    def ReplaceLine(self, newLine):
        """"PreCondition: List is not empty.
        Replaces current line with newLine."""
        if not self.IsEmpty():
            self.List.getCurrent().setData(newLine)
            return
        print('List is empty!')

    def ReplaceChar(self, newchar):
        """PreCondition: Line is not empty.
        Replaces the current char in line with newChar"""
        if not self.IsEmpty() and self.GetCurrentLine() !=0:
            self.List.getCurrent()[self.i] = newchar
            return self.List
        print('List/Line is empty!')

    def ClearFile(self):
        """Clears the current file data."""
        self.CreateNewFile(self.FileName)

    def SaveFile(self):
        """Saves the List in current file."""
        with open(self.FileName, 'w+') as f:
            if not self.IsEmpty():
                for line in self.List:
                    f.write(''.join(line))
        print('File Save Successfully!')

    def IsEmpty(self):
        """Checks if current file is empty"""
        return self.List.isEmpty()

    def __len__(self):
        """Returns the number of lines."""
        return len(self.List)

    def __str__(self):
        if self.IsEmpty():
            return 'File is empty!'
        lines = ''
        for line in self.List:
            lines += ''.join(line)
        return lines