# -*- coding: utf-8 -*-
import random
from agents.base_agent import MinecraftAgent

class OracleBot(MinecraftAgent):
    def __init__(self, name):
        super().__init__(name)

    def ask(self, question):
        responses = [
            "Build a castle!",
            "Try a treehouse.",
            "How about exploring a cave?",
            "Collect some diamonds!",
            "Create an underwater base."
        ]
        return random.choice(responses)

    def perform_action(self):
        self.mc.postToChat(f"[{self.name}]: I'm ready, ask me something!")

        while True:
            posts = self.mc.events.pollChatPosts()

            for post in posts:
                player_name = post.entityId
                question = post.message

                answer = self.ask(question)

                self.mc.postToChat(f"[{self.name}]: {player_name} asked: {question}")
                self.mc.postToChat(f"[{self.name}]: My answer: {answer}")

