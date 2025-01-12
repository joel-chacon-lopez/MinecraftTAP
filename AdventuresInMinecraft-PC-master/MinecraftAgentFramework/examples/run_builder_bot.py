import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.builder_bot import BuilderBot

if __name__ == "__main__":
    bot = BuilderBot("BuilderBot")
    bot.perform_action()

