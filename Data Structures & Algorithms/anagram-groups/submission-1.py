class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

#what this operation does is counts the ascii value of the str and keeps track of that, grouping all other strings with the same ascii value's
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
            #group all anagrams with this particualar ascii count  
        return list(res.values())