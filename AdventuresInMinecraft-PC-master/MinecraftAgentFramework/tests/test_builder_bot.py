# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch, MagicMock
from agents.tnt_bot import TNTBot

class TestTNTBot(unittest.TestCase):
    def setUp(self):
        # Configurar el bot TNT con mocks
        self.bot = TNTBot("TNTBot")
        self.mock_mc = MagicMock()
        self.bot.mc = self.mock_mc

    @patch("time.sleep", return_value=None)
    def test_perform_action(self, mock_sleep):
        # Configurar la posición simulada del jugador
        mock_pos = MagicMock()
        mock_pos.x = 10
        mock_pos.y = 64
        mock_pos.z = 20
        self.mock_mc.player.getTilePos.return_value = mock_pos

        # Ejecutar la acción una sola vez
        with patch.object(self.bot, "say") as mock_say:
            with patch.object(self.bot.mc, "setBlock") as mock_setBlock:
                # Romper el bucle infinito para la prueba
                with patch("builtins.input", side_effect=[KeyboardInterrupt]):
                    try:
                        self.bot.perform_action()
                    except KeyboardInterrupt:
                        pass

                # Verificar que se colocó un bloque TNT en la posición esperada
                mock_setBlock.assert_called_once_with(11, 64, 20, self.mock_mc.TNT.id)

                # Verificar que se envió el mensaje correcto
                mock_say.assert_called_once_with("jeje... ups... a TNT appeared...")

if __name__ == "__main__":
    unittest.main()













































                                    [ New File ]
^G Help       ^O Write Out  ^W Where Is   ^K Cut        ^T Execute    ^C Location
^X Exit       ^R Read File  ^\ Replace    ^U Paste      ^J Justify    ^/ Go To Line
