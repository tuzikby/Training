from test_utils import *


def hackernews_menu():
    response = input("Please choose an option from below:\n" +
                     "1. Find article with highest number of comments\n" +
                     "2. Find article with the highest number of points\n" +
                     "3. First 10 articles about python\n"+
                     "4. Top 10 articles based on the number of comments\n")

    if response == "1":
        print(highest_num_comments())
    elif response == "2":
        print(highest_rating())
    elif response == "3":
        pretty_print(first_ten_python_articles())
    elif response == "4":
        pretty_print(top_ten_articles())
    else:
        print("there is no such option")


hackernews_menu()

response2 = "yes"
while response2 == "yes":
    response2 = input("Would you like to choose another option?\n")
    response2 = response2.lower()
    if response2 == "yes":
        hackernews_menu()
    else:
        print('Goodbye')
        break
