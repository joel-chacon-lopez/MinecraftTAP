import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.tnt_bot import TNTBot

if __name__ == "__main__":
    bot = TNTBot("TNTBot")
    bot.perform_action()
