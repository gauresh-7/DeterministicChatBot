responses={"What is your name?":"My names ProtoBot1",
           "Hows the weather today?":"I dont know I cant really see it",
           "What do you do?" :"Not much , I'm not very functional",
           "Bye":"Goodbye! Have a great day!",
           "You good?":"Always! Thanks for checking in."
           }
def respond(messages):
    if messages in responses:
        return responses[messages]
question=input("whats your question?")
print(respond(question))