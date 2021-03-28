"""Exercise 2."""


def interleave(xs, ys):
    """Return a list of corresponding elements from xs and ys,
    interleaved. The remaining elements of the longer list are ignored.
    """

    return [* sum(zip(xs, ys), () )]


def to_pairs(xs, ys):
    """Return a list of pairs of corresponding elements from xs and ys,
    interleaved. The remaining elements of the longer list are ignored.
    """
    return [a for a in zip(xs, ys)]


def repeat(f, x, n):
    """Return a list [x, f(x), f(f(x)), ..., f ^ n(x)].
    Pre: n >= 0
    """
    return [x] if (n==0) else [x] + repeat(f, f(x), n-1)


def num_neg(xs):
    """Return a number of negative elements in xs.
    No recursion, no higher-order functions. Use list comprehension!
    """
    return len([x for x in xs if x < 0])


def gen_sqaures(low, high):
    """Return a list of squares of even integers between low and high, inclusive.
    No recursion, no higher-order functions. Use list comprehension!
    """
    return [x*x for x in range(low, high+1) if x%2 == 0]


def triples(n):
    """Return a list of triples (x, y, z) all less than or equal to n, such
    that x ^ 2 + y ^ 2 == z ^ 2, with no duplicate triples or premutations of
    ealier triples.
    No recursion, no higher-order functions. Use list comprehension!
    """
    return [(a,b,c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a**2 + b**2 == c**2]

    
    
