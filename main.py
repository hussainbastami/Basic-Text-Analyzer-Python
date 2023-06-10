import re
import sys
def text_analyzer():
    text = input("Please Enter your text: ").strip()

    words = len(text.split(' '))
    chars = len(text.replace(' ', ''))
    chars_space = len(text)
    sentences = len(re.split(r'[?!.]',text))-1
    sentences = sentences if sentences else 1
    print(f"words: {words}")
    print(f"characters: {chars}\ncharacters(including spaces): {chars_space}")
    print(f"sentences: {sentences}")
    
    text = input("enter (q) to quit. Any other key continue: ").strip()
    sys.exit() if text == "q" else text_analyzer()
    
    
text_analyzer()
