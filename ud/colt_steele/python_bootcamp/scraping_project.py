import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import choice
import pyfiglet
from termcolor import colored
import nltk
# nltk.download('punkt')

quote_list = []


def set_up():
    url = "http://quotes.toscrape.com"
    pageno = 1
    while pageno < 11:
        targ = requests.get(f"{url}/page/{pageno}/")
        soup = BeautifulSoup(targ.text, "html.parser")
        mydivs = soup.select(".quote")
        for e in mydivs:
            quote_list.append([e.select(".text")[0].get_text(),
                               e.select(".author")[0].get_text(),
                               url + e.find('a', href=True)['href']])
        sleep(1)
        pageno += 1


def play_game():
    print(
        f"There are {len(quote_list)} quotations scraped from this site!  Here's one:")
    question_quote = choice(quote_list)
    print(question_quote[0])
    # guesses = 4
    the_answer = question_quote[1]
    # print(f"Secret answer: {the_answer}")
    answer1 = input("Who said it? ")

    if answer1 == the_answer:
        print("Congratulations!  Got it in one!")
        return True
    else:
        print("Sorry that's not correct")
        # guesses -= 1
        bio_list = get_bio(question_quote[2], the_answer)
        answer2 = input("Does that now ring a bell? ")
        if answer2 == the_answer:
            print("Congratulations!  Got it on the 2nd try!")
            return True
        else:
            # guesses -= 1
            print(
                f"Sorry that's not correct.  Their initials are {question_quote[1][0]}.{question_quote[1].split()[1][0]}.")
            answer3 = input("Does that now ring a bell? ")
            if answer3 == the_answer:
                print("Congratulations!  Got it on the 3rd try!")
                return True
            else:
                # guesses -= 1
                print(
                    "Sorry that's not correct.  Try again - here's a random fact about them:")
                print(choice(bio_list[3]))
                answer4 = input("How about now? ")
                if answer4 == the_answer:
                    print("Well done (just about!)")
                    return True
                else:
                    print(
                        f"Sorry, you're out of guesses.  The answer was: {the_answer}.")
                    return True


def get_bio(link, target):
    bio = requests.get(link)
    bio_soup = BeautifulSoup(bio.text, "html.parser")
    bio_list = []
    # bio_list.append(bio_soup.find(class_="author-title")) - doesn't work
    bio_list.append(bio_soup.select(".author-born-date")[0].get_text())
    bio_list.append(bio_soup.select(".author-born-location")[0].get_text())
    bio_list.append(bio_soup.select(".author-description")[0].get_text())
    bio_list[2] = bio_list[2].replace(target, "BLANK").replace(
        target.split(" ")[-1], "BLANK")
    bio_list.append(nltk.tokenize.sent_tokenize(bio_list[2]))
    print(f"This person was born on {bio_list[0]} {bio_list[1]}...")
    return bio_list

# Colt's version has cool implementation of if..elif...elif... for game logic based on remaining guesses.
# Also puts each quote into dictionary (within one list).
# And, if user wants another go, calls game function WITHIN the function
# Can save to a separate csv easily, and use that 
# Separate hint function?  Though possibly overkill

if __name__ == "__main__":
    set_up()
    user_input = ''
    # get_bio("http://quotes.toscrape.com/author/Albert-Einstein/") - for debugging

    while user_input != "q":
        play_game()
        user_input = input("Press any key to play again, or q to quit: ")

    print(colored(pyfiglet.figlet_format("Goodbye!"), "yellow"))
