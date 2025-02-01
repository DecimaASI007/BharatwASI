from chatbot import BharatwASI

bot = BharatwASI()
while True:
    prompt = input("User: ")
    response = bot.chat(prompt)
    print(f"BharatwASI: {response}")
