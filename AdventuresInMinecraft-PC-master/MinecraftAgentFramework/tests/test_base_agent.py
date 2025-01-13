# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch, MagicMock
from agents.base_agent import MinecraftAgent

class TestMinecraftAgent(unittest.TestCase):
    def setUp(self):
        # Configurar un agente simulado
        self.agent = MinecraftAgent("MinecraftAgent")
        self.mock_mc = MagicMock()
        self.agent.mc = self.mock_mc

    @patch("builtins.print")
    def test_say(self, mock_print):
        # Probar que el agente envía el mensaje al chat
        message = "Hello, Minecraft!"
        self.agent.say(message)
        self.mock_mc.postToChat.assert_called_once_with("[MinecraftAgent]: Hello, Minecraft!")

    def test_list_methods(self):
        # Probar que el agente lista los métodos correctamente
        with patch.object(self.agent, "say") as mock_say:
            self.agent.list_methods()

            # Verificar que se llamó a say con la lista de métodos
            expected_methods = [
                method for method in dir(self.agent)
                if callable(getattr(self.agent, method)) and not method.startswith("__")
            ]
            mock_say.assert_called_once_with(f"Available methods: {', '.join(expected_methods)}")

    def test_perform_action_not_implemented(self):
        # Probar que perform_action lanza NotImplementedError
        with self.assertRaises(NotImplementedError):
            self.agent.perform_action()

if __name__ == "__main__":
    unittest.main()
