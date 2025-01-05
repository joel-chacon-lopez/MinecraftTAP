# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from mcpi.block import TNT

class TNTBot:
    def __init__(self):
        self.mc = Minecraft.create()

    def place_tnt(self, x, y, z):
        self.mc.setBlock(x, y, z, TNT.id, 1)  # Coloca TNT encendida
        self.mc.postToChat("jeje... Se ha colocado TNT.")

if __name__ == "__main__":
    bot = TNTBot()
    bot.place_tnt(4, 79, -103)
