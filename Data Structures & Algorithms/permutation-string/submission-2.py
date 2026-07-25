class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        freqS1 = {}
        freqWin = {}
        # matches = 0
        l = 0

        for i in range(len(s1)):
            freqS1[s1[i]] = 1 + freqS1.get(s1[i], 0)
            freqWin[s2[i]] = 1 + freqWin.get(s2[i], 0)

        # for i in s1:
        #     if freqS1.get(i, 0) == freqWin.get(i, 0):
        #         matches +=1

        for i in range(len(s1), len(s2)):
            if freqWin == freqS1:
                return True

            freqWin[s2[i]] = freqWin.get(s2[i], 0) + 1
            # if freqS1.get(s2[i], 0):
            #     if freqWin.get(s2[i], 0) == freqS1.get(s2[i], 0):
            #         matches += 1
            #     elif freqWin[s2[i]] == freqS1.get(s2[i], 0) + 1:
            #         matches -= 1


            freqWin[s2[l]] -= 1
            if freqWin[s2[l]] == 0:
                freqWin.pop(s2[l])

            # if freqS1.get(s2[l], 0):
            #     if freqWin[s2[l]] == freqS1.get(s2[l], 0):
            #         matches += 1
            #     elif freqWin[s2[l]] ==  freqS1.get(s2[l], 0) - 1:
            #         matches -= 1
            l +=1
        return freqWin == freqS1
