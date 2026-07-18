class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = "";
        for (let s in strs) {
            res += strs[s].length + "#" + strs[s]
        }
        return res;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        console.log(str)
        let res = []; let i = 0;
        while (i < str.length) {
            let j = i;
            while (str[j] != "#") {
                j++;
            }
            res.push(str.slice(j+1, j+1+ Number(str.slice(i,j))))
            i = j+1+ Number(str.slice(i,j))
        }
        return res;
    }
}
