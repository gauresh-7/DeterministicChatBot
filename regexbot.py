
import re

def Respond(user_input):
    user_input = user_input.lower()
    
    insults = r'\b(stupid|dumb|idiot|fool|loser|clown|noob|lame|weirdo|jerk|moron|buffoon|airhead|blockhead|nitwit|doofus|goofball|knucklehead|bonehead|simpleton)\b'
    
    greetings = re.search(
        r'\b(hello|hi|hey|sup|yo|hiya|howdy|greetings|good morning|good afternoon|good evening|what’s up|wassup|whatsup|long time no see|nice to meet you|pleased to meet you|how are you|how’s it going|how have you been|how’s everything|how’s life|good day|welcome)\b',
        user_input
    )
    
    if greetings:
        return "Hello!!"
    
    if re.search(insults, user_input):
        return "THATS RUDE , LEARN SOME MANNERS DUDE"
    
    # Capture phrases after "do you think" or similar
    good = re.search(r'(?:do you think|whats your opinion on|what do you think of|do you)\s+(.+)', user_input)
    if good:
        thing = good.group(1)
        return f"Yes, I think {thing} is nice!"
    
    return "Hmm, I don't have an answer for that."

# Main loop
user_input = input("What would you like to ask? ")
print("BOT:", Respond(user_input))