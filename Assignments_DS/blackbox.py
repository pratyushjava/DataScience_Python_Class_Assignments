# Name- Pratyush Singh
# Programming Assignment #8



"""
this function accepts as a list of integers, and modifies it by removing any consecutive duplicates
"""
def remove_consecutive_duplicates(dup_list):
    index = 0
    # since we are checking equality of index and index +1, we limit the loop one less than the length of loop
    while index < len(dup_list)-1:
        # checking for consecutive duplicate
        if dup_list[index] == dup_list[index+1]:
            # delete if the duplicate found
            del dup_list[index]
        else:
            index = index+1


"""
general case test
"""
def test1():
    dup_list = [1, 2, 2, 3, 2, 2, 3]
    remove_consecutive_duplicates(dup_list)
    if(len(dup_list) == 5):
        if(dup_list[0] == 1 and dup_list[1] == 2 and dup_list[2] == 3 and dup_list[3] == 2 and dup_list[4] == 3):
            print("test1 pass")
        else:
            print("test1 fail")
    else:
        print("test 1 fail")




"""
test for all consecutive values but one
"""
def test2():
    dup_list = [1, 2, 2, 2,2,2,2]
    remove_consecutive_duplicates(dup_list)
    if(len(dup_list) == 2):
        if(dup_list[0] == 1 and dup_list[1] == 2):
            print("test2 pass")
        else:
            print("test2 fail")
    else:
        print("test 2 fail")




"""
test for empty list
"""
def test3():
    dup_list = []
    remove_consecutive_duplicates(dup_list)
    if(len(dup_list) == 0):
        print("test3 pass")
    else:
        print("test 3 fail")


"""
test for two continuous same values
"""
def test4():
    dup_list = [2, 2, 2, 3, 3, 3, 3]
    remove_consecutive_duplicates(dup_list)
    if(len(dup_list) == 2):
        if(dup_list[0] == 2 and dup_list[1] == 3):
            print("test4 pass")
        else:
            print("test4 fail")
    else:
        print("test 4 fail")


"""
test for all consecutive values
"""
def test5():
    dup_list = [4,4,4,4,4,4,4,4,4]
    remove_consecutive_duplicates(dup_list)
    if(len(dup_list) == 1):
        if(dup_list[0] == 4):
            print("test5 pass")
        else:
            print("test5 fail")
    else:
        print("test 5 fail")



"""
test for negative value
"""
def test6():
    dup_list = [-1,-1,-2,-2,-3,-3,-4]
    remove_consecutive_duplicates(dup_list)
    if(len(dup_list) == 4):
        if(dup_list[0] == -1 and dup_list[1] == -2 and dup_list[2] == -3 and dup_list[3] == -4):
            print("test6 pass")
        else:
            print("test6 fail")
    else:
        print("test 6 fail")



"""
execute test cases, there are total 6 test cases
"""
def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    
main()
    
