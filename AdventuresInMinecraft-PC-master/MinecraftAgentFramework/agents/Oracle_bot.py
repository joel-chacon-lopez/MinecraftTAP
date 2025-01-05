# -*- coding: utf-8 -*-
import random
from mcpi.minecraft import Minecraft

class OracleBot:
    def __init__(self):
        self.mc = Minecraft.create()

    def answer_question(self):
        answers = ["Si", "No", "Tal vez", "Preguntamelo despues", "Definitivamente si", "Definitivamente no"]
        answer = random.choice(answers)
        self.mc.postToChat(f"El oraculo dice: {answer}")

if __name__ == "__main__":
    bot = OracleBot()
    bot.answer_question()
