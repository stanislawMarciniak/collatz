def collatz(a, b, initial_a):

    print(f"Sprawdzam: {a}x + {b}")
    
    if a < initial_a: 
        print(f"\nRozwiązano dla: {a}x + {b}\n")
        return
    
    if a % 2 == 0 and b % 2 == 0: 
        collatz(a // 2, b // 2, initial_a)
    elif a % 2 == 1:
        print("Pierwszy przypadek")  
        collatz(2 * a, b, 2 * a)
        print("Drugi przypadek")  
        collatz(2 * a, a + b, 2 * a) 
    else:  
        collatz(3 * a, 3 * b + 1, initial_a)

if __name__ == "__main__":
    initial_a = 1  
    initial_b = 0
    collatz(initial_a, initial_b, initial_a)
    print('Udowodniono problem Collatza')
