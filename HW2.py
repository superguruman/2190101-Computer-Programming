# HW02 (Don't delete this line or add any line above this line.)

def read_file(filename):
    # return a list of lines 
    lines = []
    fn = open(filename,"r")
    for line in fn:
        lines.append(line.rstrip("\n"))
    fn.close()  
    return lines

def write_file(lines, filename):
    # return nothing, write all lines to filename
    fn = open(filename, "w")
    for i in range(len(lines)):
        fn.write(lines[i] + "\n")
    fn.close()

def vi_editor(lines, commands):
	# Write your code here
	x=0
	y=0
	last_command=""
	insert_mode=False
	text=[]
	for i in range(len(commands)):
		if commands[i] == 'l' and insert_mode == False: #Moves to the right
			x+=1
		if x > len(lines[y]): #If the cursor hits the right limit, goes back by 1
			x-=1
		if y > len(lines): #If the cursor hits the bottom limit, goes back by 1
			y-=1
		elif commands[i] == 'h' and x != 0 and insert_mode == False: #Moves to the left unless it's at the left limit
			x-=1
		elif commands[i] == 'j' and insert_mode == False: #Moves downward
			y+=1
		elif commands[i] == 'k' and y != 0 and insert_mode == False: #Moves upward unless it's at the top limit
			y-=1
		elif commands[i] == 'D' and insert_mode == False: #Deletes the rest of the sentence
			lines[y] = lines[y][:x]
		elif commands[i] == 'x' and insert_mode == False: #Removes the character at cursor
			lines[y] = lines[y][:x] + lines[y][x+1:]
		elif commands[i] == 'i' and insert_mode == False: #Opens insert mode and remembers the command "i"
			insert_mode = True
			last_command = commands[i]
		elif commands[i] == 'o' and insert_mode == False: #Opens insert mode and remembers the command "o"
			insert_mode = True
			last_command = commands[i]
		if commands[i:i+5] == '[Esc]' or (i == len(commands)-1 and (last_command == 'o' or last_command == 'i')) : #If detect "[Esc]" or hits the last letter in commands while in "o" or "i" command, close the insert_mode
			insert_mode = False
			if i == len(commands)-1 and (last_command == 'o' or last_command == 'i'): #Adds the last character since if it hits the last letter in commands, it won't add the last character into text list.
				text.append(commands[i])
			if last_command == 'i': #command = "i", pop the first letter (which is the command) and add text at the cursor
				text.pop(0)
				lines[y] = lines[y][:x] + "".join(text) + lines[y][x:]
			elif last_command == 'o': #command = "o", pop the first letter (which is the command) and insert the text as new line at the line above.
				text.pop(0)
				lines.insert(y, "".join(text))
			x+=len(text) #adjust the cursor to be at the end of the added text
			text = [] #reset the text
			last_command=""
		if insert_mode == True: #add the character after enabling insert mode
			text.append(commands[i])

	return lines

### TEST CASE ###
#Disclaimer: The last 2 commands are supposed to be "xx" instead of "dd" from the test case in the collab since the output is expected to be 'TheThe newly addquick brown fox' (remove 2 characters, which is xx).
lines = read_file('data.txt')
commands = "lllxiThe newly added[Esc]hhhxx"
vi_editor(lines, commands)
write_file(lines, 'edited_data.txt')

if __name__ == "__main__":

    test_lines = [
        ["The quick brown fox", "jumps over the lazy dog"],
        ["The quick brown fox", "jumps over the lazy dog"],
        ["The quick brown fox", "jumps over the lazy dog"]
    ]

    test_commands = [
        "lllD",
        "joThis is the new line",
        "lllxiThe newly added[Esc]hhhxx"
    ]

    test_output = [
        ["The", "jumps over the lazy dog"],
        ["The quick brown fox", "This is the new line", "jumps over the lazy dog"],
        ['TheThe newly addquick brown fox', 'jumps over the lazy dog']
    ]

    for i in range(len(test_lines)):
        lines = test_lines[i]
        commands = test_commands[i]
        output = test_output[i]
        result = vi_editor(lines, commands)
        
        if result == output:
            print("Test case {} passed!".format(i+1))
        else:
            print("Test case {} failed!".format(i+1))
            print("Expected output: \t{}".format(output))
            print("Your output: \t\t{}".format(result))

        print("\n")