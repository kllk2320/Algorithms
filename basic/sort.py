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
    if A.__len__() < 2 : 
        return A
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

