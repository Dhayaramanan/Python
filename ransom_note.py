def canConstruct(ransom_note, magazine: str) -> bool:
    set_ransom_note = set(ransom_note)
    for i in set_ransom_note:
        if i not in magazine:
            return False
        if ransom_note.count(i) > magazine.count(i):
            return False

    return True


print(canConstruct('a', 'b'))

"""
Best solution:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False
        return True
"""