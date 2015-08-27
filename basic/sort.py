#Just for self-study

#Sorting Problems:
# Input:  a sequence of n numbers <a1, a2, ..., an>
# Output: a permutation (reordering) <A1, A2, ..., An> of 
#         input seqence such that A1 <= A2 <= ... <= An

#1 Insertion sort (Vanila)
#1.1 Psudo-Code ( From Introduction to Algorithms )
# INSERTION-SORT(A)
#   for j = 2 to A.length
#       key = A[j]
#       // Insert A[j] into the sorted sequence A[1 .. j-1].
#       i = j - 1
#       while i > 0 and A[i] > key
#           A[i + 1] = A[i]
#           i = i - 1
#       A[i + 1] = key
#
#1.2 Analysis
# * Description: 
# Starting from the second item of the array to which we have a pointer, which is called Key.
# The Key keeps moving to the end as we go through different steps of the algorithm. In each 
# step, we compare the key with each of the items in front of it to find the correct position 
# into which we then inert the key.
# 
# * Loop invariants:
#   At the start of each iteration of the for loop, the subarray A[1, j-1] consists of the 
#   elements originally in A[1, j-1], but in sorted order.
#
# * Complexity:
# There are O(n) steps in terms of key position. In each step, there are O(n) works, which 
# consists of one compare and one swap. Thus, we can also say there are O(n) compares and swaps.
# Counting numbers of compares and numbers of swaps separately is important, because the cost of 
# comparison and the cost of swap may differ substantially in some cases, though usually the two 
# opersions are quite likely equal in cost. 
# 
# In summary, the complexity of the above vanila insertion sort is O(n^2), in terms of both comparison
# and swap. 
# 
#
def insertion_sort(A) :
    """
    This is an implementaion of vanila insertion sort algorithm
    :param A: An array of numbers to be sorted 
    :return: An sorted array
    """
    assert A.__len__() > 1
    for j in range(1, A.__len__()):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = key
    return A 
    
#2 Insertion sort (Binary search)
#2.1 Motivation
#  In cases where comparison is much more expensive than swap, we may want to reduce the number of 
#  comparison operation. As can be seen from the analysis of vanila insertion sort, comparison operation
#  happens when finding the correct position in the subarray before the key for the key to 
#  insert into. Since the subarray has already been sorted, thus we can use binary-search for finding the 
#  correction position, where only O(log(n)) compares are required in each step. However it does not reduce
#  the number of swaps, which is still O(n) in each step. 
#  
#  Overall, the complexity remains O(n^2). 
#

#def insertion_sort_b(A):
#   To Do
# 





#3 Merge sort
#3.1 Divide and Conquer approach
#*How it works..
# It breaks the problem into several subproblems that are similar to the original problem but smaller in
# size, solve the subproblems recursively, and then combine these solutions to create a solution to the 
# original problem.
#
#*Paradigm, it involves three steps at each level of the recursion:
# a. Divide the problem into a number of subproblems that are smaller instances of the same problem. 
# b. Conquer the problem by solving them recursively. If the subproblem sizes are small enough, however
#    just solve the subproblems in a straightforward mannner.
# c. Combine the solutions to the subproblems into the solution for the original problem.
#
#3.2 Psudo-Code ( From Introduction to Algorithms )
#// Auxiliary procedure to complete the "Combine" step in merge-sort
#// which merge two sorted subarrays A[p, q] and A[q+1, r] into one sorted array A[p, r]
# MERGE(A, p, q r) 
#   n1 = q - p + 1
#   n2 = r - q
#   let L[1, n1 + 1] and R[1, n2 + 1] be the new arrays
#   for i = 1 to n1
#       L[i] = A[p + i - 1] 
#   for i = 1 to n2 
#       R[i] = A[q + i] 
#   L[n1 + 1] = +infinte
#   R[n2 + 1] = +infinte 
#   i = 1
#   j = 1
#   for k = p to r
#       if L[i] <= R[j]
#           A[k] = L[i]
#           i = i + 1
#       else 
#           A[k] = R[j]
#           j = j + 1
#
# MERGE-SORT(A, p r)
#   if (p < r) 
#       q = (p + r) / 2
#       MERGE-SORT(A, p , q)
#       MERGE_SORT(A, q + 1, r)
#       MERGE(A, p, q, r)
# 
#3.2 The way how merge-sort works..
# Merge-sort follows closely the Divide-Conquer paradigm, it operates in the way that firstly we split the 
# size n array into two subarray of size n/2, which corresponds to the Divide step; then we solve the two 
# size n/2 subarrays recursively using merge-sort in the Conquer step; lastly we merge the sorted subarrays
# to produce the sorted answer. 
#
# The divide step is quite straightforward. The conquer step is where the recursion happens, and nothing but
# keeping calling itself is done in the step. While the Combine step is the key step, as it is in this step 
# where most of the work is done. 
#
# The complexity of the "combine step" is O(n)
# 

# * Complexity:
# T(n) = 2T(n/2) + O(n) --> O(nlog(n))
# 
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[p + i ]) 
    for i in range(0, n2):
        R.append(A[q + 1 + i])
    L.append(float("inf"))
    R.append(float("inf"))
    i = 0 
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge_sort_(A, p, r):
    if ( p < r):
        q = (p + r) / 2
        merge_sort_(A, p, q)
        merge_sort_(A, q + 1, r)
        merge(A, p, q, r)

def merge_sort(A):
    merge_sort_(A, 0, (A.__len__() - 1))



#4 Heap Sort
#4.1 The Heap Data Structure 
# An array object that can be viewed as nearly complete binary tree. Each node of the tree corresponds to 
# an element of the array. The tree is completely filled on all levels except the lowest level, which is 
# filled from the left up to a point. Suppose an array A represents a heap. A has the following properties:
#  * A.length gives the number of elements in the array
#  * A.size represents how many elements in the heap are stored in array A. 
#  *  0<= A.size <= A.length. 
#  * The root of the tree is A[1].
#  * The parent of node i(the indice of a node) is:
#       PARENT(i)
#           return  i/2 
#
#  * The left child of node i is 
#       LEFT(i)
#           return  2*i 
#
#  * The right child of node i is 
#       RIGHT(i)
#           return  2*i + 1
#
# * For max-heap: the value of a node is not greater than its parents, where A[PARENT(i)] >= A[i], thus the 
#   largest element in a max-heap is at the root A[1]
# * For min-heap: the value of a node is not smaller than its parents, where A[PARENT(i)] <= A[i], thus the 
#   smallest element in a min-heap is at the root A[1]
# * Since max-heap and min-heap are very similar, so without further specifying we use max-heap to stand for 
#   the term 'heap'
# 
# * the height of a node is defined as the number of edges on the longest simple downward path from the node 
#   to a leaf.
# * the height of a heap is defined as the height of its root, which is O(lgn)
# 
# 4.2 Maintaining the heap property  -- MAX-HEAPIFY
# In order to maintain the max-heap property, we call the precodure MAX-HEAPIFY
#  
# It takes an array A and an index i into the array as inputs. It also assumes that there are at most 1 violation
# of the max-heap propety, which is that the binary trees rooted at LEFT(i) and RIGHT(i) are max-heaps, but 
# that A[i] can be smaller that its children, thus violating the max-heap propety. This assumption is very vital 
# to MAX-HEAPIFY as it simplifies the implementaion of MAX-HEAPIFY significantly but at the same time also makes 
# it possible to build a max-heap from an arbitary array by calling itself recursively 
# Psudo Code:
#   MAX-HEAPIFY(A, i):
#       l = LEFT(i)
#       r = RIGHT(i)
#       if l <= A.size and  A[l] > A[i]
#           largest = l
#       else 
#           largest = i
#       if r <= A.size and A[r] > A[largest]
#           largest = r
#       if largest != i 
#           tmp = A[i]
#           A[i] = A[largest]
#           A[largest] = tmp
#           MAX-HEAPIFY(A, largest]
#
# The time-complexity of MAX-HEAPIFY on a node of height h is O(h) 


def heap_left(i):
#   Note that this can be further optimized by LEFT shifting the binary representation of i by one bit position 
    return (2 * i)

def heap_right(i):
#   Note that this can be further optimized by LEFT shifting the binary representation of i by one bit position
#   and then setting the LSB
    return (2 * i + 1)

def heap_parent(i):
#   Note that this can be further optimized by RIGHT shifting the binary representation of i by one bit position 
    return (i / 2)

def heap_max_heapify(A, i, size):
    """
    A : The array represents a heap 
    i : the index of the node from which to start max-heapify, starts from 0;
    size: the number of elements in the heap, usually it equals to the length of array A
    """
    assert size <= A.__len__()
    #Converting to one-based indexing when caculating the indices of the node's children 
    l = heap_left(i + 1) - 1
    r = heap_right(i + 1) - 1
    
    if l < size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < size and A[r] > A[largest]:
        largest = r

    if largest != i:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        # After swapping A[i] with A[largest], which causes node i and its children to satisfy the max-heap 
        # preporty. Howerver the node indexed by largest now has the original value of A[i], and thus the 
        # subtree rooted at largest might violate the max-heap property. So we call itself recursively on 
        # that subtree
        heap_max_heapify(A, largest, size)

def heap_min_heapify(A, i, size):
    """
    A : The array represents a heap 
    i : the index of the node from which to start min-heapify, starts from 0;
    size: the number of elements in the heap, usually it equals to the length of array A
    """
    assert size <= A.__len__()
    #Converting to one-based indexing when caculating the indices of the node's children 
    l = heap_left(i + 1) - 1
    r = heap_right(i + 1) - 1
    
    if l < size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i

    if r < size and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        tmp = A[i]
        A[i] = A[smallest]
        A[smallest] = tmp
        # After swapping A[i] with A[smallest], which causes node i and its children to satisfy the min-heap 
        # preporty. Howerver the node indexed by smallest now has the original value of A[i], and thus the 
        # subtree rooted at smallest might violate the min-heap property. So we call itself recursively on 
        # that subtree
        heap_min_heapify(A, smallest, size)


# Iterative control construct( a loop) version
def heap_max_heapify_it(A, i, size):
    """
    This is an efficient MAX-HEAPIFY procedure that uses an iterative control construct instead of recursion
    A : The array represents a heap 
    i : the index of the node from which to start max-heapify, starts from 0;
    size: the number of elements in the heap, usually it equals to the length of array A
    """
    assert size <= A.__len__()
    while i <= size/2 - 1:
        l = heap_left(i + 1) - 1
        r = heap_right(i + 1) - 1
        if A[l] > A[i]:
            largest = l
        else:
            largest = i

        if r < size and A[r] > A[largest]:
            largest = r
        
        if largest == i:
            break
        else:
            tmp = A[i]
            A[i] = A[largest]
            A[largest] = tmp
            i = largest

# Iterative control construct( a loop) version
def heap_min_heapify_it(A, i, size):
    """
    This is an efficient MIN-HEAPIFY procedure that uses an iterative control construct instead of recursion
    A : The array represents a heap 
    i : the index of the node from which to start min-heapify, starts from 0;
    size: the number of elements in the heap, usually it equals to the length of array A
    """
    assert size <= A.__len__()
    while i <= size/2 - 1:
        l = heap_left(i + 1) - 1
        r = heap_right(i + 1) - 1
        if A[l] < A[i]:
            smallest = l
        else:
            smallest = i

        if r < size and A[r] < A[smallest]:
            smallest = r
        
        if smallest == i:
            break
        else:
            tmp = A[i]
            A[i] = A[smallest]
            A[smallest] = tmp
            i = smallest

#4.3 Building a heap
# * The elements in subarray A[(n/2 + 1) .. n] are all leaves of the tree and so each is a 1-element heap to begin 
#   with. So we can build a heap by runing MAX-HEAPIFY on each of the remaining nodes in reverse order.
#
#   Pseudo Code
#   BUILD-MAX-HEAP(A)
#       A.heap-size = A.length
#       for i = A.heap-szie/2  downto 1
#           MAX-HEAPIFY(A, i)
#
# * Correctness Analysis 
#   loop invariant: 
#      at the start of each iteration of the for loop, each nodes i+1, i+2, ..., n is the root of a max-heap.
#   
#   Initialization: Prior to the first iteration of loop, i = n/2. Each node n/2 + 1, n/2 + 2, ..., n is a leaf
#       and is thus a root of a trivial max-heap
#
#   Maintenace: To see each iteration maintains the loop invariant, observe that the children of node i are 
#       indexed higher than i. By the loop invariant, they are both roots of max-heaps. This is exactly the c
#       condition required for the call MAX-HEAPIFY(A, i) to make node i a max-heap root. Moreover, the MAX-
#       HEAPIFY call preserves the property that nodes i+1, i+2, .., n are all roots of max-heaps. Decrementing
#       i in the for loop update restablishes the loop invariant of the next iteration.
#
#   Termination: i= 0. By the loop invariant, each node 1, 2, ..., n is root of a max-heap. In pariticular, node 
#       1 is. 
#
# * Time Complexity
#   The running time of BUILD-MAX-HEAP(A) is O(n), which is in linear time. 
#
def heap_build(A):
    """
    This is a procedure that builds a max-heap from an unordered array.
    A: An unordered array.
    """
    assert A.__len__() > 0

    for i in xrange(A.__len__()/2 - 1, -1, -1):
        heap_max_heapify(A, i, A.__len__())

def heap_build_it(A):
    """
    This is a procedure that builds a max-heap from an unordered array using an max-heapify procedure that
    uses an iterative control construct
    A: An unordered array.
    """
    assert A.__len__() > 0

    for i in xrange(A.__len__()/2 - 1, -1, -1):
        heap_max_heapify_it(A, i, A.__len__())

def heap_min_build(A):
    """
    This is a procedure that builds a min-heap from an unordered array.
    A: An unordered array.
    """
    assert A.__len__() > 0

    for i in xrange(A.__len__()/2 - 1, -1, -1):
        heap_min_heapify(A, i, A.__len__())

def heap_min_build_it(A):
    """
    This is a procedure that builds a min-heap from an unordered array using an max-heapify procedure that
    uses an iterative control construct
    A: An unordered array.
    """
    assert A.__len__() > 0

    for i in xrange(A.__len__()/2 - 1, -1, -1):
        heap_min_heapify_it(A, i, A.__len__())



#4.4 The Heapsort Algorithm
# * Rational
#   Since we know the maximum element of a max-heap is the root node, we can put it into the correct final position
#   in the array by exchanging it with A[n]. If now we discard node n from the heap, we observe that the children 
#   of root remain max-heaps, but the new root element might violate the max-heap propetry. All we need to do is
#   to restore the max-heap property by calling MAX-HEAPIFY(A, 1) with the heap of size n-1 . Then we repeat this
#   process for the max-heap of size n-1 down to a heap of size 2.  After all the steps, we will have an sorted 
#   array.
#   
#   Pseudo Code:
#
#   HEAPSORT(A)
#       BUILD-MAX-HEAP(A)
#       for i = A.length downto 2
#           tmp = A[i]
#           A[i] = A[1]
#           A[1] = tmp
#           A.heap-size = A.heap-size -1
#           MAX-HEAPIFY(A, 1)
#   
# * Time Complexity
#   The running time of HEAPSORT procedure is O(nlgn), since the call to BUILD-MAX-HEAP takes time O(n) and each 
#   of the n-1 calls to MAX-HEAPIFY takes time O(lgn).
#
#   Best-case:      O(nlogn)
#   Worst-case:     O(nlogn)
#   Average-case:   O(nlogn) 
#
# * Advantages
#   O(nlogn) upper bound on running time 
#   Constant upper bound on auxiliary storage. 
#
# * Disadvantages
#   Bad data cache performance since its memory references are spread throughout the heap.
#   Unstable
#   Not good for parallelization
#   

def heap_sort(A):
    """
    This is an implementation of the heapsort algorithm
    A: An array to be sorted
    """
    assert A.__len__() > 0
    heap_build(A)
    for i in xrange(A.__len__() - 1, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        heap_max_heapify(A, 0, i)





#4.5 Priority Queue
# 4.5.1 Introduction
#   A priority queue is a data structure for maintaining a set S of elements, each with an associated value called
#   a key. For a max-priority queue, the following operations are supported:
# 1) INSERT(S, x) inserts the element x into the set S.
# 2) MAXIMUM(S) returns the element of S with the largest key.
# 3) EXTRACT-MAX(S) removes and returns the element of S with the largest key.
# 4) INCREASE-KEY(S, x, k) increases the value of element's key to the new value k, which is assumed to be at 
#    least as large as x's current key value.
#
#4.5.2 Implementation
# * The MAXIMUM operation
#
#   HEAP-MAXIMUM(A)
#       return A(1)
#   
#   The running time of HEAP-MAXIMUM(A) is O(1). 
#
# * The EXTRACT-MAX operation
#
#   HEAP-EXTRACT-MAX(A)
#       if A.heap-size < 1
#           error "heap underflow"
#       max = A[1]
#       A[1] = A[A.heap-size]
#       A.heap-size = A.heap-size - 1
#       MAX-HEAPIFY(A, 1)
#       return max
#   
#   The running time of HEAP-EXTRACT-MAX is O(log n), since it performs only a constant amount of work on top of 
#   the O(log n) time for MAX-HEAPIFY
#
# * The INCREASE-KEY operation 
# 
#   HEAP-INCREASE-KEY(A, i, key)
#       if key < A[i] 
#           error "new key is smaller than current key"
#       A[i] = key
#       while i > 1 and A[PARENT(i)] < A[i]
#           exchange A[i] with A[PARENT(i)]
#           i = PARENT(i)
#
#   Note that after update the key of A[i], it may violate the property of max-heap, so the procedure then 
#   traverses a simple path from this node toward the root to find the proper place for the newly increased key.
#   As it traverses the path, it repeatedly compares an element to its parent, exchanging their keys and 
#   continuing if the elemet's key is larger, and terminating if the element's key is smaller, since the max-heap
#   property now holds
#
#   This running time of HEAP-INCREASE-KEY is O(log n)
#
# * The INSERT operation
#   
#   HEAP-MAX-INSERT(A, key)
#       A.heap-size = A.heap-size + 1
#       A[A.heap-size] = -inf
#       HEAP-INCREASE-KEY(A, A.heap-size, key)
#   
#   The running time of HEAP-MAX-INSERT is O(log n)
#
#
def heap_pqueue_maximum(A):
    assert A.__len__() > 0
    return A[0]

def heap_pqueue_extract_max(A):
    assert A.__len__() > 0
    if A.__len__() == 1:
        return A.pop(-1)
    max = A[0] 
    A[0] = A.pop(-1)
    heap_max_heapify(A, 0, A.__len__())
    return max

def heap_pqueue_increase_key(A, i, key):
    assert A.__len__() > 0
    assert A.__len__() > i
    assert A[i] <= key
    A[i] = key
    p = heap_parent(i+1) - 1
    while p >= 0 and A[p] < A[i]:
        tmp = A[p]
        A[p] = A[i]
        A[i] = tmp
        i = p
        p = heap_parent(i+1) - 1

def heap_pqueue_max_insert(A, key):
    A.append("-inf")
    heap_p_queue_increase_key(A, A.__len__() - 1, key)

#4.6 Problems
#4.6.1 The operation HEAP-DELETE(A, i) deletes the item in node i from heap A. Give an implementation of HEAP-
#   DELETE that runs in O(log n) time for an n-element max-heap
def heap_delete(A, i):
    """
    This procedure deletes the item in node from heap A
    A: A heap array .
    i: Index of the node to be deleted 
    """
    assert A.__len__() > i
    if A.__len__() ==  1:
        A.pop(-1)
    A[i] = A.pop(-1)
    p = heap_parent(i + 1) - 1
    # decides which direction to traverse: upwards or downwards  
    # If node i is the root or A[i] is smaller than its parent, however the subree rooted at i might violate
    # the max-heap property, thus we need to run MAX-HEAPIFY on node i, 
    if p < 0  or A[p] >= A[i] :        
        heap_max_heapify(A, i, A.__len__())
    # If node i is not the root and A[i] is greater than its parent, which thus violates the max-heap property,
    # so we need to traverse a simple path from node i toward the root to find the proper place for this node.
    else:
        while p >= 0 and A[p] < A[i]:
            tmp = A[p]
            A[p] = A[i]
            A[i] = tmp
            i = p
            p = heap_parent(i + 1) - 1


#4.6.2 Give an O(nlogk)-time algorithm to merge k sorted lists into one sorted list, where n is the total number 
#   of elements in all the input lists.

class SortedList:
    data = []
    def __init__(self, l=[]):
        self.data = l
    def __lt__(self, other):
        return self.data[0] < other

    def __gt__(self, other):
        return self.data[0] > other

    def __eq__(self, other):
        return self.data[0] == other

    def __ne__(self, other):
        return self.data[0] != other

    def __le__(self, other):
        if isinstance(other, SortedList):
            return self.data[0] <= other.data[0]
        elif isinstance(other, (int, float)):
            return self.data[0] <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, SortedList):
            return self.data[0] >= other.data[0]
        elif isinstance(other, (int, float)):
            return self.data[0] >= other
        else:
            return NotImplemented

    def __len__(self):
        return self.data.__len__()

    def pop(self, index=0):
        return self.data.pop(index)


def merge_sorted_lists(*lists):
    """
    This precodure merges k sorted lists into one sorted list in O(nlogk) time, where n is the total number of 
    elements in all the input lists.
    @lists: the sorted lists to be merged
    """
    assert lists.__len__() > 0
    k = lists.__len__()
    n = 0
    H = []
    R = []
    for l in lists:
        assert l.__len__() > 0
        H.append(SortedList(l))
        n = n + l.__len__()
    
    heap_min_build_it(H)
    while H.__len__() > 0 :
        heap_min_heapify_it(H, 0, H.__len__())
        R.append(H[0].pop())
        if H[0].__len__() == 0:
            del H[0]
        n = n - 1
    assert n == 0
    return R


