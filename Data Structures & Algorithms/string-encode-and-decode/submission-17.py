class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

        # strs = ["hello", "world"]
        # final = 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        ptr = 0
        decoded_strs = []

        while ptr < len(s):
            length_end = ptr

            while s[length_end] != '#':
                length_end += 1

            length = int(s[ptr:length_end])
            str_start = length_end + 1
            str_end = str_start + length

            decoded_strs.append(s[str_start:str_end])
            ptr = str_end
        return decoded_strs