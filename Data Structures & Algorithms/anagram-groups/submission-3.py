class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for s in strs:
            sorted_word = ''.join(sorted(s))
            groups[sorted_word].append(s)

        res = []
        for word in groups:
            res.append(groups[word])

        return res