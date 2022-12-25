import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

convert = {'0': 0, '1': 1, '2': 2, '=': -2, '-': -1}
total = sum(map(lambda x: sum(5**i * convert[c] for i, c in enumerate(x[::-1])), lines))

def to_snafu(n):
    if n == 0: return ''
    first = '=' if n%5==3 else '-' if n%5==4 else str(n%5)
    add = 2 if n%5==3 else 1 if n%5==4 else 0
    return first + to_snafu((n+add)//5)

print("Part one (and two):", to_snafu(total)[::-1])