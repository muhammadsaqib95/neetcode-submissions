class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for st in strs:
            s_st = "".join(sorted(st))
            if s_st in freq:
                freq[s_st].append(st)
            else:
                freq[s_st] = [st]
            
        return list(freq.values())

        