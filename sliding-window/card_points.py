class Solution:
    def max_score(self, card_score, k):
        """
        https://takeuforward.org/blogs/data-structure-and-algorithm/maximum-points-you-can-obtain-from-cards
        """
        n = len(card_score)
        if k < 0 or k > n:
            return -1
        
        if k == 0:
            return 0
        
        if k == n:
            return sum(card_score)

        max_pts = sum(card_score[:k])
        curr_score = max_pts
        right = n - 1
        
        for left in range(k-1, -1, -1):
            curr_score = curr_score - card_score[left] + card_score[right]
            right -= 1
            if curr_score > max_pts:
                max_pts = curr_score
        
        return max_pts

if __name__ == "__main__":
    obj = Solution()
    cards = list(map(int, input("Enter card scores: ").split()))
    k = int(input("Number of cards: "))
    out = obj.max_score(cards, k)
    print(f"Maximum score with {k} cards is {out}")