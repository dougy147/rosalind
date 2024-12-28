rosalind_helper_memo_cache = {}
def memo(f):
    def m(*x):
        if not str([*x]) in rosalind_helper_memo_cache:
            rosalind_helper_memo_cache[str([*x])] = f(*x)
        return rosalind_helper_memo_cache[str([*x])]
    return m
