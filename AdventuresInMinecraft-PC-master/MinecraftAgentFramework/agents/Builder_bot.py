# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from mcpi.block import STONE

class BuilderBot:
    def __init__(self):
        self.mc = Minecraft.create()

    def build_tower(self, x, y, z, height):
        for i in range(height):
            self.mc.setBlock(x, y + i, z, STONE.id)
        self.mc.postToChat("Torre construida.")

if __name__ == "__main__":
    bot = BuilderBot()
    bot.build_tower(3, 80, -103, 500)
