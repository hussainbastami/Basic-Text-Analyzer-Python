import re
import sys

# creating the Main function
def text_analyzer():
    # Getting an input from user
    text = input("Please Enter your text: ").strip()
    # splitting words with each space, Creating a list of them and getting the len of the list (Number of words)
    words = len(text.split(' '))
    # Getting the number of characters (without space, so we delete everyspace)
    chars = len(text.replace(' ', ''))
    # Getting the number of characters (including spaces)
    chars_space = len(text)
    
    
    """
    Getting the number of sentences.
    We create a list of sentences in which eash sentence has been seprated with the others by a "? . !" .
    Then we make sure there is no junk sentence. (ex. When we have a sentence like this: "Hello Everyone!!!", The app will count each "!" as a sentence and we don't want this) 
    """
    sentences = len([i for i in re.split(r'[?!.]',text) if i.strip() != ''])
    
    # We will check if the sentences number is 0 or not (ex. When we have a sentence like this: "Hello Everyone", there is no period, question mark or... ; but we turn it to 1 sentence by default) 
    sentences = sentences if sentences else 1
    
    # Printing results
    print(f"words: {words}")
    print(f"characters: {chars}\ncharacters(including spaces): {chars_space}")
    print(f"sentences: {sentences}")
    
    # Get quit command. If not, restart the function and start getting a new input from the user.
    text = input("enter (q) to quit. Any other key continue: ").strip()
    sys.exit() if text == "q" else text_analyzer()
    
# Calling the main function
text_analyzer()
