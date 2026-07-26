/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let dummy = new ListNode(0, head);
        let slow = dummy;
        let fast = dummy;

        // Move fast pointer ahead so there is a gap of n nodes between slow and fast
        for (let i = 0; i <= n; i++) {
            fast = fast.next;
        }

        // Move both pointers until fast reaches the end
        while (fast !== null) {
            slow = slow.next;
            fast = fast.next;
        }

        // Delete the nth node from the end
        slow.next = slow.next.next;

        // Return the actual head
        return dummy.next;
    }
}
