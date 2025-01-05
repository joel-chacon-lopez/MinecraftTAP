# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from mcpi.block import AIR

class MinerBot:
    def __init__(self):
        self.mc = Minecraft.create()

    def mine_line(self, x, y, z, length):
        for i in range(length):
            self.mc.setBlock(x + i, y, z, AIR.id)
        self.mc.postToChat("Mineria completada...")

if __name__ == "__main__":
    bot = MinerBot()
    bot.mine_line(4, 80, -103, 10000)
