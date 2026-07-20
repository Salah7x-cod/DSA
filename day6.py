from click import command


if __name__ == '__main__':
    N = int(input())
    my_list = []

    #FOR each of #FOR each of the n lines:
    for _ in range(N): 
        #Read the command line as a string
        command_line = input().split()
        #Split the string into parts (words)
        command = command[0]
        #IF first word == "insert":
        if command_name == "insert":
            #position = second word (convert to int)
            i = int(command_line[1])
            #value = third word (convert to int)
            e = int(command_line[2])
            #insert value at position in my_list
            my_list.insert(i, e)
        #ELSE IF first word == "print":
        elif command == "print":
            #print my_list
            print(my_list)
        #ELSE IF first word == "remove":
            #value = second word (convert to int)
            #remove first occurrence of value from my_list

        #ELSE IF first word == "append":
            #value = second word (convert to int)
            #append value to my_list

        #ELSE IF first word == "sort":
            #sort my_list

        #ELSE IF first word == "pop":
            #remove last element from my_list

        #ELSE IF first word == "reverse":
            #reverse my_list

    #END FOR
