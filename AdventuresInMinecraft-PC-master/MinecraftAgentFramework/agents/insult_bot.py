# -*- coding: utf-8 -*-
import random
from mcpi.minecraft import Minecraft

class InsultBot:
    def __init__(self):
        self.mc = Minecraft.create()

    def insult(self):
        insults = ["noob", "bot", "tonto"]
        insult = random.choice(insults)
        self.mc.postToChat(insult)

if __name__ == "__main__":
    bot = InsultBot()
    bot.insult()

