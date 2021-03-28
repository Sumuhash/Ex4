"""Exercise 2."""


def interleave(xs_1, ys_1):
    """Return a list of corresponding elements from xs and ys,
    interleaved. The remaining elements of the longer list are ignored.
    """
    return [* sum(zip(xs_1, ys_1), ())]


def to_pairs(xs_1, ys_1):
    """Return a list of pairs of corresponding elements from xs and ys,
    interleaved. The remaining elements of the longer list are ignored.
    """
    return list(zip(xs_1, ys_1))


def repeat(func, x_1, n_1):
    """Return a list [x, f(x), f(f(x)), ..., f ^ n(x)].
    Pre: n >= 0
    """
    return [x_1] if (n_1 == 0) else [x_1] + repeat(func, func(x_1), n_1-1)


def num_neg(xs_1):
    """Return a number of negative elements in xs.
    No recursion, no higher-order functions. Use list comprehension!
    """
    return len([x for x in xs_1 if x < 0])


def gen_squares(low, high):
    """Return a list of squares of even integers between low and high, inclusive.
    No recursion, no higher-order functions. Use list comprehension!
    """
    return [x * x for x in range(low, high+1) if x % 2 == 0]


def triples(n_1):
    """Return a list of triples (x, y, z) all less than or equal to n, such
    that x ^ 2 + y ^ 2 == z ^ 2, with no duplicate triples or premutations of
    ealier triples.
    No recursion, no higher-order functions. Use list comprehension!
    """
    return [(a, b, c) for a in range(1, n_1+1) for b in range(
        a, n_1+1)for c in range(b, n_1+1) if a ** 2 + b ** 2 == c ** 2]
