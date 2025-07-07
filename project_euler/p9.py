def pythagorean(a, b, c):
   return a * a + b * b == c * c

def main():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if pythagorean(a, b, c):
                    if a + b + c == 1000:
                        return a * b * c
    
    return 

if __name__ == "__main__":
    output = main()
    print(output)