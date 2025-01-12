# -*- coding: utf-8 -*-
from agents.base_agent import MinecraftAgent
import mcpi.block as block

class BuilderBot(MinecraftAgent):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def generate_house_structure(x, y, z, width, height, depth):
        return [
            (x + dx, y + dy, z + dz, block.WOOD.id if dy < height - 1 else block.STONE.id)
            for dx in range(width)
            for dy in range(height)
            for dz in range(depth)
            if dx == 0 or dx == width - 1 or dz == 0 or dz == depth - 1 or dy == height - 1
        ]

    def build_house(self, x, y, z):
        structure = self.generate_house_structure(x, y, z, 5, 4, 5)
        for bx, by, bz, material in structure:
            self.mc.setBlock(bx, by, bz, material)
        self.say("House built!")

    def perform_action(self):
        pos = self.mc.player.getTilePos()
        self.mc.postToChat(f"[{self.name}]: Building a house near you!")
        self.build_house(pos.x + 2, pos.y, pos.z + 2)

