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
