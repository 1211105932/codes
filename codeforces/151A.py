"""
input:
3 4 5 10 8 100 3 1

output:
2
"""

def main():
    n = list(map(int,input().split()))
    toasts = int(n[1]*n[2]/n[6])
    limes = int(n[3]*n[4])
    salt = int(n[5]/n[7])
    print(int(min(toasts, limes, salt)/n[0]))

if __name__ == "__main__":
    main()