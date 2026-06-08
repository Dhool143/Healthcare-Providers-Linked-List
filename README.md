HealthMerge Inc. – Merge Two Sorted Linked Lists

Overview

HealthMerge Inc. recently acquired CarePlus. Both healthcare providers store patient records in linked lists sorted by Social Security Number (SSN).

The goal of this project is to merge two sorted linked lists into a single sorted linked list while preserving all patient records, including duplicate SSNs.

This solution maintains the sorted order of the records, allowing healthcare professionals to efficiently access patient information.


Problem Statement

Given the heads of two sorted linked lists representing patient records, merge them into one sorted linked list.

Requirements:

* Maintain ascending SSN order.
* Preserve duplicate records.
* Reuse existing nodes whenever possible.
* Return the head of the merged linked list.



Clarifying Questions

Before implementing the solution, the following questions were considered:

1. Are both linked lists already sorted in ascending order by SSN?
2. Can duplicate SSNs exist?
3. Should duplicate records be preserved?
4. Can one or both linked lists be empty?
5. Can existing nodes be reused instead of creating new nodes?
6. What should happen if both lists are empty?



Assumptions

* Both linked lists are sorted in ascending order.
* Duplicate SSNs should be preserved.
* Existing nodes can be reused.
* Either linked list may be empty.
* If both lists are empty, the function returns None.



Solution Approach

An iterative approach is used with a dummy node.

Steps

1. Create a dummy node.
2. Create a current pointer.
3. Compare the SSNs of both lists.
4. Attach the node with the smaller SSN.
5. Move the corresponding pointer forward.
6. Continue until one list becomes empty.
7. Attach any remaining nodes.
8. Return the merged list.

⸻

Flowchart

Start
  |
  v
Compare current nodes of List1 and List2
  |
  +---- List1 SSN <= List2 SSN?
  |           |
 Yes          No
  |           |
Take List1   Take List2
Node         Node
  |           |
Move         Move
List1        List2
Pointer      Pointer
   \         /
    \       /
     Continue
        |
        v
One list empty?
        |
       Yes
        |
Attach remaining nodes
        |
        v
Return merged list
        |
       End

⸻

Files

main.py

Contains:

* PatientNode class
* merge_patient_lists() function

test_solution.py

Contains:

* Unit tests
* Helper functions
* Normal test cases
* Edge test cases

⸻

Test Cases

Normal Cases

Test Case 1

Input:

[100,300,500]
[200,400,600]

Output:

[100,200,300,400,500,600]

Test Case 2

Input:

[100,300]
[200,400,500,600]

Output:

[100,200,300,400,500,600]

Test Case 3

Input:

[100,300,500]
[100,400,500]

Output:

[100,100,300,400,500,500]

Edge Cases

Test Case 4

Input:

[]
[100,200,300]

Output:

[100,200,300]

Test Case 5

Input:

[100,200,300]
[]

Output:

[100,200,300]

Test Case 6

Input:

[]
[]

Output:

[]

⸻





Time Complexity

Let:

* n = number of nodes in the first linked list
* m = number of nodes in the second linked list

Each node is visited exactly once.

Time Complexity:

O(n + m)

⸻

Space Complexity

The solution reuses existing nodes and only uses a few pointers.

Space Complexity:

O(1)

Optimization Discussion

This solution is already optimal.

* Every node must be visited at least once, so O(n + m) is the best possible time complexity.
* Existing nodes are reused, resulting in O(1) auxiliary space.

No further meaningful optimization is possible without changing the problem requirements.


Conclusion

This project successfully merges two sorted linked lists of patient records while preserving duplicates and maintaining sorted order.

Final Complexity:

* Time Complexity: O(n + m)
* Space Complexity: O(1)

The implementation is efficient, readable, and scalable for managing patient records in a healthcare system.