from text_editor_main import EditBuffer

def ShowOptions(editor):
	while True:
		print('\n===============================================================')
		print('Please choose what you want to do:')
		print('1: Insert New Line.')
		print('2: Insert new character.')
		print('3: Move Cursor Up.')
		print('4: Move Cusor Down.')
		print('5: Move Cursor Right.')
		print('6: Move Cursor Left.')
		print('7: Go to first line.')
		print('8: Go to last line.')
		print('9: Replace Current Line.')
		print('10: Replace Current Character')
		print('11: Delete Current Line.')
		print('12: Delete Current Character.')
		print('13: Show File Data.')
		print('14: Clear File.')
		print('15: Save File.')
		print('16: Exit.')

		if not editor.IsEmpty():
			print(f'\nCurrent Line: {editor.GetCurrentLine()}\nLength of Line: {editor.GetLineSize()}\nChar Index: {editor.i}')
			print(f'Total Lines: {len(editor)}\nCursor at: {editor.GetCurrentChar()}\n')

		option = input()

		try:
			int(option)
		except ValueError:
			print('Please enter option in number.\n')
			continue
		else:
			option = int(option)

		if option == 1:
			print('Enter the line you want to insert:')
			line = input()
			editor.InsertLine(line)
		elif option == 2:
			print('Enter the character you want to insert:')
			char = input()
			editor.InsertChar(char)
		elif option == 3:
			editor.MoveUp()
		elif option == 4:
			editor.MoveDown()
		elif option == 5:
			editor.MoveRight()
		elif option == 6:
			editor.MoveLeft()
		elif option == 7:
			editor.GoToFirst()
		elif option == 8:
			editor.GoToLast()
		elif option == 9:
			print('Enter the new line:')
			line = input()
			editor.ReplaceLine(line)
		elif option == 10:
			print('Enter the new character:')
			char = input()
			editor.ReplaceChar(char)
		elif option == 11:
			editor.DeleteLine()
		elif option == 12:
			editor.DeleteChar()
		elif option == 13:
			print(editor)
		elif option == 14:
			editor.ClearFile()
		elif option == 15:
			editor.SaveFile()
		elif option == 16:
			break
		else:
			print('Invalid option!')
	

def TestTextEditor():
	editor = EditBuffer()
	print('\n===============================================================')
	print('\t\tWelcome To My Text Editor')
	print('===============================================================\n')
	while True:
		print('Please choose what you want to do:')
		print('1: Create a new file.')
		print('2: Edit a file.')
		print('3: Exit.')

		response = input()

		try:
			int(response)
		except ValueError:
			print('Please enter option in number.\n')
			continue
		else:
			response = int(response)

		if response == 1:
			print('Please Enter the file name you want to create:')
			FileName = input()
			editor.CreateNewFile(FileName)
			print('\nNewFile Created!')

			ShowOptions(editor)
			
		elif response == 2:
			print('Please Enter the file name you want to edit:')
			FileName = input()
			exitStatus = editor.EditFile(FileName)
			if exitStatus == -1:
				print(f'{FileName} file does not exits in directory!')
				continue

			ShowOptions(editor)

		elif response == 3:
			break 

		else:
			print('Invalid option!')
	print('Thank You!')



TestTextEditor()