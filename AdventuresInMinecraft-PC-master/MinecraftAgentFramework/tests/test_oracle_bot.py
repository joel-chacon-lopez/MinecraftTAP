# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from agents.oracle_bot import OracleBot

class TestOracleBot(unittest.TestCase):
    def setUp(self):
        # Configurar el bot Oracle con mocks
        self.bot = OracleBot("OracleBot")
        self.mock_mc = MagicMock()
        self.bot.mc = self.mock_mc

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_generate_response_logs_interaction(self, mock_open):
        # Probar que generate_response registra interacciones en un archivo
        question = "Should I build a castle?"
        expected_response = "Build a castle!"

        # Ejecutar generate_response
        response = self.bot.generate_response(question)

        # Verificar la respuesta
        self.assertEqual(response, expected_response)

        # Verificar que se registró la interacción en el archivo
        mock_open.assert_called_once_with("oracle_log.txt", "a")
        mock_open().write.assert_called_once_with(f"Q: {question} -> A: {expected_response}\n")

    @patch.object(OracleBot, "say")
    def test_generate_response_known_question(self, mock_say):
        # Probar respuestas conocidas
        question = "Should I mine for diamonds?"
        expected_response = "Find some diamonds!"

        response = self.bot.generate_response(question)
        self.assertEqual(response, expected_response)

        # Verificar las llamadas a say
        expected_calls = [
            unittest.mock.call(f"Logging question: {question}"),
            unittest.mock.call(expected_response),
        ]
        mock_say.assert_has_calls(expected_calls)

    @patch.object(OracleBot, "say")
    def test_generate_response_unknown_question(self, mock_say):
        # Probar una pregunta desconocida
        question = "What is the meaning of life?"
        expected_response = "That's an interesting question!"

        response = self.bot.generate_response(question)
        self.assertEqual(response, expected_response)

        # Verificar las llamadas a say
        expected_calls = [
            unittest.mock.call(f"Logging question: {question}"),
            unittest.mock.call(expected_response),
        ]
        mock_say.assert_has_calls(expected_calls)


    @patch("time.sleep", return_value=None)
    @patch.object(OracleBot, "generate_response", return_value="This is a test response!")
    @patch.object(OracleBot, "say")
    def test_perform_action(self, mock_say, mock_generate_response, mock_sleep):
        # Simular publicaciones de chat
        self.mock_mc.events.pollChatPosts.return_value = [
            MagicMock(message="What should I do?")
        ]

        # Ejecutar perform_action una vez (rompiendo el bucle)
        with patch("builtins.input", side_effect=[KeyboardInterrupt]):
            try:
                self.bot.perform_action()
            except KeyboardInterrupt:
                pass

        # Verificar que generate_response y say fueron llamados
        mock_generate_response.assert_called_once_with("What should I do?")
        mock_say.assert_called_with("This is a test response!")

if __name__ == "__main__":
    unittest.main()
