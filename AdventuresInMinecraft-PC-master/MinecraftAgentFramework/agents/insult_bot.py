import random

class InsultBot(MinecraftAgent):
    def insult(self):
        insults = ["Eres un noob!", "­Construcci¢n horrible!", "¨Eso es todo lo que sabes hacer?"]
        self.send_message(random.choice(insults))

# Crear un InsultBot y hacerlo insultar
if __name__ == "__main__":
    bot = InsultBot()
    bot.insult()

