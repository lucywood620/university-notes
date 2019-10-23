module Lib
    ( someFunc
    ) where

someFunc :: IO ()

--n = a `div` length xs
--  where
--    a=10
--    xs=[1,2,3,4,5]


-- Last
lastnum n = head(reverse(n))

-- Other definition for Last
altlastnum n = n !! (length(n)-1)

--definition for init
init n = reverse(tail(reverse n))

-- other definition for init
altinit n = take (length (n)-1) n

-- shuffle
shuffle n = if length n == 0 then [] else (drop 1 n) ++ drop (length(n)-1) (reverse n)

-- Sorting function
f [] = []
f(x:xs) = f ys ++ [x] ++ f zs
  where
    ys = [a | a <- xs, a < x]
    zs = [b | b <- xs, b>x]
    
-- it would remove duplicates   



someFunc = print (f [4,2,5,1,1]) 
