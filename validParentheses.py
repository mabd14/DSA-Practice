class Solution:
    def isValid(self, s: str) -> bool:
        pending = [] 
        pair = {'{': '}', '[': ']', '(': ')'} 
        open_par = '({[' 
        for letter in s: 
            if letter in open_par: 
                pending.append(letter) 
            else:
                if len(pending) == 0 or pair[pending.pop()] != letter: 
                    return False
        
        return len(pending) == 0 

"""
    pending: a stack that stores opening parantheses and validate their matching closing parantheses in the correct order
    pair: a dictionary that has the key as the open parantheses and the value as the closing parantheses
    open_par: all opening parantheses

    for letter in s: -> Iterate over each character in the input string
        if letter in open_par:  -> Check if the character is an opening parenthesis
            pending.append(letter)  -> If it is, push it onto the stack
        else:
            if len(pending) == 0 or pair[pending.pop()] != letter:  -> If the character is a closing parenthesis, check for mismatched or unbalanced parentheses
                return False  -> Return False if there is a mismatch or no opening parenthesis to match
        return len(pending) == 0  -> Return True if all parentheses are balanced (stack is empty), otherwise False
"""
