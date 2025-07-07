class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            i = word.index(ch) + 1
            word = word[:i][::-1] + word[i:]
        
        return word