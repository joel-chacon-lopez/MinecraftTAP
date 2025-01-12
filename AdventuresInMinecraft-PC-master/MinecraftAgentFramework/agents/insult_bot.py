# -*- coding: utf-8 -*-
import random
from agents.base_agent import MinecraftAgent
import time

class InsultBot(MinecraftAgent):
    def __init__(self, name):
        super().__init__(name)
        self.insults = [
            "asshole",
            "noob",
            "draft cow",
            "maggot",
            "loser"
        ]

    def insult(self):
        insult = random.choice(self.insults)
        self.say(insult)

    def perform_action(self):
        self.say("Type 'list_methods' in chat to see what I can do!")
        while True:
            posts = self.mc.events.pollChatPosts()
            for post in posts:
                if post.message == "list_methods":
                    self.list_methods()
                else:
                    self.insult()

