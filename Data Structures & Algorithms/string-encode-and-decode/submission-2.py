class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["neet","code","love","you"]
        # "neetcodeloveyou"
        # "neet!code!love!you"
        # ["ne!et","co!de","love","you"]
        # "ne!et!co!de!love!you"
        # ["ne", "et","co", "de","love","you"]
        # "4!neet4!code"
        res = ""

        for s in strs:
            res += str(len(s)) + "!" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "!":
                j += 1
            
            length = int(s[i:j])

            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return res


            
