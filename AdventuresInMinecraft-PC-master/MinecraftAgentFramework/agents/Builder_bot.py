# -*- coding: utf-8 -*-
from agents.base_agent import MinecraftAgent
import mcpi.block as block

class BuilderBot(MinecraftAgent):
    def __init__(self, name):
        super().__init__(name)

    def build_house(self, x, y, z):
        width = 5
        height = 4
        depth = 5

        for dx in range(width):
            for dy in range(height):
                for dz in range(depth):
                    if dx == 0 or dx == width - 1 or dz == 0 or dz == depth - 1:
                        if not (dx == width // 2 and dz == 0 and dy < 2):  
                            self.mc.setBlock(x + dx, y + dy, z + dz, block.WOOD.id)

        for dx in range(width):
            for dz in range(depth):
                self.mc.setBlock(x + dx, y + height, z + dz, block.WOOD.id)

        for dx in range(width):
            for dz in range(depth):
                self.mc.setBlock(x + dx, y - 1, z + dz, block.STONE.id)

        self.mc.postToChat(f"[{self.name}]: House built at ({x}, {y}, {z})")

    def perform_action(self):
        pos = self.mc.player.getTilePos()
        self.mc.postToChat(f"[{self.name}]: Building a house near you!")
        self.build_house(pos.x + 2, pos.y, pos.z + 2)

