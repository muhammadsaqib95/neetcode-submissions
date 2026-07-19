class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            res.append(str(len(st)) + "#" + st)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num_str = ""
        while i < len(s):
            if s[i] == "#" and num_str:
                slice_digit = int(num_str)
                start = i+1
                end = i+1+slice_digit
                word = s[start: end]
                res.append(word)
                i = end
                num_str = ""
            else:
                num_str = num_str + s[i]
                i += 1
        return res
