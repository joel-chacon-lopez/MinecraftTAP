# -*- coding: utf-8 -*-
import random
from agents.base_agent import MinecraftAgent

def log_interaction(func):
    def wrapper(self, question):
        self.say(f"Logging question: {question}")
        response = func(self, question)
        with open("oracle_log.txt", "a") as log_file:
            log_file.write(f"Q: {question} -> A: {response}\n")
        return response
    return wrapper

class OracleBot(MinecraftAgent):
    def __init__(self, name):
        super().__init__(name)
        self.responses = {
            "build": "Build a castle!",
            "explore": "Explore a cave!",
            "mine": "Find some diamonds!"
        }

    @log_interaction
    def generate_response(self, question):
        for keyword, response in self.responses.items():
            if keyword in question.lower():
                return response
        return "That's an interesting question!"

    def perform_action(self):
        self.say("Ask me something!")
        while True:
            posts = self.mc.events.pollChatPosts()
            for post in posts:
                question = post.message
                answer = self.generate_response(question)
                self.say(answer)
