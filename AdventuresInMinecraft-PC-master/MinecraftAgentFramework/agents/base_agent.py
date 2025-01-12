# -*- coding: utf-8 -*-
import mcpi.minecraft as minecraft

class MinecraftAgent:
    def __init__(self, name):
        self.name = name
        self.mc = minecraft.Minecraft.create()

    def say(self, message):
        self.mc.postToChat(f"[{self.name}]: {message}")

    def perform_action(self):
        raise NotImplementedError("Este metodo debe ser implementado por subclases.")

    def list_methods(self):
        methods = [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith("__")]
        self.say(f"Available methods: {', '.join(methods)}")
