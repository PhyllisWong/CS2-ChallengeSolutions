## Data Structures
## Linked Lists and Hash Tables

- choose the right tool for the right job
- What is the shape of the data, what are the constraints?
- What are the constraints
- Which operations need to be fast

#### Arrays (Python List)
- Contiguous piece of memory - sequential memory addresses in RAM
- Python arrays are pointers, and the pointers point to the data
    - Python lists are a hybrid of array and linked lists
- Same size storage space at each index
- Static - Memory allocated once, size can't change
- Dynamic - New memory allocated, array copied to grow
    - Lists in python are dynamic arrays
    - In general, when you can tell the compiler how much memory you need ahead of time, it will help with optimization
- Equation to find memory address at an index:
    - starting_address + (size * index) = address
    - A[0] + (s * i) = A[i]

#### Accessing Data Dynamic Array Runtime
- Access Element via the index: O(1) - fastest runtime
- Insert or Delete element at beginning or middle: O(n) - slowest
- Insert or delete element at the end: O(1)


##### Linked lists
-

#### Questions to solidify concepts - Dec 7, 2017
note: vocabulary to remember: primitive data type

1. If you build a histogram, how many entries will it have?
    - A histogram will have as many entries as there are types or unique words.

1. If you build a 1st order Markov Chain, what structures do you need to create, and how many?
    - I used a histogram with key value pairs, where each type is a key, and each value is a histogram. The nested histogram has the types that follow the key_word, and the values are the frequency it follows the key_word.

1. If you build a 2nd order Markov Chain, how would your structures change?
    - Instead of having a type as the key to the Markov, I could use a phrase as the key, with the values being histograms where each key is a type that follows the phrase and a value of frequency it follows.

1. Approximately how many of these structures will you have?


### Regular expressions
1. ReGex works on strings
1. Strings are sequences of characters (bytes)
1. Files are sequences of bytes, you have the possibility of a pattern

### Matching patterns
1. With a pattern specifies, new questions arise
1. Is it found, how many times, what position, what comes before and after?
1. Exact vs inexact
    - Exact: matches: describes a literal string
    - Inexact: matches: describes a pattern to match on (what regular expressions do!)

1. pattern = '\$' means I want the dollar sign char
1. '.' means wildcard {4} 4o f means anything: pattern = '\$.{4}' grab up to 4 chars after the dollar sign
1. pattern = '\$[0-9]+\.?[0-9]*
1. \d = [0-9] new pattern = \$\d+\.?\d* will grab the amounts with the dollar signs
1. pattern to keep some of the pattern use grouping ()
new pattern \$(\d+\.?\d*)
