// my practices of Leetcode sample questions

1. Longest Substring Without Repeating Characters

2. Reverse a singly linked list.

3. You are climbing a stair case. It takes n steps to reach to the top.

4. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? (Note: Given n will be a positive integer.)

5. Given a linked list, remove the n-th node from the end of list and return its head.

6. Given a binary tree, determine if it is a valid binary search tree (BST).

7. Given a singly linked list, determine if it is a palindrome.

8. Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

9. Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

10. Given an array with N suppliers that includes city, supplier_name, prices and an array with M clients looking for hotels with input in the form of city and numbers of days ordered before check-in, please design an program to find all possible prices according to client's requirement and hotel supplier's prices conditions in ascending order.
If the client booked the hotel before 1 day of checkin, the price would be increased by 50% in A.
If the client booked the hotel within 3 days before the checkin, the order cannot be completed.
If the client booked the hotel 7 days or more than 7 days before the day of checkin, the price would be decreased by 10% in A.
If the client booked the hotel within 7 day of checkin, the price would be increased by 10% in A.
eg:
input for hotels:
7
Toronto,A,100.00
North York,B,250
Waterloo,C,19.99
Toronto,D,100.00
Kitchener,F,25
Kitchener,F,24
Kitchener,F,25

inputs for clients:
4,
Toronto,1
North York,2
Waterloo,8
Kitchener,10

output:
110.00 150.00
None
17.99
24 25
