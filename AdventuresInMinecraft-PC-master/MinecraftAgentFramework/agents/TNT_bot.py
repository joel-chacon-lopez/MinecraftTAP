# -*- coding: utf-8 -*-
from agents.base_agent import MinecraftAgent
import mcpi.block as block

class TNTBot(MinecraftAgent):
   def __init__(self, name):
        super().__init__(name)
 
   def perform_action(self):
        pos = self.mc.player.getTilePos()
        self.mc.setBlock(pos.x + 1, pos.y, pos.z, block.TNT.id)
        self.say("jeje... ups... a TNT appeared...")
