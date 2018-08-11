# Allows the user to search jokes from http://icanhazdadjoke.com/search
from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
from random import choice
import requests
init()


def print_greeting():
    """ Prints the decorative greeting message """
    greeting = figlet_format(
        "DAD JOKE 3000")  # Uses the figlet_format() method from the pyfiglet module to create art from the text "DAD JOKE 3000"
    # Picks a random color from the available options to later use as the text
    # color
    print_color = choice(["red", "cyan", "green"])
    # Uses the colored() method from the termcolor module to color the text in
    # the randomly selected colour, and the background white
    greeting = colored(greeting, color=print_color, on_color="on_white")
    print(greeting)


def accepts_topic():
    """Prompts the user to enter the topic that they would like the joke to be about, and returns it"""
    topic = input("Let me tell you a joke! Give me a topic: ")
    return topic


def conducts_search(topic):
    """Searches the website for the user's topic and returns a list of the joke containing their search term"""
    url = "http://icanhazdadjoke.com/search"
    search_results = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": topic}
    )
    # The "headers" part ensures that the response contains json
    # The "params" part searches by the topic that the user entered
    search_results = search_results.json()  # Converts from json to python
    print(search_results)
    # At this point, search_results is a dictionary, containing the search results, the current page, the limit on search results, and more.
    # We only want the "results" part of this dictionary
    # Returns only the "results" part of the dictionary. The key "results" is
    # paired with a *list* containing the results. Each result contains the
    # joke and its ID
    return search_results["results"]


def makes_list_of_jokes(search_results):
    """Takes the list of results and returns a list of only the joke (discarding the ID) """
    number_of_jokes = len(search_results)
    # Prints a message telling the user how many jokes there are about their
    # topic
    print(
        f"I found {number_of_jokes} jokes about your topic, {topic}. Here is one: ")
    list_of_jokes = []
    for result in search_results:
        list_of_jokes.append(result["joke"])
    # This adds the joke from each result to list_of_jokes. The IDs are
    # ignored.
    return(list_of_jokes)


def picks_joke(list_of_jokes):
    """Picks one of the jokes from the list at random, and prints it. Runs if there is more than one joke"""
    picked_joke = choice(list_of_jokes)
    print(picked_joke)


def single_joke_printer(search_results):
    """In the case of there being only a single result, the joke is printed """
    print(f"I only have one joke about your topic, {topic}. Here it is:  ")
    print(search_results[0]["joke"])
    # At this point, search_results is still a list of the results, including IDs
    # The [0] is to target the first (and only) result in the list
    # The ["joke"] targets the value paired with the key ["joke"], as opposed
    # to the other key (["ID"])


print_greeting()
while True:  # Continues to run in a loop until the user decides that they don't want to play anymore, and the loop breaks
    global topic  # topic is made global so that it can be accessed inside of the functions
    topic = accepts_topic()
    # Sets the value of search_results equal to the value returned by the
    # function conducts_search
    search_results = conducts_search(topic)
    if len(search_results) > 1:
        # If there is more than one search result, a list must be made, and a
        # random joke picked from the list
        list_of_jokes = makes_list_of_jokes(search_results)
        picks_joke(list_of_jokes)
    # If there is only one search result, the joke can simply be printed.
    elif len(search_results) == 1:
        single_joke_printer(search_results)
    elif len(search_results) == 0:  # If there are no jokes, a message is displayed
        print(f"Sorry, I couldn't find any jokes about your topic, {topic}.")
    will_to_go_on = input("Do you want me to tell you another joke? ")
    will_to_go_on.lower()
    # If the user enters one of these, the loop breaks.
    if will_to_go_on in ["no", "n", "nope", "nah"]:
        break
