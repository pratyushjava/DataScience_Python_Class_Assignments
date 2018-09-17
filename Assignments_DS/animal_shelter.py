# Name- Pratyush Singh
# Programming Assignment #8


'''
This program focuses on using lists that change size and also demonstrates a
type of program that maintains data in a manner useful in supporting typical volunteer organizations.
In this assignment we have written a program that keeps track of animals at an animal shelter.
'''

# constant for file names
pets_file = "pets.txt"
transferred_file = "transferred.txt"
adopted_file = "adopted.txt"

"""
Print the option menu for the user
"""
def print_options():
    
    print("Type one of the following options:")
    print("adopt: adopt a pet")
    print("intake: add more animals to the shelter")
    print("list: display all adoptable pets")
    print("quit: exit the program")
    print("save: save the current data")
    print("transfer: transfer pets to another shelter")


"""    
read from the file. input = filename , output = list of tuples for each line
"""
def read_pet_from_file(input_file, tlist):
    # open file and get its handel
    in_file = open(input_file)
    # read all lines of the file
    file_lines = in_file.readlines()
    # close the file
    in_file.close()
    for t in file_lines:
        # split the line by " "
        t = t.split(" ")
        # swap the values inside tuple, to make sorting possible
        tlist.append((t[1].strip(), t[2].strip(), t[0].strip()))



"""
main: controler of program display summary of program
"""
def main():
    # Empty list for each file
    pets_tlist = []
    transferred_tlist = []
    adopted_tlist = []
    
    # get list of tuples from pet file
    read_pet_from_file(pets_file, pets_tlist)
    # get list of tuples from transfered file
    read_pet_from_file(transferred_file, transferred_tlist)
    # get list of tuples from adopted file
    read_pet_from_file(adopted_file, adopted_tlist)
    # print option for user
    print_options()
    # receive the option from the input
    option = input("option? ")
    while(option.lower() != "quit"):
        
        if(option.lower() == "adopt"):
            adopt_pet(pets_tlist, adopted_tlist)
            adopted_tlist.sort()
            pets_tlist.sort()
        elif(option.lower() == "intake"):
            intake_pet(pets_tlist)
            pets_tlist.sort()
        elif(option.lower() == "list"):
            list_pet(pets_tlist)
        elif(option.lower() == "save"):
            save_pet(pets_tlist, transferred_tlist, adopted_tlist)
        elif(option.lower() == "transfer"):
            transfer_pet(pets_tlist, transferred_tlist)
            
        # print option for user
        print_options()
        # receive the option from the input
        option = input("option? ")
    print(str(len(pets_tlist))+ " pets currently in the shelter" )
    print(str(len(adopted_tlist))+ " adopted_tlist" )
    print(str(len(transferred_tlist))+ " transferred" )
    print(pets_tlist)
    print(adopted_tlist)
    print(transferred_tlist)
    
    
"""
This function will prepare the user prompt msg string.
it has all the types of pet in the string
"""
def get_prompt_string(pets_tlist):
    pet_type = []
    # get the types of pet to prompt to the user
    for tpl in pets_tlist:
        if tpl[2] not in pet_type:
            pet_type.append(tpl[2])
    type_prompt = ""   
    pet_type.sort()
    
    # create prompt string to the user to ask for type of pet
    for pet in pet_type:
        type_prompt += pet
        type_prompt += " or "
    type_prompt = type_prompt[:-4]
    return type_prompt
    
"""
given pet should be removed from the shelter and added to the list of pets that have been adopted
"""
def adopt_pet(pets_tlist, adopted_tlist):
    # get the string to prompt to the user on the basis of types of pet present in the list
    type_prompt = get_prompt_string(pets_tlist)
    type_prompt += "?"
    type = input(type_prompt)
    name = input("name?")
    
    # check if the pet present in the list if yes move it to the adopted list
    for tpl in pets_tlist:
        if(tpl[0].lower() == name.lower() and tpl[2].lower() == type.lower()):
            pets_tlist.remove(tpl)
            adopted_tlist.append(tpl)
            return
        
    print("Not Found!!")
    return
            
    
"""
add all of the pets from intake file to the shelter list
"""
def intake_pet(pets_tlist):
    # get input file name
    intake_file = input("file name?")
    intake_tlist = []
    # read intake  file data
    read_pet_from_file(intake_file, intake_tlist)
    # extend shelter list with the intake list
    pets_tlist.extend(intake_tlist)
    # after adding again sort the shelter list because intake list element are added at  last
    pets_tlist.sort()
    
"""
The program should then display a list of all pets at the shelter of the given type of pet
"""    
def list_pet(pets_tlist):
    # get the string to prompt to the user on the basis of types of pet present in the list
    type_prompt = get_prompt_string(pets_tlist)
    type_prompt += " or all?"
    # get the input of the type of pet to be displayed from the shelter list
    list_pet_type = input(type_prompt)
    if(list_pet_type.lower() == "all"):
        for t in pets_tlist:
            print(t)
    else:
        for t in pets_tlist:
            if(t[2].lower() == list_pet_type.lower()):
                print(t)

"""
conversion from list to string
"""
def list_to_string(lists):
    string_ls = ' '.join(lists)
    return string_ls


"""
reorder the tuples so that they can be saved in a file in which they were read
"""
def reorder_tuples_to_save(tpllist):
    newtpllist = []
    for t in tpllist:
        newtpllist.append((t[2], t[0], t[1]))
    tpllist.clear()
    tpllist.extend(newtpllist)

"""
saves data to respective files
"""
def save_pet(pets_tlist, transferred_tlist, adopted_tlist):
    # reorder the list as it was read from the file
    reorder_tuples_to_save(pets_tlist)
    reorder_tuples_to_save(transferred_tlist)
    reorder_tuples_to_save(adopted_tlist)
    
    # write each line in file
    with open(pets_file, 'w') as f:
        for t in pets_tlist:
            f.write((list_to_string(t))+'\n')
    
    # write each line in file
    with open(transferred_file, 'w') as f:
        for t in transferred_tlist:
            f.write((list_to_string(t))+'\n')
    
    # write each line in file  
    with open(adopted_file, 'w') as f:
        for t in adopted_tlist:
            f.write((list_to_string(t))+'\n')



"""
move all of the pets listed in the file inputed by the user out of the shelter and into the transferred list
"""
def transfer_pet(pets_tlist, transferred_tlist):
    to_transferlist = []
    # get the file name for transfer
    to_transfer_file = input("file name?")
    # read data to transfer
    read_pet_from_file(to_transfer_file, to_transferlist)
    # remove data from shelter list and add to the transferred list
    for t in to_transferlist:
        if t in pets_tlist:
            pets_tlist.remove(t)
            transferred_tlist.append(t)
    transferred_tlist.sort()
    pets_tlist.sort()


main()


