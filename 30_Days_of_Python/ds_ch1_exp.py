"""
Data Structures and Algorithms in Python

Chapter 1: Overview

Experiments
"""

def list_char_without_space(string: str):
    """
    1-A
    Write a Python list comprehension that returns the individual characters of a string that are not whitespace characters. Apply it to the string "4 and 20 blackbirds.\n”
    """
    return [x for x in string if x != ' ']
    

if __name__ == "__main__":
    # 1-A
    list_char = list_char_without_space(string="4 and 20 blackbirds.\n")
    print(list_char)
    
