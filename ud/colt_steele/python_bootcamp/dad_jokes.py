import requests
from random import randint, choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("Welcome to Dad Jokes 5000!")

print(colored(header, "cyan"))


def joke_finder():
    joke_term = input("What topic would you like to search jokes on? ")
    url = f"https://icanhazdadjoke.com/search?page=1&term={joke_term}"
    x = requests.get(url, headers={'Accept': 'application/json'})
    joke_dict = x.json()
    if joke_dict['total_jokes'] == 0:
        print(f"I'm sorry we've got nothing on {joke_term}.")

    else:
        jokes = [j['joke'] for j in x.json()['results']]
        print("------------")
        print(f"Thanks!  Here's a {joke_term} joke coming up")
        print(choice(jokes))


user_input = ""
while user_input != "q":
    joke_finder()
    user_input = input("Press any key to try another joke, or q to quit: ")

print(colored(pyfiglet.figlet_format("Goodbye!"), "yellow"))

# Added pyfiglet and choice as per Colt Steele's walkthrough
