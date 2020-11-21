# auto-memoize
Python decorator for auto-memoizing pure functions

Memoization is an old computer science trick, that stores previous computation
results to prevent the need to recalculate them. Often a memoizing program
will lazily memoize results as they are used, so that next time they don't
need to be calculated.

I was reminded of the wide utility of this technique by watching this MIT
lecture recently, and reminded that memoization is a core concept in Dynamic Programming,
which is a great technique for optimisation of algorithms.

[MIT 6.006, Fall 2011, Introduction to Algorithms Lecture 19](https://www.youtube.com/watch?v=OQ5jsbhAv_M)

Python decorators are well described in the 'Professional Python' book
and I have been using them for years to wrap loggers and other things
around functions.

[Professional Python](https://www.amazon.co.uk/Professional-Python-Luke-Sneeringer/dp/1119070856)

But having watched this MIT video recently, it made me realise that it was
possible to write a Python decorator that did the work automatically.

For the Fibonacci sequence generator, this turns an exponential time
calculation into a linear time calculation. So, fib(300) will take a long
time to calculate without memoization, as many of the sub-problems
are re-computed a large number of times. Because fib(n)->m always yields
the same m for n, in all cases (i.e. it is a pure function), this is a 
simple but very effective optimisation to make.

I left the print statements in this program so that you can see a trace
on the console of what it does, but you would take those out if deploying
this in production code.

@whaleygeek

13th Nov 2020

