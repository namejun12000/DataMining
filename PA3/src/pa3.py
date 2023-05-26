# import modules
import numpy as np
import statistics

# Global variables
# learning rate
learningRate = 1
# num of alphabet (using OCR)
CLASS = 26
# iteration
iteration = 20

# directory of text files
output_file = "../output.txt"
cookieT = "../data/fortune-cookie-data/traindata.txt"
cookieTLabel = "../data/fortune-cookie-data/trainlabels.txt"
cookieStop = "../data/fortune-cookie-data/stoplist.txt"
cookieTe = "../data/fortune-cookie-data/testdata.txt"
cookieTeLabel = "../data/fortune-cookie-data/testlabels.txt"
ocrT = "../data/OCR-data/ocr_train.txt"
ocrTe = "../data/OCR-data/ocr_test.txt"


# file reading
def read_file(input_file):
    with open(input_file, "r") as txt_file:
        # list containing each line in input_file
        lines = txt_file.readlines()
    # remove specific character \n and put them on the list
    lst = [line.rstrip('\n') for line in lines]
    # return list
    return lst


# form the vocabulary
def formVoca(file, stop):
    # empty voca set
    voca = set()
    # remove the words contained in the stop file and configure team as set of voca
    for lst in file:
        for word in lst.split():
            if word not in stop:
                voca.add(word)
    # return sort alphabetically vocabulary set
    return sorted(voca)


# convert the data
def convertVector(data, voca):
    # empty convert list
    convertList = list()
    # word in data
    word = [[i for i in line.split()] for line in data]
    # each slot in that vectors takes the value of 0 or 1
    for i in word:
        # vector list
        vecList = list()
        for j in voca:
            # word in the voca
            if j in i:
                # add 1
                vecList.append(1)
            else:  # word not in voca
                # add 0
                vecList.append(0)
        # fill the convert list
        convertList.append(vecList)
    # return convert data list
    return convertList


# data into a set of features
def setListData(convList, label):
    # empty list
    setList = list()
    # fill the st list with converted data and labels
    for i in range(len(convList)):
        setList.append((convList[i], int(label[i])))
    # retrun set of features list
    return setList


# binary classifier with perceptron weight each iteration
def binaryClassifierPerceptron(feature, example):
    # empty mistake list
    misList = list()
    # set initalize the weights to zero ndarray
    w = np.zeros(len(example), dtype=int)
    # compute number of mistakes and update the weight each iteration
    for i in range(iteration):  # repeat each iteration
        # set initalize mistake
        mistake = 0
        # examples
        for j in feature:
            # predict using the current weights
            xt = np.array(j[0])
            hatyt = xt.dot(w)
            # mistake
            if hatyt <= 0:
                yt = np.array(j[1])
                w = w + learningRate * (xt * yt)  # update the weight
                mistake += 1  # update the num of mistake
        # fill the num of mistake each iteration
        misList.append(mistake)
    # return final weight and mistake list
    return w, misList


# compute the accuracy after each iteration (binary class)
def findBinaryClassifierAccuracy(weight, example):
    # empty accuracy list
    accuracy = list()
    # set not mistake
    noMis = 0
    # compute the accuracy using weight vector for each iteration
    for i in range(iteration):
        # examples
        for j in example:
            xt = np.array(j[0])
            hatyt = xt.dot(weight)
            if hatyt > 0:  # if not mistake
                noMis += 1  # update the num of not mistake
        # calcuate the accuracy of each iteration
        noMis = noMis / len(example)
        # fill the each iteration of accuracy in accuracy list
        accuracy.append(noMis)
    # return accuracy list
    return accuracy


# separate the data to input features and output label
def separateFeatureLabel(input_file):
    # list of each feature and label
    feature = list()
    label = list()
    # doing separate the data
    for line in input_file:
        # divide lines with specific characters (\t) first
        val = line.split('\t')
        # if the length of the line is greater than 3 and fourth index of the line contains _ after dividing the line,
        if (len(val) > 3) and (val[3] == '_'):
            # fill the feature list with the second line index removed from the im
            feature.append(val[1].lstrip('im'))
            # fill the label list with last index
            label.append(val[2])
    # return feature and label list
    return feature, label


# convert the data
def convertOCR(data):
    # 128 binary values
    feature = len(data[0])
    # total length of input
    example = len(data)
    # generates an array of zeroes by the total length and feature of the input data
    dataArray = np.zeros((example, feature + 1))
    # if the resulting array contains a value, add 1 to fill the ndarray
    for i, val in enumerate(data):
        for j, binaryImage in enumerate(val):
            dataArray[i][j] = int(binaryImage)
        dataArray[i][feature] = 1
    # return length of feature and convert the ndarray data
    return feature, dataArray


# form the vocabulary
def formlabel(data):
    # sorting separated label data in a dictionary
    outputLabel = sorted(list(set(data)))
    # set each letter and index dictionary
    letter = dict()
    index = dict()
    # in the letter dict with the letter key is created, and the index dict with the index key is created
    for i, l in enumerate(outputLabel):
        letter[l] = i
        index[i] = l
    # return each index and letter dictionary
    return index, letter


# multi-class classifier with perceptron weight
def multiClassClassifierPerceptron(feature, example, label, outputLb):
    # set initalize the weights to zero ndarray for features
    w = np.zeros((CLASS, feature + 1))
    # set empty mistake list
    misList = list()
    # length of example
    D = len(example)
    # compute number of mistakes and update the weight each iteration
    for i in range(iteration):
        mis = 0  # set initalize mistake
        # repeat each examples
        for j in range(D):
            # set initalize the predict zero ndarray for class
            pred = np.zeros((1, CLASS))
            # predict using the current weights for each class
            for k in range(CLASS):
                pred[0][k] = np.dot(example[j], np.transpose(w[k]))
            wyt = np.argmax(pred)
            hatwyt = outputLb[label[j]]
            # if mistake
            if wyt <= 0 or wyt != hatwyt:
                # update the mistake
                mis += 1
                # update the weights
                w[wyt] = w[wyt] - learningRate * example[j]
                w[hatwyt] = w[hatwyt] + learningRate * example[j]
        # fill the num of mistake each iteration
        misList.append(mis)
    # return final weight and mistake list
    return w, misList


# compute the accuracy after each iteration (multi class)
def findMultiClassifierAccuracy(weight, examples, label, outputLbIndex):
    # set not mistake
    noMis = 0
    # set empty accuracy list
    accuracyList = list()
    # total length of data (shape)
    totData = len(examples)
    # compute the accuracy using weight vector for each iteration
    # for each iteration
    for a in range(iteration):
        # for each example
        for i in range(totData):
            # set zero ndarray size of class (26)
            zeroLb = np.zeros((1, CLASS))
            # for each class
            for j in range(CLASS):
                zeroLb[0][j] = np.dot(examples[i], np.transpose(weight[j]))
            if outputLbIndex[np.argmax(zeroLb)] == label[i]:  # not mistake
                noMis += 1  # update not mistake
        noMis = noMis / totData  # calcualte the accuracy
        # fill the accuracy for each iteration
        accuracyList.append(noMis)
    # return accuracy list
    return accuracyList


# find the average perceptron accuracy
def findAverageAccuracy(accuracy):
    # the average of the elements in the accuracy list is calcualted and returned
    return statistics.mean(accuracy)


# find the standard perceptron accuracy
def findStandardAccuracy(accuracy):
    # returns the final accuracy of elemetns in the accuracy list
    return accuracy[-1]


# file dumping
def dump_output(noMisFortune, tAccFortune, teAccFortune, tStPercept, teStPercept, tAvgPercept, teAvgPercept,
                noMisOCR, tAccOCR, teAccOCR, tStPerOCR, teStPerOCR, tAvgPerOCR, teAvgPerOCR):
    with open(output_file, "w") as txt_file:
        txt_file.write("Fortune Cookie Classifier\n")
        # set iteration (1-20)
        nums = list(range(iteration))
        # write num of mistake cookie train for each iteration
        for conf, num in zip(noMisFortune, nums):
            txt_file.write(f'iteration-{num + 1}  {conf}\n')
        txt_file.write("\n")
        # write cookie train and test accuracies for each iteration
        for conf1, conf2, num1 in zip(tAccFortune, teAccFortune, nums):
            txt_file.write(f'iteration-{num1 + 1}  {conf1}  {conf2}\n')
        txt_file.write("\n")
        # write cookie train and test standard perceptron and average perceptron
        conf3, conf4, conf5, conf6 = tStPercept, teStPercept, tAvgPercept, teAvgPercept
        txt_file.write(f'{conf3} {conf4}\n')
        txt_file.write(f'{conf5} {conf6}\n\n')
        # OCR
        txt_file.write("OCR Classifier\n")
        # write the num of mistake OCR train for each iteration
        for conf7, num2 in zip(noMisOCR, nums):
            txt_file.write(f'iteration-{num2 + 1}  {conf7}\n')
        txt_file.write("\n")
        # write OCR train and test accuracies for each iteration
        for conf8, conf9, num3 in zip(tAccOCR, teAccOCR, nums):
            txt_file.write(f'iteration-{num3 + 1}  {conf8}  {conf9}\n')
        txt_file.write("\n")
        # write OCR train and test standard perceptron and average perceptron
        conf10, conf11, conf12, conf13 = tStPerOCR, teStPerOCR, tAvgPerOCR, teAvgPerOCR
        txt_file.write(f'{conf10} {conf11}\n')
        txt_file.write(f'{conf12} {conf13}\n')
    return


def main():
    # Fortune Cookie
    # train
    # load train and train label
    print("**********Fortune Cookie**********\n")
    print("Train, Train Label, and Stop Files Read in progress...")
    cookieTrain = read_file(cookieT)
    cookieTrainLab = read_file(cookieTLabel)
    # load stop label
    stop = read_file(cookieStop)
    print('File read completely!!!\n\n')
    # form of voca
    print("Voca Forming in progress...")
    vocabulary = formVoca(cookieTrain, stop)
    print("Forming successfully!!!\n\n")
    # convert train data
    print("Cookie train data converting in progress...")
    cookieConvertTrain = convertVector(cookieTrain, vocabulary)
    print("Data converting successfully!!!\n\n")
    # set cookie train
    print("Cookie Train Setting in progress...")
    ckTrain = setListData(cookieConvertTrain, cookieTrainLab)
    print("Setting successfully!!!\n\n")
    # weight and mistake (cookie train)
    print("Compute the Weight and Mistake in progress...")
    ckTrainWeight, ckTrainMistake = binaryClassifierPerceptron(ckTrain, vocabulary)
    print("Compute successfully!!!\n\n")
    # accuracy (cookie train)
    print("Compute the accuracy in progress...")
    ckTrainAcc = findBinaryClassifierAccuracy(ckTrainWeight, ckTrain)
    print("Compute successfully!!!\n\n")
    # standard and average accuracy (cookie train)
    print("Compute the standard and average accuracy in progress...")
    ckTrainStdAcc = findStandardAccuracy(ckTrainAcc)
    ckTrainAvgAcc = findAverageAccuracy(ckTrainAcc)
    print("Compute successfully!!!\n\n")
    # test
    # load cookie test and test label
    print("Test, and Test Label Files Read in progress...")
    cookieTest = read_file(cookieTe)
    cookieTestLab = read_file(cookieTeLabel)
    print('File read completely!!!\n\n')
    # form of voca
    print("Voca Forming in progress...")
    vocabulary1 = formVoca(cookieTest, stop)
    print("Forming successfully!!!\n\n")
    # convert test data
    print("Cookie test data converting in progress...")
    cookieConvertTest = convertVector(cookieTest, vocabulary1)
    print("Data converting successfully!!!\n\n")
    # set cookie test
    print("Cookie Test Setting in progress...")
    ckTest = setListData(cookieConvertTest, cookieTestLab)
    print("Setting successfully!!!\n\n")
    # weight and mistake (cookie test)
    print("Compute the Weight and Mistake in progress...")
    ckTestWeight, ckTestMistake = binaryClassifierPerceptron(ckTest, vocabulary1)
    print("Compute successfully!!!\n\n")
    #  accuracy (cookie test)
    print("Compute the accuracy in progress...")
    ckTestAcc = findBinaryClassifierAccuracy(ckTestWeight, ckTest)
    print("Compute successfully!!!\n\n")
    # standard and average accuracy (cookie test)
    print("Compute the standard and average accuracy in progress...")
    ckTestStdAcc = findStandardAccuracy(ckTestAcc)
    ckTestAvgAcc = findAverageAccuracy(ckTestAcc)
    print("Compute successfully!!!\n\n")
    # OCR
    # train
    # load ocr train
    print("OCR Train File Read in progress...")
    ocrTr = read_file(ocrT)
    print('File read completely!!!\n\n')
    # separate feature and label
    print('Separating feature and label in progress...')
    ocrTFeature, ocrTLabel = separateFeatureLabel(ocrTr)
    print("Separating successfully!!!\n\n")
    # convert train data
    print("OCR train data converting and setting in progress...")
    feature, ocrTrain = convertOCR(ocrTFeature)
    print("Data converting successfully!!!\n\n")
    # form of label
    print("Letter Forming in progress...")
    letterIndex, letter = formlabel(ocrTLabel)
    print("Letter Forming successfully!!!\n\n")
    # weight and mistake (ocr train)
    print("Compute the Weight and Mistake in progress...")
    ocrTrainWeight, ocrTrainMistake = multiClassClassifierPerceptron(feature, ocrTrain, ocrTLabel, letter)
    print("Compute successfully!!!\n\n")
    # accuracy (ocr train)
    print("Compute the accuracy in progress...")
    ocrTrainAcc = findMultiClassifierAccuracy(ocrTrainWeight, ocrTrain, ocrTLabel, letterIndex)
    print("Compute successfully!!!\n\n")
    # standard and average accuracy (ocr train)
    print("Compute the standard and average accuracy in progress...")
    ocrTrainStdAcc = findStandardAccuracy(ocrTrainAcc)
    ocrTrainAvgAcc = findAverageAccuracy(ocrTrainAcc)
    print("Compute successfully!!!\n\n")
    # test
    # load ocr test
    print("**********OCR**********\n")
    print("OCR Test File Read in progress...")
    ocrTes = read_file(ocrTe)
    print('File read completely!!!\n\n')
    # separate feature and label
    print('Separating feature and label in progress...')
    ocrTeFeature, ocrTeLabel = separateFeatureLabel(ocrTes)
    print("Separating successfully!!!\n\n")
    # convert test data
    print("OCR test data converting and setting in progress...")
    featureTe, ocrTest = convertOCR(ocrTeFeature)
    print("Data converting successfully!!!\n\n")
    # form of label
    print("Letter Forming in progress...")
    letterIndexTest, letterTest = formlabel(ocrTeLabel)
    print("Letter Forming successfully!!!\n\n")
    # weight and mistake (ocr test)
    print("Compute the Weight and Mistake in progress...")
    ocrTestWeight, ocrTestMistake = multiClassClassifierPerceptron(featureTe, ocrTest, ocrTeLabel, letterTest)
    print("Compute successfully!!!\n\n")
    # accuracy (ocr test)
    print("Compute the accuracy in progress...")
    ocrTestAcc = findMultiClassifierAccuracy(ocrTestWeight, ocrTest, ocrTeLabel, letterIndexTest)
    print("Compute successfully!!!\n\n")
    # standard and average accuracy (ocr test)
    print("Compute the standard and average accuracy in progress...")
    ocrTestStdAcc = findStandardAccuracy(ocrTestAcc)
    ocrTestAvgAcc = findAverageAccuracy(ocrTestAcc)
    print("Compute successfully!!!\n\n")
    # dump
    print("Dump in progress...")
    dump_output(ckTrainMistake, ckTrainAcc, ckTestAcc, ckTrainStdAcc, ckTestStdAcc, ckTrainAvgAcc, ckTestAvgAcc,
                ocrTrainMistake, ocrTrainAcc, ocrTestAcc, ocrTrainStdAcc, ocrTestStdAcc, ocrTrainAvgAcc, ocrTestAvgAcc)
    print("Dump completely!!!\n")
    print("Please check the output.txt")


if __name__ == '__main__':
    main()
