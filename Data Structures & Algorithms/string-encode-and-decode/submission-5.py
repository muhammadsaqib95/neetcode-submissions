class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}:{s}"
        return encoded_str

    def decode(self, s: str) -> list[str]:
        decoded_list = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            
            length = int(s[i:j])
            
            start_of_word = j + 1
            end_of_word = start_of_word + length
            
            decoded_list.append(s[start_of_word:end_of_word])
            
            i = end_of_word
            
        return decoded_list
