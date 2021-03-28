module E4 where

-- |interleave xs ys
-- return a list of corresponding elements from xs and ys, 
-- interleaved. The remaining elements of the longer list
-- are ignored.
interleave:: [a] -> [a] -> [a]
interleave x [] = [] 
interleave [] y = []
interleave (x:xs) (y: ys) = [x, y] ++ interleave xs ys

-- |toPairs xs ys
-- return a list of pairs of corresponding elements from xs and ys, 
-- interleaved. The remaining elements of the longer list
-- are ignored.
toPairs:: [a] -> [b] -> [(a, b)]
toPairs x [] = []
toPairs [] y = []
toPairs (x: xs) (y: ys) = (x, y) : toPairs xs ys

-- |repeat f x n
-- return a list [x, f(x), f(f(x)), ..., f^n(x)]
-- requires n >= 0
repeat':: (a -> a) -> a -> Int -> [a]
repeat' f x 0 = [x]
repeat' f x n = x : repeat' f (f x) (n-1)

-- |numNeg xs 
-- return a number of negative elements in xs
-- No recursion, no higher-order functions. Use list comprehension!
numNeg :: (Ord a, Num a) => [a] -> Int
numNeg x = length [i | i <- x, i<0]

-- |genSquares (low, high)
-- return a list of squares of even integers between low and high, inclusive.
-- No recursion, no higher-order functions. Use list comprehension!
genSquares :: Int -> Int -> [Int]
genSquares x y = [i*i |i <-[x..y], mod i 2 == 0 ]

-- |triples n 
-- return a list of triples (x,y,z) all less than or equal to n, such
-- that x^2 + y^2 == z^2, with no duplicate triples or premutations of
-- ealier triples.
-- No recursion, no higher-order functions. Use list comprehension!
triples :: Int -> [(Int, Int, Int)]
triples x = [(i, j ,k) | i <- [1..x], j <- [i..x], k<-[j..x], i*i + j*j == k*k]
