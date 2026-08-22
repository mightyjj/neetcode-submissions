from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word].append(word)
        """
        {
            act: [act, cat]
            aht: [hat]
        }
        """
        res = []
        for words in dic.values():
            res.append(words)

        return res