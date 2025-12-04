import re
import sys
import nltk
import wikipedia
import warnings
from nltk.corpus import stopwords
from wikipedia.exceptions import DisambiguationError, PageError


try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    print("Downloading NLTK stopwords...")
    nltk.download('stopwords')
    print("Download complete.")
except LookupError:
     print("NLTK not found. Please ensure it is installed: pip install nltk")



try:
    from bs4 import GuessedAtParserWarning
    warnings.filterwarnings('ignore', category=GuessedAtParserWarning)
except ImportError:
    pass



def extract_keywords(question):
    
    words = re.findall(r'\b\w+\b', question.lower())
    stop_words = set(stopwords.words('english'))
    
    keywords = [w for w in words if w not in stop_words and len(w) > 1]
    return keywords

def askWiki(keywords):
    
    if not keywords:
        return "ERROR: I couldn't identify the core topic to search for after filtering your question."

    primary_kw = " ".join(keywords)
    print(f" Searching Wikipedia for: '{primary_kw}'...")
    
    try:
        
        summary = wikipedia.summary(primary_kw, sentences=3, auto_suggest=True)
        return summary
    
    except DisambiguationError as e:
        
        first_option = e.options[0]
        try:
             summary = wikipedia.summary(first_option, sentences=2, auto_suggest=False)
             return f"Disambiguation Alert: I found several topics, but here is information on **{first_option}**: {summary}"
        except Exception:
             return f" Error: I found several options for '{primary_kw}' but couldn't summarize any. Try being more specific. Possible topics: {', '.join(e.options[:5])}."
            
    except PageError:
        return f"Error: I couldn't find a Wikipedia page for '{primary_kw}'."
        
    except Exception as e:
        return f" Error: An unexpected issue occurred during the lookup: {e}"



if __name__ == "__main__":
    
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("\nUsage: python your_script_name.py")
        print("This program prompts you for a question and uses Wikipedia to find the answer.")
        sys.exit(0)

    print("\n--- Wikipedia Question Answering Tool ---")
    
    try:
        user_question = input(" What factual question would you like to ask? ")
    except EOFError:
        print("\nExiting program.")
        sys.exit(0)
    
    if not user_question.strip():
        print("Please enter a question.")
        sys.exit(0)

    
    keywords = extract_keywords(user_question)
    
    if not keywords:
        print("\n--- Result ---")
        print(askWiki(keywords))
    else:
       
        wiki_answer = askWiki(keywords)
        
       
        print("\n--- Analysis ---")
        print(f"Keywords extracted: {keywords}")
        
        print("\n--- Wikipedia Answer ---")
        print(wiki_answer)