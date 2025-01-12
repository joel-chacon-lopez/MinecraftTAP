# -*- coding: utf-8 -*-
import random
from agents.base_agent import MinecraftAgent
import time

class InsultBot(MinecraftAgent):
    def __init__(self, name):
        super().__init__(name)
        self.insults = [
            "You call that a house? Even a creeper could build better!",
            "Are you mining with a wooden pickaxe? How noob!",
            "Watch out! Oh wait, it's just your reflection.",
            "I've seen zombies with better strategies than you.",
            "Even chickens laugh at your builds!"
        ]

    def insult(self):
        insult = random.choice(self.insults)
        self.say(insult)

    def perform_action(self):
        self.say("I'm here to insult you, brace yourself!")
        try:
            while True:
                self.insult()
                time.sleep(3)
        except KeyboardInterrupt:
            self.say("Goodbye! Stopping now.")
            print("\nBot stopped by user.")
