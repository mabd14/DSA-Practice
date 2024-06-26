class Solution:
    def isValid(self, s: str) -> bool:
        pending = [] # 0(1)
        pair = {'{': '}', '[': ']', '(': ')'} # 0(1)
        open_par = '({[' # 0(1)
        for letter in s: # 0(N)
            if letter in open_par: # 0(1)
                pending.append(letter) # 0(1)
            else:
                if len(pending) == 0 or pair[pending.pop()] != letter: # 0(1)
                    return False
        # 0(1)*  0(N)
        return len(pending) == 0 
