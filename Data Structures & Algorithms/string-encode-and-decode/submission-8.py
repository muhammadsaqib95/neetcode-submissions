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
                word = s[i+1:i+1+slice_digit]
                res.append(word)
                i += int(num_str) + 1
                num_str = ""
            else:
                num_str = num_str + s[i]
                i += 1
        return res
