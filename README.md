# 🔍 Find the Smallest Element in an AVL Tree

This project demonstrates how to find the **smallest element** in an AVL tree (or any Binary Search Tree) using both **iterative** and **recursive** approaches.

##  What Is an AVL Tree?

An **AVL tree** is a type of self-balancing Binary Search Tree (BST). While AVL trees maintain balance to ensure optimal performance, the logic to find the smallest element remains:

> The **leftmost node** in a BST is always the smallest.

---

##  Two Approaches

### 1. Iterative Approach

This method starts at the root and repeatedly moves to the left child until it reaches the leftmost node. This is efficient and avoids the call stack overhead of recursion.

### 2. Recursive Approach

This method calls itself on the left child until it finds a node with no left child — which is the smallest node. It's cleaner and elegant, especially for small to medium trees.

---

##  Example

Given the following tree:

      50
     /  \
   30    70
  /  \   /  \
20   40 60   80

Both approaches correctly return `20` as the smallest element.


