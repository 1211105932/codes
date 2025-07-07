"""
input:
3
2014 2016 2015

ouput:
2015
"""

def main():
    n = input()
    years = list(map(int, input().split()))
    print(int(sum(years)/len(years)))

if __name__ == "__main__":
    main()