import sys

#The function to find neighbours of given row and column numbers
def neighbours(row_input,column_input,rows_list):
    wanted_number=rows_list[row_input][column_input] #Define the searching number
    neighbours_list=[] #The empty list to append neighbour numbers' indexes
    same_numbers=[] #The empty list to append the numbers that equal to wanted_number from rows_list
    if wanted_number=='N': #If wanted_number is equal to 'N' this square looks like space to user
        return neighbours_list
    
    for col in range(len(rows_list[0])):
        for row in range(len(rows_list)):
            if rows_list[row][col]==wanted_number: 
                same_numbers.append([row,col])
    current_numbers=[[row_input,column_input]] #Determine the numbers will be processed
    #Control values are determined to stop the function
    control_same_numbers=False 
    control_last_element_appended=False
    while control_same_numbers==False and control_last_element_appended==False:
        lenght_current_numbers=len(current_numbers)
        lenght_same_numbers=len(same_numbers)
        for rc in current_numbers:
            if rc == current_numbers[-1]: 
                control_last_element= True #Check if the controled rc is the last element
            if rc[0]>0: #Check if the board exceeded from upward
                for element in same_numbers:
                    if element == [rc[0]-1,rc[1]]:    
                        if [rc[0]-1,rc[1]] not in neighbours_list:               
                            current_numbers.append([rc[0]-1,rc[1]])                
                            neighbours_list.append([rc[0]-1,rc[1]])
            if rc[0]<len(rows_list): #Check if the board exceeded from downward
                for element in same_numbers:
                    if element == [rc[0]+1,rc[1]]:
                        if [rc[0]+1,rc[1]] not in neighbours_list:
                            current_numbers.append([rc[0]+1,rc[1]])
                            neighbours_list.append([rc[0]+1,rc[1]])
            if rc[1]>0: #Check if the board exceeded from leftside
                for element in same_numbers:
                    if element == [rc[0],rc[1]-1]:
                        if [rc[0],rc[1]-1] not in neighbours_list:
                            current_numbers.append([rc[0],rc[1]-1])
                            neighbours_list.append([rc[0],rc[1]-1])

            if rc[1]<len(rows_list[0]): #Check if the board exceeded from rightside
                for element in same_numbers:
                    if element == [rc[0],rc[1]+1]:
                        if [rc[0],rc[1]+1] not in neighbours_list:
                            current_numbers.append([rc[0],rc[1]+1])
                            neighbours_list.append([rc[0],rc[1]+1])
        current_numbers=current_numbers[lenght_current_numbers:] #Only new current numbers retain
        if len(current_numbers)==0 and control_last_element==True: #If there is no current numbers to check and last element is checked stop the loop
            control_last_element_appended=True    
        if lenght_same_numbers==len(neighbours_list): #If there is no element in same_numbers to check stop the loop
            control_same_numbers=True
    return neighbours_list

#The function to convert neighbours to 'N' chararacter
def none_convertion(row_input,column_input,rows_list):
    neighbours_list_indexes=neighbours(row_input,column_input,rows_list)
    for element in neighbours_list_indexes:
        rows_list[element[0]][element[1]]='N'
    return rows_list

#The function to delete neighbours and move remain items according to game rules
def move_items(rows_list):
    none_column_indexes=[] #The empty list to append column number if there is 'N' character in that column
    column_to_be_deleted=[] #The empty list to append column number if there is no element in that column 
    for col in range(len(rows_list[0])):
        for i in range(len(rows_list)):
            if rows_list[i][col]=="N":
                none_column_indexes.append(col)
    for col in range(len(rows_list[0])):
        count=none_column_indexes.count(col) #Compute the number of 'N' characters in one column
        if count==0: #Check if the column include 'N' character
            continue
        if count!=0:
            if count==len(rows_list): #Check if the column's all elements are equal to 'N' character
                column_to_be_deleted.append(col)
            else:
                important_list=[] #The empty list to move element that are not equal to 'N' downward
                for row in range(len(rows_list)):
                    important_list.append(rows_list[row][col]) 
                important_list=[element for element in important_list if element!="N"]
                none_list=["N"]*count 
                important_list=none_list+important_list #'N' characters appended to beginning of column
                for index in range(len(important_list)):
                    rows_list[index][col]=important_list[index] #Change the rows_list according to new list 
                none_list=[] #Change the list to empty list to use again
    if column_to_be_deleted!=[]:
        for element in column_to_be_deleted[::-1]: #Reversed the list to not change indexes before the process
            for row in rows_list:
                del row[element]
    control_list_to_rows=[] #The empty list to check if the row should be deleted
    rows_to_be_deleted=[]
    for row in rows_list:
        for i in range(len(row)):
            if row[i]=='N':
                control_list_to_rows.append(row[i])
        if row==control_list_to_rows:
            rows_to_be_deleted.append(row)
        control_list_to_rows=[]
    for element in rows_to_be_deleted[::-1]: #Reversed the list to not change indexes before the process
        rows_list.remove(element)

    return rows_list

#The function to convert 'N' characters into spaces
def list_to_game(rows_list):
    solution_board="" #The empty string to append board for user's screen
    for row in move_items(rows_list):
        n_indexes=[index for index, element in enumerate(row) if element=='N'] #Appended 'N' character's indexes to convert them spaces
        if n_indexes!=[]:
            for index in n_indexes:
                row.pop(index)
                row.insert(index," ")
                row_string=" ".join(row)
            solution_board+=row_string+"\n"
        else:
            row_string=" ".join(row) # If there is no 'N' character don't convert
            solution_board+=row_string+"\n"
    return solution_board

#The function to convert spaces into 'N' characters to use this board again
def spaces_to_n(rows_list):
    for row in rows_list: 
        n_indexes=[index for index, element in enumerate(row) if element==' ']
        if n_indexes!=[]:
            for index in n_indexes:
                row.pop(index)
                row.insert(index,"N")        
    return rows_list

#The function to play game according to rules
def play_game(board,rows_list):
    score=0 #Assigned 0 to score to add new scores while playing
    print(board,"\n")
    print("Your score is: ",score,"\n")
    control_value=False #Assigned to determine current step is first step or not
    while True:
        if rows_list==[]: #If there is no element to remove it means game over stop the loop
            print("Game over\n")
            return rows_list
        movement_control_list=[] #The empty list to append elements that have neighbours
        for row in range(len(rows_list)):
            for column in range(len(rows_list[0])):
                if neighbours(row,column,rows_list)!=[]:
                    movement_control_list.append([row,column])
        if len(movement_control_list)==0: #If there is no element have neighbours it means game over stop the loop
            print("Game over\n")
            return rows_list
        input_numbers=input("Please enter a row and a column number: ")
        print()
        row_input,column_input=input_numbers.split()
        #Convert the input numbers into suitable for list indexes
        row_input=int(row_input)-1 
        column_input=int(column_input)-1
        #Check if given indexes exceed the board
        if row_input>len(rows_list) or row_input<0 or column_input>len(rows_list[0]) or column_input<0 or rows_list[row_input][column_input]=='N':
            print("Please enter a correct size! \n")
            continue
        #Check if the number that addresed on given indexes have neighbours
        if neighbours(row_input,column_input,rows_list)==[]:
            print("No movement happened try again \n")
            if control_value==False: #Checked if the current step is first step
                print(board) #If it is first step print first board
                print("Your score is:",score,"\n")
            else:
                print(game_board) #If it is not first step print processed board
                print("Your score is:",score,"\n")
            continue
        wanted_number=rows_list[row_input][column_input] #Assigned to compute the score of user
        control_value=True #The first step is finished
        neighbours(row_input,column_input,rows_list) #Determine the neighbours
        neighbours_count=len(neighbours(row_input,column_input,rows_list)) #Assigned to compute the score of user
        none_convertion(row_input,column_input,rows_list) #Convert neighbours to 'N'
        move_items(rows_list) #Move items according to given rules
        if rows_list!=[]:
            game_board=list_to_game(rows_list) #Assigned to use later
            print(game_board) 
            spaces_to_n(rows_list) #Convert spaces to 'N' character again to use this board again
        score+= neighbours_count*int(wanted_number) 
        print("Your score is:",score,"\n")
              
    return rows_list

def main():
    input_file=open(sys.argv[1],"r") 
    board=input_file.read()
    input_file.close()
    rows=board.split("\n")
    cleaned_list = [''.join(item.split()) for item in rows]
    rows_list=[list(cleaned_list[i]) for i in range(len(cleaned_list))] #Convert the input into a two dimensional list
    input_file.close
    play_game(board,rows_list)

if __name__=="__main__":
    main()