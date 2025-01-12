import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.insult_bot import InsultBot

if __name__ == "__main__":
    bot = InsultBot("InsultBot")
    bot.perform_action()
