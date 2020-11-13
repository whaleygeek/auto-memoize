# memo.py  12/11/2020  D.J.Whale
# auto-memoisation wrapper experiment

def memo(fn):
    fn.memo = {}
    def mf(n):
        try:
            f = fn.memo[n]
            print("    using memoized fib(%d)->%d" % (n, f))
            return f
        except KeyError:
            f = fn(n)
            print("    memoizing fib(%d)->%d" % (n, f))
            fn.memo[n] = f
            return f
    return mf

@memo
def fib(n):
    print("  fib(%d)" % n)
    if n <= 2: return 1
    else: return fib(n-1) + fib(n-2)

def calc(n):
    print("CALC fib(%d)" % n)
    print("RES=%d" % fib(n))

if __name__ == "__main__":
    for i in range(1,10):
        print(i, fib(i))
    #calc(5)
    #calc(20)
    #calc(499)
