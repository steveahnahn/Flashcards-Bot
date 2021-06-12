from chatbot import Flashcard

flashcardSet = [

    #Heaps
    Flashcard("What is a binary heap?", "The binary heap is an array that we can be viewed as a nearly complete binary tree. Each node of the tree corresponds to an element of the array. The tree is filled on all levels except sometimes the lowest, which is filled starting from the left."),
    Flashcard("What is the max-heap property?", "For every node i other than the root A[parent(i)] >= A[i]"),
    Flashcard("What is the max-heapify procedure?", "In order to maintain the max-heap property, we call max-heapify on array A and index i. It runs in time O(log(n)) and assumes the binary trees rooted at Left(i) and Right(i) are also max-heaps - A[i] can be smaller than it's children, so max-heapify allows A[i] to 'float down' the heap. This is not to be confused with 'heapify' that initially arranges an array to a heap costing T(O(N)) "),
    
    #Trees
    Flashcard("What is a complete binary tree?", "A binary tree in which every level except possibly the last level is completed filled and all nodes are as far left as possible"),
    Flashcard("What is a full binary tree?", "A tree in which every node other than the leaves have two children."),
    Flashcard("What is Depth First Search?", "A Tree or Graph traversal algorithm where you visit all of the neighbor's neighbors before you exhaustively search the current node's neighbors, hence going deep before going wide"),
    Flashcard("What is Breadth First Search", "A Tree or Graph traversal algorithm where you exhaustively visit all of the current node's neighbors beefore visiting any of the neighbor's neighors, hence going wide before going deep."),

    #Linked Lists
    Flashcard("What are the time complexities of 'Add Node at Tail', 'Add Node at Head', 'Delete Head Node', 'Delete Non-Head Node' of a Singly Linked List", f"1.)Add Node at Tail: T(O(N))\n2.)Add Node at Head: T(O(1))\n3.)Delete Head Node T(O(1))\n4.)Delete Non-Head Node T(O(K)) where K is position of Nodew"),
    Flashcard("How do you detect if a Linked List has a cycle in it?", "Use Floyd's Cycle detection algorithm where one pointer traverses the Linked List twice as fast as the other pointer and if they ever meet on the same node, a cycle exists"),
    Flashcard("How do you reverse a singly Linked List?", "Iterate through the Linked List and save node.next to a temp variable. Then you may proceed to change the pointers where node.next = prev, prev = node, node = temp"),
    Flashcard("What are the time complexities of 'Add/Delete Node at Tail', 'Add/Delete Node at Head', 'Delete Node given Node'", "1.)Add/Delete Node at Tail: T(O(1))\n2.)Add/Delete Node at Head: T(O(1))\n3.)Delete Node given Node: T(O(1))"),
    
    #Arrays
    Flashcard("What some common pointer traversal methods to solve Array problems?", "1.)Read/Write Pointers where the read pointer traverses and swaps with the write pointer\n2.)Traversing from the start and end of the array\n3.)Double loops with two pointers"),
    Flashcard("When can you use Binary Search and what is the time/space complexity", "Use Binary Search when your search space is monotonically increasing. The time/space is T(O(LogN)) S(O(1))"),

    #Strings
    Flashcard("Given two strings, how do you know if one string is an anagram of the other?", "1.) Sort both strings and compare the strings 2.) Create a hashtable with a key-value pair of the character to its frequency. Use the other string to decrement the counts in the hashtable. You should be left with an empty hashtable"),
    Flashcard("What is a palindrome?", "When a string is read the same way forward and backwards. Ex.) 'racecar', 'cattac', 'palinnilap'" ),
    Flashcard("What are commmon edge cases related to strings?", f"1.)Empty strings\n2.)Strings with 1 or 2 characters\n3.Strings with repeating characters\n4.)Strings with only one distinct character"),
    Flashcard("What are the method functions and time complexities of a Trie?", "1.)Inserting words into a Trie T(O(N*M)) where N is the longest word and M is the number of words\n2.)Search through the whole Trie with BFS or DFS T(O(N*M))\n3.)Search a prefix/word T(O(N)) where N is the length of the word"),
    Flashcard("Why is storing counts of words in a Trie more spaced optimized than say a Hash Table?", "Trie's benefit from the fact that if a prefix of a word already exists in the Trie, it does not need to be recreated and can either extend the node's path or leverage its prefix to update its count"), 

    #Graphs
    Flashcard("Regarding Graphs - what is Bidirectional Search?", "Searching for a target node from a starting node, executing BFS from both the target and starting node to decrease time complexity from T(O(B^d)) to T(O(B^d/2))"),
    Flashcard("Regarding Graphs - what is topological sort and how do you algorithmically solve it?", "A top sort will ensure that a node's dependency comes first before the node itself that is only applicable to DAGs. To solve it use Kahn's algorithm\n 1.)Create an array that holds the indegrees for all nodes\n 2.)Add all nodes with 0 indegrees to a Queue, adding to the top sort when processed\n 3.)Decrease the indegrees by 1 of all nodes that are affected and re-adding newly 0 indegree nodes"),
    Flashcard("Regarding Graphs - what is a strongly connected component and how do we know if we have one?", "A SCC is when every vertex can reach another vertex through a directed path. You can use Kosaraju's algorithm to test for a SCC graph. Kosaraju's algorithm:\n 1.)Run DFS on the whole graph, if the graph is disconnected the visited set will have some vertices not included. The idea is that the last vertex visited in the DFS will be the mother vertex.\n2.)Keep track of the last vertex, reset the visited list and run DFS starting from the last vertex and if all are visited, it is the mother vertex."),
    Flashcard("What is a minimum spanning tree and how do we generate one?", "A minimum spanning tree is an acylcic graph with V verticies and V-1 edges generated from a graph. Prims and Kahn's algorithm is sufficient to find the MST."),
    Flashcard("What does Dijkstra's Algorithm do?", "Dijkstra's algorithm finds the shortest path for a single source and the graph must not contain any negative edges"),
    Flashcard("Regarding Graphs - how do you detect a cycle within a graph?", "Do BFS or DFS and if any of the node's neighbors have been already seen and it's parent is not the current node, cycle detected"),
    Flashcard("What is the solution to the well known Chess Knight Graph Problem", "1.)Create a queue and enqueue the source cell having a distance of 0\n2.)While queue, pop the node and if node is the destination, return distance otherwise mark the node and add all 8 other possible movements that knights can traverse with +1 distance while ensuring its within the board boundaries and not previously visited.\n3.)Use a directions tuple array to help you with iterating through all possible movements"),
    # Flashcard(""),
    ]

