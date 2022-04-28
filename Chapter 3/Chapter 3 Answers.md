#Complexity Science Chapter 3 Answers
##Exercise 1

1. All are O(n^(3))
2. It is O(n^(3))
3. If `f` is in `O(g)`, then `af + b` is also in `O(g)` for some specified values of x.
4. If `f1` and `f2` are in `O(g)`, then `f1 + f2` is also in `O(g)` for some specified values of x. 
5. Not sure. If `f1` and `f2` are in `O(h)` and `O(g)` respectively, then `f1 + f2` should be in? Why though?
6. Not sure. Same reasoning as above?

##Exercise 2
1. A "comparison sort" does this: 'examines the data only by comparing two elements with a comparison operator.' 
	* The best worst-case order of growth for a comparison sort is n^(2). 
	* The best worst-case order of growth for any search algorithm is n * n!.
2. The order of growth of a Bubble Sort is n^(2). Obama thinks it's the wrong way to go because for ordering tons of items, it would take an exceedingly long time.
3. The order of growth of a Radix Sort is O(n.k), for n numbers each containing k digits. Preconditions: need each number to contain the same number of digits.
4. A stable sort is one that "maintains the relative order of records with equal keys". This might matter in practice because the order may be important.
5. The worst sorting algorithm that has a name is called the Bogosort.
6. What sort algorithm does the C library use? What sort algorithm does Python use? Are these algorithms stable? You might have to Google around to find these answers.
	* The C library uses a  sorting algorithm known as qsort,which is basically a quicksort algorithm.
	* Python by default uses a sorting algorithm called Timsort which essentially is a hybrid of both insertion sort and merge sort. This algorithm finds subsets of 	   pre-sorted data and then uses these subsets to further efficiently sort the remaining elements. 
7. Many of the non-comparison sorts are linear, so why does does Python use an O(n logn) comparison sort?
	* Python uses the O(n logn) comparison sort because in its worst case, the memory storage is n, and it's fast.

##Exercise 3
N/A. I read the "bisect" module documentation. Good to know.

##Exercise 4
Skipped.

##Exercise 5
Skipped.

