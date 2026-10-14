import heapq

class Solution:
    def mergeKLists(self, lists):
        h = [(n.val, i, n) for i, n in enumerate(lists) if n]
        heapq.heapify(h)
        d = t = ListNode()
        while h:
            _, i, n = heapq.heappop(h)
            t.next = n
            t = n
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))
        return d.next