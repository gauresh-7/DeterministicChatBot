import re
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")


def respond(user_input):
    """
    Deterministic chatbot response function using regex patterns.
    """
    user_input = user_input.lower()
    
    # Regex patterns for different types of input
    insults = r'\b(stupid|dumb|idiot|fool|loser|clown|noob|lame|weirdo|jerk|moron|buffoon|airhead|blockhead|nitwit|doofus|goofball|knucklehead|bonehead|simpleton)\b'
    greetings = r'\b(hello|hi|hey|sup|yo|hiya|howdy|greetings|good morning|good afternoon|good evening|what\'s up|wassup|whatsup|long time no see|nice to meet you|pleased to meet you|how are you|how\'s it going|how have you been|how\'s everything|how\'s life|good day|welcome)\b'
    opinion = r'(?:do you think|whats your opinion on|what do you think of|do you)\\s+(.+)'
    python_term_doubt = r'(?:what is|what are|explain|define|tell me about)\\s+(a|an|the)?\\s*(\\w+\\s*\\w*)\\s*(?:in python)?'
    
    # Check for greetings
    if re.search(greetings, user_input):
        return "Hello! Welcome to the Deterministic ChatBot! How can I help you today?"
    
    # Check for insults
    if re.search(insults, user_input):
        return "THAT'S RUDE! Please be respectful. I'm here to help you."
    
    # Check for Python terminology questions
    match_doubt = re.search(python_term_doubt, user_input)
    if match_doubt:
        term = match_doubt.group(2).strip()
        
        # Python term definitions
        python_terms = {
            "list": "A **list** in Python is a collection of items that are ordered and changeable. It allows duplicate members and is created using square brackets [].",
            "tuple": "A **tuple** in Python is a collection of items that is ordered and unchangeable (immutable). It allows duplicate members and is created using parentheses ().",
            "dictionary": "A **dictionary** in Python is a collection of items that is unordered, changeable, and indexed. It stores data in **key:value** pairs.",
            "variable": "A **variable** in Python is a reserved memory location to store values. When you create a variable, you reserve some space in memory.",
            "function": "A **function** in Python is a block of organized, reusable code that is used to perform a single, related action. It helps in breaking down programs into smaller, manageable chunks.",
            "loop": "A **loop** in Python is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. Common types are `for` loops and `while` loops.",
            "string": "A **string** in Python is a sequence of characters enclosed in quotes. It is immutable and used to represent text data.",
            "integer": "An **integer** in Python is a whole number (positive, negative, or zero) without a decimal point.",
            "float": "A **float** in Python is a number that contains a decimal point, used for representing real numbers.",
            "class": "A **class** in Python is a blueprint for creating objects. It defines attributes and methods that the objects will have.",
            "module": "A **module** in Python is a file containing Python code (functions, classes, variables) that can be imported and used in other Python programs."
        }
        
        if term in python_terms:
            return python_terms[term]
        else:
            return f"Hmm, I can try to explain **{term}**, but I don't have a specific definition for that Python term right now. Try asking about common terms like list, dictionary, function, loop, etc."
    
    # Check for opinion questions
    match_opinion = re.search(opinion, user_input)
    if match_opinion:
        subject = match_opinion.group(1).strip()
        return f"Yes, I think {subject} is interesting! What do you think about it?"
    
    # Default response
    return "Hmm, I don't have an answer for that. Try asking me about Python concepts, or just say hello!"


@app.route("/")
def index():
    """Serve the main HTML page"""
    return send_from_directory(".", "ChatBot1.html")


@app.route("/answer", methods=["POST"])
def answer():
    """API endpoint to get chatbot responses"""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    
    if not question:
        return jsonify({"answer": "Please ask me something!"}), 400
    
    return jsonify({"answer": respond(question)})


@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "ChatBot is running!"})


if __name__ == "__main__":
    print("Starting Deterministic ChatBot Flask Server...")
    print("Visit http://127.0.0.1:5000 in your browser")
    app.run(debug=True, host="0.0.0.0", port=5000)

