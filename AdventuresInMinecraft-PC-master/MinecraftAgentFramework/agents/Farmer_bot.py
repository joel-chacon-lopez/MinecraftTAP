# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from mcpi.block import FARMLAND, CROPS

class FarmerBot:
    def __init__(self):
        self.mc = Minecraft.create()

    def plant_crops(self, x, y, z, length):
        for i in range(length):
            self.mc.setBlock(x + i, y, z, FARMLAND.id)
            self.mc.setBlock(x + i, y + 1, z, CROPS.id)
        self.mc.postToChat("Cultivos plantados...")

if __name__ == "__main__":
    bot = FarmerBot()
    bot.plant_crops(4, 79, -103, 1000)
