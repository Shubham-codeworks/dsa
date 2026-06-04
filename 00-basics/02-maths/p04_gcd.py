class GCD:
    def gcd_bruteforce(self, m: int, n: int) -> int:
        m, n = abs(m), abs(n)
        k = min(m, n)
        
        if k == 0:
            return max(m, n)
        
        for i in range(1, k+1):
            if m%i == 0 and n%i == 0:
                ans = i
        return ans
    
    def gcd_bruteforce2(self, m:int, n:int) -> int:
        m, n = abs(m), abs(n)
        k = min(m, n)
        
        if k == 0:
            return max(m, n)
        
        for i in range(k, 0, -1):
            if m%i == 0 and n%i == 0:
                return i
    
    def gcd_euclidean(self, m:int, n:int) -> int:
        m, n = abs(m), abs(n)
        while n != 0:
            m, n = n, m%n
        return m
    
if __name__ == "__main__":
    m, n = map(int, input("Enter two numbers: ").split())
    obj = GCD()
    
    res1 = obj.gcd_bruteforce(m, n)
    print(f"GCD of {m} and {n} using brute force approach is {res1}")

    res2 = obj.gcd_bruteforce2(m, n)
    print(f"GCD of {m} and {n} using second brute force approach is {res2}")

    res3 = obj.gcd_euclidean(m, n)
    print(f"GCD of {m} and {n} using Euclidean method is {res3}")