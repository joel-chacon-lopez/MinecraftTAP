import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.oracle_bot import OracleBot

if __name__ == "__main__":
    bot = OracleBot("OracleBot")
    bot.perform_action()

