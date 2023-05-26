Title: Programming Assignment 1
Author: Nam Jun Lee

Supported set of language: Python

Using libraries: 

1. from itertools import combinations
- It serves to combine the items in the basket. 
- ex) [A, B, C] => [(A,B), (A,C), (B,C)]

2. from timeit import default_timer
- It serves to show the time it takes for each step in the console window.

Program Description:

The program uses an A-priori algorithm to show each of two or three frequent sets up to five in a highly confidence score order. First, read the file "browsing-data.txt" and count the number of each item through the pass 1. At this time, the support is fixed to 100, and items with more than 100 numbers are extracted. After that, find the item obtained through pass1 and the frequent item set with the total item size of 2, and count the number.  And find the set of items obtained pass 2 and the set of frequent items with the total size of 3 and then count the number. At this time, in pass 2 and pass 3, only a set of items with a number of 100 or more is extracted by fixing the support at 100. After that, the confidence of the set of frequent items of size 2 and 3 is calculated, and the set of frequent items of size 2 and 3 having the top 5 reliability scores is extracted, respectively. Finally, a set of frequent items with sizes 2 and 3 having the top 5 reliability scores is output to "output.txt".


Result:

It took a considerable amount of time to proceed with the pass 3 process and the confidence score of triple of set is rounded to the first decimal place.
OUTPUT A: top 5 pair of set, and each confidence score
OUTPUT B: top 5 triple of set, and each confidence score

OUTPUT A
DAI93865 FRO40251 1.0
GRO85051 FRO40251 0.999176276771005
GRO38636 FRO40251 0.9906542056074766
ELE12951 FRO40251 0.9905660377358491
DAI88079 FRO40251 0.9867256637168141
OUTPUT B
ELE92920 DAI23334 DAI62779 1.0
SNA18336 ELE92920 DAI62779 1.0
GRO73461 GRO85051 FRO40251 1.0
SNA18336 ELE17451 DAI62779 1.0
SNA18336 ELE17451 ELE92920 1.0


