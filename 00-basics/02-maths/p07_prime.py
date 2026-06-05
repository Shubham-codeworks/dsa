from p06_divisors import Divisors

class isPrime:
    def is_prime(self, n: int) -> bool:
        div_lst = Divisors().divisors(n)
        
        if n == 1:
            return False
        
        return len(div_lst) == 2
    
if __name__ == "__main__":
    obj = isPrime()
    num = int(input("Enter a number: "))
    res = obj.is_prime(num)
    print(f"Is {num} a prime number? {res}")
