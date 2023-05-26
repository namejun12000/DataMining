# import modules
import itertools
import timeit

# Global variables

# input file
input_file = "../data/browsing-data.txt"
# output file
output_file = "../output.txt"
# support
support = 100


# file reading
def read_file():
    with open(input_file, "r") as txt_file:
        # list containing each line in input file
        all_lines = txt_file.readlines()
        # split the lines and put them on the list
        baskets = [[i for i in line.split()] for line in all_lines]
    # return list
    return baskets


# file dumping
def dump_output(a, b):
    with open(output_file, "w") as txt_file:
        txt_file.write("OUTPUT A\n")
        # write pair of items and confidence score
        for conf in a:
            txt_file.write(f'{conf[0][0]} {conf[0][1]} {conf[1]}\n')
        txt_file.write("OUTPUT B\n")
        # write triple of items and confidence score
        for conf in b:
            txt_file.write(f'{conf[0][0]} {conf[0][1]} {conf[0][2]} {round(conf[1], 0)}\n')
    return


# A-priori Algorithm
def apriori1(basket):  # PASS 1
    # empty set
    table = {}
    for items in basket:
        for item in items:
            if item in table:
                # item matched then add 1
                table[item] += 1
            else:
                # item not matched then just 1
                table[item] = 1
    # return item and items count if count more then support
    return {key: count for (key, count) in table.items() if count >= support}


def apriori2(pass1, basket, cb):  # PASS 2
    # empty set
    table = {}
    # items covered with pass1
    pass1_1 = pass1.keys()
    # put the item got in pass1 into the table
    for item in itertools.combinations(pass1_1, cb):
        table[item] = 0
    # find candidate itemsets (pair)
    for i in basket:
        for j in itertools.combinations(i, cb):
            if j in table.keys():
                # if item matches then count + 1
                table[j] += 1
            elif j[::-1] in table.keys():
                # if item matches from behind then count + 1
                table[j[::-1]] += 1
            else:
                # if item not matches then just 1
                table[j] = 1
    # return item and items count if count more then support
    return {item: count for (item, count) in table.items() if count >= support}


def apriori3(pass2, basket, cb):  # PASS 3
    # empty set
    table = {}
    # item covered with pass2
    pass2_2 = pass2.keys()
    # put the item got in pass1 into the table
    for item in itertools.combinations(pass2_2, cb):
        table[item] = 0
    # find candidate itemsets (triple)
    for i in basket:
        for j in itertools.combinations(i, cb):
            if j in table.keys():
                # if item matches then count + 1
                table[j] += 1
            elif j[::-1] in table.keys():
                # if item matches from behind then count + 1
                table[j[::-1]] += 1
            else:
                # if item not matches then just 1
                table[j] = 1
    # return item and items count if count more then support
    return {item: count for (item, count) in table.items() if count >= support}


# Compute the Confidence

# pair of confidence
def computeConfidencePair(pass1, pass2):
    # empty confidence set
    confTable = {}
    for i in pass2.keys():
        # X => Y
        confTable[(i[0], i[1])] = pass2[i] / pass1[i[0]]
        # Y => X
        confTable[(i[1], i[0])] = pass2[i] / pass1[i[1]]
    # return pair of confidence table
    return confTable


# triple of confidence
def computeConfidenceTriple(pass2, pass3):
    # empty confidence set
    confTable = {}
    for i in pass3.keys():
        # (X,Y) => Z
        xy = pass2.get((i[0], i[1])) or pass2.get((i[1], i[0]))
        confTable[(i[0], i[1], i[2])] = pass3[i] / xy
        # (X,Z) => Y
        xz = pass2.get((i[0], i[2])) or pass2.get((i[2], i[0]))
        confTable[(i[0], i[2], i[1])] = pass3[i] / xz
        # (Y,Z) => X
        yz = pass2.get((i[1], i[2])) or pass2.get((i[2], i[1]))
        confTable[(i[1], i[2], i[0])] = pass3[i] / yz
    # return triple of cofidence table
    return confTable


# find top 5 with confidence scores and lexicographically order.
def top5(pass0):
    top = sorted(pass0.items(), key=lambda x: x[1], reverse=True)
    # return order by highest 5 confidence scores
    return top[:5]


# main function
def main():
    # File load
    print('File Read in progress...')
    start_time = timeit.default_timer()
    buckets = read_file()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    print('File read completely!!!\n\n')
    # pass 1
    print('Pass 1 in progress...')
    start_time = timeit.default_timer()
    ap1 = apriori1(buckets)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    print('Pass 1 completely!!!\n\n')
    # pass 2
    print('Pass 2 in progress...')
    start_time = timeit.default_timer()
    ap2 = apriori2(ap1, buckets, 2)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    print('Pass 2 completely!!!\n\n')
    # pass 3
    print('Pass 3 in progress...\nIts going to take some time (approximately 5 minutes), so please wait...')
    start_time = timeit.default_timer()
    ap3 = apriori3(ap2, buckets, 3)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    print('Pass 3 completely!!!\n\n')
    # top 5 pair of confidences
    print('Compute the top 5 pair of confidences...')
    start_time = timeit.default_timer()
    pairC = computeConfidencePair(ap1, ap2)
    pairC5 = top5(pairC)
    stop_time = timeit.default_timer()
    print('Computation time: ', stop_time - start_time)
    print('Find the top 5 pair of confidences completely!!!\n\n')
    # top 5 triple of confidences
    print('Compute the top 5 triple of confidences...')
    start_time = timeit.default_timer()
    triC = computeConfidenceTriple(ap2, ap3)
    triC5 = top5(triC)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    print("Compute the top 5 triple of confidences completely!!!\n\n")
    # dump
    print('Dump in progress...')
    start_time = timeit.default_timer()
    dump_output(pairC5, triC5)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    print("Dump completely!!!\n")
    print("Please check the output.txt")


if __name__ == '__main__':
    main()
