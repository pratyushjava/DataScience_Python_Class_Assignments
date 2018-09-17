# Name- Pratyush Singh
# Programming Assignment #10



"""
    this program gives the recommendations for the user for the books
    this program also need review.py and ratings.txt.
    input the rating file name first when program prompt  
    user need to choose the option recommend, best, add, quit to perform actions
"""
from review import Review 

"""
    function will load all the reviews for all user from the file input by the user
"""
def read_ratings(reviews,filename):
    # open the file and read lines
    f = open(filename)
    all_lines = f.readlines()
    f.close()    
    # clean the lines-> extra spaces or blank lines
    lines = []
    for i in range(0,len(all_lines)):
        all_lines[i] = all_lines[i].rstrip()
        if(len(all_lines[i]) > 0):
            lines.append(all_lines[i].strip())  
    # fill the dictionary where key is user name and value as set of review objects.
    for i in range(0, int(len(lines)/4)):
        i = i * 4  # there are 4 lines for each review so we need 4 steps
        if lines[i].lower() not in reviews: # if user is not already present add the user first
            reviews[lines[i].lower()] = set() 
        reviews[lines[i].lower()].add(Review(lines[i+1].lower(),lines[i+2].lower(),lines[i+3].lower())) # add reviews in user set


"""
    this function just print the options to the user
"""
def print_menu():
    print("Welcome to the CSC110 Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("best      : the book with the highest rating among all users")
    print("add       : add a new book")
    print("quit      : exit the program")


"""
    called when user choose the recommend option 
    creating a map of users to distances form the user you are trying to make a recommendation for.
"""
def compute_distance_similarity(reviews, distance, user):
    """
       go through your dictionary that maps users to their reviews 
       For each of those reviews go through all of the reviews of the user you are trying to make a recommendation for
       if the book titles are the same, multiply the ratings of the two users and add them to the similarity score
    """
    similarity = 0  
    for u in reviews: 
        if u != user: # not for same user
            # go through user review
            for review in reviews[u]:
                for user_review in reviews[user]:
                    # if title is same compute the similarity measure
                    if(review.get_title() == user_review.get_title()):
                        similarity += review.get_rating() * user_review.get_rating()
                        break; # once the title is found don't go further
            distance[u] = similarity
            similarity = 0

"""
   called when user choose the recommend option, calculate recommendations for a particular user
"""
def recommendation(reviews , user):
    # dictionary for storing distance between users
    distance = dict()    
    # compute similarity between between users
    compute_distance_similarity(reviews, distance, user)
    # find the most similar user    
    near_user = max(distance, key=distance.get)
    """
        from the similar user Output all of the books that he has read and rated a positive number 
        that the person you are trying to make a recommendation for hasnt
    """
    show_review = True
    for review in reviews[near_user]:
        for user_review in reviews[user]:
            if(review.get_title() == user_review.get_title()): # if the titles are same then don't show
                show_review = False
                break
        if show_review and review.get_rating() > 0: # rating should also be greater than 0
                print(review.__str__())
        show_review = True


"""
    called when user chooses the best option
    create another dictionary mapping the title of each book to a tuple containing the sum of all of its ratings 
    and the number of ratings
"""
def get_total_ratings(books_ratings, reviews):
    # go through all the users
    for u in reviews: 
        # go through all the reviews of each user.
        for review in reviews[u]: 
            # get the title for this review.
            title = review.get_title()     
            if title not in books_ratings:  # if title not already present add it to dictionary
                books_ratings[title] = (review.get_rating(), 1) 
            else: # increment when title found again
                books_ratings[title] = (books_ratings[title][0] + review.get_rating() , books_ratings[title][1] + 1)


"""
    called when user chooses the best option 
    gives best book according to ratings
"""
def get_best_book(books_ratings):
    """
    loop over the dictionary to find the book with the highest average review 
    ( average is given by dividing sum of all ratings by number of ratings).
    """
    best_title = ""
    overall_score = -1
    for title in  books_ratings:
        average = books_ratings[title][0] / books_ratings[title][1] # get the average
        if (average > overall_score): # if the average is max set this as max
            overall_score = average
            best_title = title      # set the max average book as best book
    return (best_title,overall_score)


"""
   called when user chooses the best option 
"""
def show_best_book(reviews):
    # dictionary mapping the title of each book to a tuple containing the sum of all of its ratings
    books_ratings = dict()   
    # get the books ratings by all users        
    get_total_ratings(books_ratings, reviews)
    # get the best book
    best_book = get_best_book(books_ratings)
    # print the best book
    print("The highest rated book is:")
    print(best_book[0])
    print("with an overall score of ", best_book[1])

"""
    add new review inputed by the user to the dictionary
"""
def add_new_book(reviews,  review, user):
    if user not in reviews:
        reviews[user] = set()
    reviews[user].add(review)


"""
   controler of the program continues till user choose to quit
"""
def start_application(reviews):
    command = input("next task?") # ask the user for option
    while(command != "quit"):     # do until user choose to quit
        if command.lower() == "recommend": # give recommendations
            user = input("user?").lower().strip() # strip extra spaces
            if user in reviews: # user should be present in dictionary to get recommendations
                recommendation(reviews , user)
        elif command.lower() == "best":  # get best book
            show_best_book(reviews)
        elif command.lower() == "add":  # add new review to the dictionary
            user = input("user?").lower().strip() # get user name
            title = input("title?").lower().strip() # get title
            author = input("author?").lower().strip() # get author name
            rating = input("rating?").lower().strip() # get rating for review
            add_new_book(reviews,Review(title,author,rating), user) # add the review to dictionary
        command = input("next task?")


"""
    gives the summary of program simple and short
"""
def main():
    reviews = dict()
    print("Enter the name of file")
    filename = input()
    read_ratings(reviews,filename)
    print_menu()
    start_application(reviews)
    print("Good Bye!!")

main()
