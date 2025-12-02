import re
import sys
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")


def respond(user_input):
    user_input = user_input.lower()
    
    insults = r'\b(stupid|dumb|idiot|fool|loser|clown|noob|lame|weirdo|jerk|moron|buffoon|airhead|blockhead|nitwit|doofus|goofball|knucklehead|bonehead|simpleton)\b'
    greetings = r'\b(hello|hi|hey|sup|yo|hiya|howdy|greetings|good morning|good afternoon|good evening|what\'s up|wassup|whatsup|long time no see|nice to meet you|pleased to meet you|how are you|how\'s it going|how have you been|how\'s everything|how\'s life|good day|welcome)\b'
    opinion = r'(?:do you think|whats your opinion on|what do you think of|do you)\s+(.+)'
    
    
    python_dsa_doubt = r'(?:what is|what are|explain|define|tell me about|how does)\s+(a|an|the)?\s*(\w+\s*\w*\s*\w*)\s*(?:in python|work)?'
    
    if re.search(greetings, user_input):
        return "Hello!!"
    
    if re.search(insults, user_input):
        return "THATS RUDE , LEARN SOME MANNERS DUDE"
    
    
    match_doubt = re.search(python_dsa_doubt, user_input)
    if match_doubt:
        term = match_doubt.group(2).strip()
        
     
        if term == "list":
            return "A **list** in Python is a collection of items that are ordered and changeable. It allows duplicate members and is created using square brackets []."
        elif term == "tuple":
            return "A **tuple** in Python is a collection of items that is ordered and unchangeable (immutable). It allows duplicate members and is created using parentheses ()."
        elif term == "dictionary":
            return "A **dictionary** in Python is a collection of items that is unordered, changeable, and indexed. It stores data in **key:value** pairs."
        elif term == "variable":
            return "A **variable** in Python is a reserved memory location to store values. When you create a variable, you reserve some space in memory."
        
        
        elif term == "stack":
            return "A **Stack** is a linear data structure that follows the **Last-In, First-Out (LIFO)** principle. Think of it like a stack of plates—the last one placed on top is the first one taken off. "
        elif term == "queue":
            return "A **Queue** is a linear data structure that follows the **First-In, First-Out (FIFO)** principle. Like waiting in a line—the person who arrives first is the first one served. "
        elif term == "linked list":
            return "A **Linked List** is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (node) stores the data and a reference (or link) to the next element. "
        elif term == "binary tree":
            return "A **Binary Tree** is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child. It's often used for efficient searching and sorting."

        elif term == "hash map" or term == "hash table":
            return "A **Hash Map** (or Hash Table) is a data structure that stores data in key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be retrieved. "
        elif term == "binary search":
            return "**Binary Search** is an efficient algorithm for finding an item from a **sorted** list of items. It repeatedly divides the search interval in half to eliminate half of the elements at each step."
        elif term == "time complexity":
            return "**Time Complexity** is a measure of the time required to run an algorithm as the input size grows. It is usually expressed using **Big O notation** (e.g., $O(n)$, $O(\log n)$)."
        
        else:
            return f"That's a great question! I can try to explain **{term}**, but I don't have a specific definition for that Python or DSA term yet."
    
    match_opinion = re.search(opinion, user_input)
    if match_opinion:
        return f"Yes, I think {match_opinion.group(1)} is nice!"
    
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
