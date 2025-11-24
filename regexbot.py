import re
import sys
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")


def respond(user_input):
    user_input = user_input.lower()
    
    insults = r'\b(stupid|dumb|idiot|fool|loser|clown|noob|lame|weirdo|jerk|moron|buffoon|airhead|blockhead|nitwit|doofus|goofball|knucklehead|bonehead|simpleton)\b'
    greetings = r'\b(hello|hi|hey|sup|yo|hiya|howdy|greetings|good morning|good afternoon|good evening|what\'s up|wassup|whatsup|long time no see|nice to meet you|pleased to meet you|how are you|how\'s it going|how have you been|how\'s everything|how\'s life|good day|welcome)\b'
    opinion = r'(?:do you think|whats your opinion on|what do you think of|do you)\s+(.+)'
    
    if re.search(greetings, user_input):
        return "Hello!!"
    
    if re.search(insults, user_input):
        return "THATS RUDE , LEARN SOME MANNERS DUDE"
    
    match = re.search(opinion, user_input)
    if match:
        return f"Yes, I think {match.group(1)} is nice!"
    
    return "Hmm, I don't have an answer for that."


@app.route("/")
def index():
    return send_from_directory(".", "ChatBot1.html")


@app.post("/answer")
def answer():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    return jsonify({"answer": respond(question)})


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        user_input = input("What would you like to ask? ")
        print("BOT:", respond(user_input))
    else:
        app.run(debug=True)
