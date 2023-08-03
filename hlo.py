# Python : is a simple, gernal purpose, hight level, object oriented, interpreted, dyanmiclly typed, case senstive languguage...

# web devlopment
# mobiles app backed
# AI(Machine learnig, Data Science/..)


# low level language....

# 0 1


# object oriented
# OOPs:
# 1) inharitance
# 2) polymorphisum
# 3) abstraction
# 4) encapsulation....



# type of lanagus:
# 1) complied type
# 2) interpreted..


# Dyanmiclly typed language...



# case senstive:


# a = 10

# A = 10


# Variables::::::

# a = 10



# print("the vale is: ",a)

# rules::
# 1) Variable always start from alphabet or underscore.



# aa = 10
# _a = 10

# 2) Variable never start from integer or symbole.

# a12 = 10



# print("Hello word !")

# input()  = >  to take input form user.....

# a = input("PLease enter your name : ")

# print("user entered his/her name : ", a)

# a = 10
# b = 20
# c = "this is string.."
# d = 10.1
# check data type::::

# type()
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# python Comments::::::

# 1) single line comment:
# 2) multiline comment:

"""
    ajsbasldjbajsd
    asdasdkad
    asdbkasd
    aksdkbksdbja

"""

import random
import re

class RuleBot:
    def __init__(self):
        self.negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
        self.exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
        self.random_questions = (
            "Why are you here?",
            "Are there many humans like you?",
            "What do you consume for sustenance?",
            "Is there intelligent life on this planet?",
            "Does Earth have a leader?",
            "What planets have you visited?",
            "What technology do you have on this planet?"
        )
        self.alienbabble = {
            'describe_planet_intent': r'.\s*your planet.',
            'answer_why_intent': r'why\sare.*',
            'about_intellipat': r'.*\s*intellipaat'
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am Transformer. Will you help me learn about your planet?\n")
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice Earth day!")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipat':
                return self.about_intellipat()
        if not found_match:
            return self.no_match_intent()

    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and species.\n",
                     "I am Transformer, the capital of the Wayward galaxies.\n")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("I come in peace.\n", "I am here to collect data on your planet and its inhabitants.\n",
                     "I heard the coffee is good.\n")
        return random.choice(responses)

    def about_intellipaat(self):
        responses = ("Intellipaat is the world's largest professional educational company.\n",
                     "Intellipaat will help you learn concepts in a way you've never learned before.\n",
                     "Intellipaat is where your career and skills grow.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Please tell me more.\n", "Tell me more!\n", "Why do you say that?\n",
            "I see. Can you elaborate?\n",
            "Interesting. Can you tell me more?\n", "I see. How do you think?\n", "Why?\n",
            "How do you think I feel when you say that?\n")
        return random.choice(responses)

# Create an instance of the RuleBot class and start the conversation
alienbot = RuleBot()
alienbot.greet()