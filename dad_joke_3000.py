from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
from random import choice
import requests
init()

def print_greeting():
	greeting = figlet_format("DAD JOKE 3000")
	print_color = choice(["red", "cyan", "green"])
	greeting = colored(greeting, color = print_color, on_color = "on_white")
	print(greeting)

def accepts_topic():
	topic = input("Let me tell you a joke! Give me a topic: ")
	return topic

def conducts_search(topic):
	url = "http://icanhazdadjoke.com/search"
	search_results = requests.get(
		url,
		headers = {"Accept": "application/json"},
		params = {"term": topic}
	)
	search_results = search_results.json()
	return search_results["results"]
	
def makes_list_of_jokes(search_results):
	number_of_jokes = len(search_results)
	print(f"I found {number_of_jokes} jokes about your topic, {topic}. Here is one: ")
	list_of_jokes = []
	for result in search_results:
		list_of_jokes.append(result["joke"])
	return(list_of_jokes)
	
def picks_joke(list_of_jokes):
	picked_joke = choice(list_of_jokes)
	print(picked_joke)

def single_joke_printer(search_results):
	print(f"I only have one joke about your topic, {topic}. Here it is:  ")
	print(search_results[0]["joke"])

print_greeting()
while True:
	global topic
	topic = accepts_topic()
	search_results = conducts_search(topic)
	if len(search_results) > 1:
		list_of_jokes = makes_list_of_jokes(search_results)
		picks_joke(list_of_jokes)
	if len(search_results) == 1:
		single_joke_printer(search_results)
	if len(search_results) == 0:
		print(f"Sorry, I couldn't find any jokes about your topic, {topic}.")
	will_to_go_on = input("Do you want me to tell you another joke? ")
	will_to_go_on.lower()
	if will_to_go_on in ["no", "n", "nope", "nah"]:
		break