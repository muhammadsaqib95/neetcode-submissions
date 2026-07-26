class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0;
        let r = nums.length - 1

        while (l <= r) {
            if (nums[l] === target) {
                return l
            } else if (nums[r] === target) {
                return r
            }
            let m = Math.floor( (l + r ) / 2)
            if (nums[m] === target) {
                return m
            }
            if (nums[m] > nums[l]) {
                if (target > nums[m] || target < nums[l]) {
                    l = m + 1
                } else {
                    r = m - 1
                }
            } else {
                if (target < nums[m] || target > nums[r]) {
                    r = m - 1
                } else {
                    l = m + 1
                }
            }
        }

        return -1
    }
}
