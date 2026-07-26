/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
        let d = 0;

        function getHeight(node) {
            if (node == null) return 0;

            let lh = getHeight(node.left)
            let rh = getHeight(node.right)

            d = Math.max(d, lh + rh)

            return 1 + Math.max(lh, rh)
        }
        getHeight(root);

        return d;
    }
}
