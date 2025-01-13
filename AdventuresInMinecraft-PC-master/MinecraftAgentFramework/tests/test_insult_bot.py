# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch, MagicMock
from agents.base_agent import MinecraftAgent
from agents.insult_bot import InsultBot

class TestInsultBot(unittest.TestCase):
    def setUp(self):
        # Configurar el bot con mocks
        self.bot = InsultBot("InsultBot")
        self.mock_mc = MagicMock()
        self.bot.mc = self.mock_mc

    @patch("random.choice", return_value="noob")
    def test_insult(self, mock_random):
        # Probar que el bot envía un insulto al chat
        self.bot.insult()

        self.mock_mc.postToChat.assert_called_once_with("[InsultBot]: noob")

    @patch("random.choice")
    def test_insult_variety(self, mock_random):
        # Probar que el bot elige diferentes insultos
        mock_random.side_effect = ["noob", "loser", "maggot"]

        for _ in range(3):
            self.bot.insult()

        expected_calls = [
            unittest.mock.call("[InsultBot]: noob"),
            unittest.mock.call("[InsultBot]: loser"),
            unittest.mock.call("[InsultBot]: maggot"),
        ]
        self.mock_mc.postToChat.assert_has_calls(expected_calls, any_order=False)


    @patch("time.time", side_effect=[0, 1, 2])
    @patch("agents.insult_bot.InsultBot.list_methods")
    def test_perform_action(self, mock_list_methods, mock_time):
        # Probar perform_action responde al mensaje "list_methods"
        self.mock_mc.events.pollChatPosts.return_value = [
            MagicMock(message="list_methods")
        ]

        with patch.object(self.bot, "insult") as mock_insult:
            # Ejecutar un ciclo simulado
            self.bot.perform_action()

            mock_list_methods.assert_called_once()
            mock_insult.assert_not_called()

if __name__ == "__main__":
    unittest.main()
