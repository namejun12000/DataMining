Title: Programming Assignment 3
Author: Nam Jun Lee

Supported set of language: Python

Using libraries:

1. import numpy as np
- It serves to create an n-dimensional array

2. import statistics
- It serves to average in this program as a mathematical-statistical function

Program Description:

The program uses binary classification algorithms and multi-classification algorithms to demonstrate each of the mistakes and accuracy for training and testing two data, as well as standard and average perceptrons. First, the fortune cookie data is loaded and pre-processed before classifying. Use stop lists to form a vocabulary. In this process, the data included in the stop list is removed and sorted in order alphabetically. Then convert the data into feature vectors and then generate a set of training data features. Next, implement a binary classifier to begin learning. First, the weights and number of mistakes are obtained, and then the weights obtained here are used to obtain accuracy for each iteration and put them in the accuracy list. At this time, the learning rate is set to 1. This accuracy list is then used to obtain accuracy with standard perceptron accuracy and average perceptions. This classification algorithm applies to both fortune cookie training data and test data.
After that, OCR data is retrieved and pre-processed before multi-classification. First, the data is loaded to separate feature and label lists. At this point, remove the 'im' in front and the '_' in the back. After this process, 128 binary characters will be entered in the feature list, and the label will be the alphabet in the last row of the line. This data is then converted to an n-dimensional array. And later, create a dictionary of index and letter forms that create for accuracy later. Next, implement a multi-classifier to start learning. At this time, the class should be set, but the class is the alphabets on the label, so the total number of alphabets is set to 26. In addition, the learning rate is set to 1.  Using the weights and real numbers obtained from the classifier, the accuracy is calculated for each iteration and placed in the accuracy list. This accuracy list is then used to obtain accuracy with standard perceptron accuracy and average perceptions. This classification algorithm applies to both OCR training data and test data. Finally, outputs these obtained values sequentially to the output.txt file.

Result:

The first block was applied to fortune cookie data using binary classification algorithms. The second block was applied to the OCR data using a multi-classification algorithm. These two blocks first show the mistakes for each iteration, then show the training accuracy and test accuracy, and finally show the standard perceptron and average perceptron of each train and test.

Fortune Cookie Classifier
iteration-1  133
iteration-2  97
iteration-3  97
iteration-4  97
iteration-5  97
iteration-6  97
iteration-7  97
iteration-8  97
iteration-9  97
iteration-10  97
iteration-11  97
iteration-12  97
iteration-13  97
iteration-14  97
iteration-15  97
iteration-16  97
iteration-17  97
iteration-18  97
iteration-19  97
iteration-20  97

iteration-1  0.6987577639751553  0.7128712871287128
iteration-2  0.70092781914278  0.7199294186844426
iteration-3  0.7009345584445428  0.7199993011750935
iteration-4  0.7009345793740513  0.7199999930809415
iteration-5  0.7009345794390499  0.7199999999314943
iteration-6  0.7009345794392516  0.7199999999993218
iteration-7  0.7009345794392524  0.7199999999999932
iteration-8  0.7009345794392524  0.72
iteration-9  0.7009345794392524  0.72
iteration-10  0.7009345794392524  0.72
iteration-11  0.7009345794392524  0.72
iteration-12  0.7009345794392524  0.72
iteration-13  0.7009345794392524  0.72
iteration-14  0.7009345794392524  0.72
iteration-15  0.7009345794392524  0.72
iteration-16  0.7009345794392524  0.72
iteration-17  0.7009345794392524  0.72
iteration-18  0.7009345794392524  0.72
iteration-19  0.7009345794392524  0.72
iteration-20  0.7009345794392524  0.72

0.7009345794392524 0.72
0.7008253995982182 0.71964

OCR Classifier
iteration-1  2072
iteration-2  1705
iteration-3  1621
iteration-4  1535
iteration-5  1483
iteration-6  1495
iteration-7  1514
iteration-8  1449
iteration-9  1446
iteration-10  1425
iteration-11  1390
iteration-12  1405
iteration-13  1378
iteration-14  1367
iteration-15  1383
iteration-16  1362
iteration-17  1373
iteration-18  1347
iteration-19  1345
iteration-20  1389

iteration-1  0.6517218973359324  0.6586515199326812
iteration-2  0.6518630543420697  0.6586653760706833
iteration-3  0.6518630849153871  0.6586653763621767
iteration-4  0.651863084922009  0.6586653763621829
iteration-5  0.6518630849220105  0.6586653763621829
iteration-6  0.6518630849220105  0.6586653763621829
iteration-7  0.6518630849220105  0.6586653763621829
iteration-8  0.6518630849220105  0.6586653763621829
iteration-9  0.6518630849220105  0.6586653763621829
iteration-10  0.6518630849220105  0.6586653763621829
iteration-11  0.6518630849220105  0.6586653763621829
iteration-12  0.6518630849220105  0.6586653763621829
iteration-13  0.6518630849220105  0.6586653763621829
iteration-14  0.6518630849220105  0.6586653763621829
iteration-15  0.6518630849220105  0.6586653763621829
iteration-16  0.6518630849220105  0.6586653763621829
iteration-17  0.6518630849220105  0.6586653763621829
iteration-18  0.6518630849220105  0.6586653763621829
iteration-19  0.6518630849220105  0.6586653763621829
iteration-20  0.6518630849220105  0.6586653763621829

0.6518630849220105 0.6586653763621829
0.6518560240133783 0.6586646835261325
