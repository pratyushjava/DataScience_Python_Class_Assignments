# Name- Pratyush Singh
# Programming Assignment #1

#
# This program performs the elimination of the redundancy. 
# This programs contains a fuction for each verse 
# This program's purpose is to test functions and print statements.
# This program outputs the cumulative song.
# The sixth verse is coustomized to rhyme with the rest.

def main():
    verse_1() 
    verse_2() 
    verse_3() 
    verse_4() 
    verse_5() 
    verse_6() 
    end_verse() 


def die(): 
    print("I don't know why she swallowed that fly,")
    print("Perhaps she'll die.")
    print()

def spider():
    print("She swallowed the spider to catch the fly,")
    die()
    
def bird():
    print("She swallowed the bird to catch the spider,")
    spider()
    
def cat():
    print("She swallowed the cat to catch the bird,")
    bird()
    
def dog():
    print("She swallowed the dog to catch the cat,")
    cat()
    
def verse_1():
    print("There was an old woman who swallowed a fly.")
    die()
    
def verse_2():
    print("There was an old woman who swallowed a spider,")
    print("That wriggled and iggled and jiggled inside her.")
    spider()
    
def verse_3():
    print("There was an old woman who swallowed a bird,")
    print("How absurd to swallow a bird.")
    bird()
    
def verse_4():
    print("There was an old woman who swallowed a cat,")
    print("Imagine that to swallow a cat.")
    cat()
    
def verse_5():
    print("There was an old woman who swallowed a dog,")
    print("What a hog to swallow a dog.")
    dog()
    
def verse_6():
    print("There was an old woman who swallowed a panther,")
    print("Its a wonder that she swallowed a panther.")
    print("She swallowed the panther to catch the dog,")
    dog()
       
def end_verse():
    print("There was an old woman who swallowed a horse,")
    print("She died of course.")

main()    
