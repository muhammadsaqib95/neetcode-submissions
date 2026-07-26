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
     * @return {void} Do not return anything, modify head in-place instead.
     */
    reorderList(head) {
        if (!head || !head.next) return;

        // Step 1: Find the middle of the linked list
        let slow = head;
        let fast = head;
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse the second half of the list
        let curr = slow.next;
        slow.next = null; // Cut off the first half from the second half
        let prev = null;
        
        while (curr) {
            let nextTmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTmp;
        }

        // Step 3: Merge the two halves (head and prev)
        let first = head;
        let second = prev; // Prev is now the head of the reversed second half
        
        while (second) {
            let tmp1 = first.next;
            let tmp2 = second.next;

            first.next = second;
            second.next = tmp1;

            first = tmp1;
            second = tmp2;
        }
    }
}
