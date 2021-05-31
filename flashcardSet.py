from chatbot import Flashcard

flashcardSet = [

    #Heaps
    Flashcard("What is a binary heap?", "The binary heap is an array that we can be viewed as a nearly complete binary tree. Each node of the tree corresponds to an element of the array. The tree is filled on all levels except sometimes the lowest, which is filled starting from the left."),
    Flashcard("What is the max-heap property?", "For every node i other than the root A[parent(i)] >= A[i]"),
    Flashcard("What is the max-heapify procedure?", "In order to maintain the max-heap property, we call max-heapify on array A and index i. It runs in time O(log(n)) and assumes the binary trees rooted at Left(i) and Right(i) are also max-heaps - A[i] can be smaller than it's children, so max-heapify allows A[i] to 'float down' the heap. This is not to be confused with 'heapify' that initially arranges an array to a heap costing T(O(N)) "),
    
    #Trees
    
    #Linked Lists
    Flashcard("What are the time complexities of 'Add Node at Tail', 'Add Node at Head', 'Delete Head Node', 'Delete Non-Head Node' of a Singly Linked List", f"1.)Add Node at Tail: T(O(N))\n2.)Add Node at Head: T(O(1))\n3.)Delete Head Node T(O(1))\n4.)Delete Non-Head Node T(O(K)) where K is position of Nodew"),

    #Arrays


    #Strings
    Flashcard("Given two strings, how do you know if one string is an anagram of the other?", "1.) Sort both strings and compare the strings 2.) Create a hashtable with a key-value pair of the character to its frequency. Use the other string to decrement the counts in the hashtable. You should be left with an empty hashtable"),
    Flashcard("What is a palindrome?", "When a string is read the same way forward and backwards. Ex.) 'racecar', 'cattac', 'palinnilap'" ),

    Flashcard("What are commmon edge cases related to strings?", f"1.)Empty strings\n2.)Strings with 1 or 2 characters\n3.Strings with repeating characters\n4.)Strings with only one distinct character"),
    Flashcard()
    
    ]