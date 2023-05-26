# import modules
import timeit
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Global variables

# input file
input_file = "../movie-lens-data/ratings.csv"
# output file
output_file = "../output.txt"
# neighborhood of size
neighborhood = 5


# Compute centered cosine similarity matrix
def cosineMatrix(table):
    # set cosine_similarity function to cosTable variables (sklearn)
    cosTable = cosine_similarity(table)
    # return x and y cosine matrix
    return pd.DataFrame(cosTable, index=table.index, columns=table.index)


# Compute the neighborhood set 5
def computeNeighborMatrix(a, b):
    # initialize zero
    zeroMx = np.zeros(a.shape)
    # num of item repeat
    for i in range(a.shape[1]):
        # top reverse
        topN = [np.argsort(b[:, i])[:-1 - neighborhood:-1]]
        # num of user
        for j in range(a.shape[0]):
            # similarity matrix
            simMxTop = b[i, :][tuple(topN)]
            # transpose the similarity matrix
            tranSimMxTop = np.transpose(simMxTop)
            # rating matrix
            ratingMxTop = a[j, :][tuple(topN)]
            # find predict
            zeroMx[j, i] = ratingMxTop @ tranSimMxTop
            zeroMx[j, i] = zeroMx[j, i] / np.sum(np.abs(tranSimMxTop))
    # return matrix (neighbor of size more then 5)
    return zeroMx


# Find users who didn't watch movie
def userNotWatch(table, user):
    # list of all movie by user
    userWIF = table.loc[user, :]
    # movie not seen by the user
    notWatch = userWIF[userWIF == 0].index.tolist()
    # all movie list
    allMv = table.columns.tolist()
    # return use not seen movie list
    return [m for m in allMv if m in notWatch]


# Find 5 recommended movies
def recomandMovie5(table, user, mvOut):
    # return five movies that user not seen that are similar to movies user seen
    return table.loc[user, mvOut].sort_values(ascending=False)[:5]


# file dumping
def dump_out(table):
    with open(output_file, "w") as txt_file:
        # write userId and 5 recommended movies
        for result in table:
            txt_file.write(f'{result[0]} {result[1]} {result[2]} {result[3]} {result[4]} {result[5]}\n')
    return


# main function
def main():
    # Read file
    print("File read in progress...")
    start_time = timeit.default_timer()
    data = pd.read_csv(input_file)
    end_time = timeit.default_timer()
    print('Computation time: ', end_time - start_time)
    print("File read completed!!!")
    # convert data to table and remove missing values
    print("Input file to table and remove missing values...")
    start_time = timeit.default_timer()
    table = pd.pivot_table(data=data, values="rating",
                           index="userId",
                           columns="movieId")
    table.fillna(0.0, inplace=True)
    end_time = timeit.default_timer()
    print('Computation time: ', end_time - start_time)
    print("Compute completed!!!")
    # centred cosine similarity
    print("Compute similarity score...")
    start_time = timeit.default_timer()
    trantable = np.transpose(table)
    cosMx = cosineMatrix(trantable)
    end_time = timeit.default_timer()
    print('Computation time: ', end_time - start_time)
    print("Compute completed!!!")
    # Neighborhood for each movie set to 5
    print("Compute neighborhood for each movie...")
    start_time = timeit.default_timer()
    nmx = computeNeighborMatrix(table.values, cosMx.values)
    end_time = timeit.default_timer()
    print('Computation time: ', end_time - start_time)
    print("Compute completed!!!")
    # Recommend 5 movies user haven't seen
    print("Find 5 recommended movies...\nIts going to take some time (approximately 5 minutes), so please wait...")
    us = 1
    count = 0
    result = []
    start_time = timeit.default_timer()
    predMx = pd.DataFrame(data=nmx, index=table.index,
                          columns=table.columns)
    # find 5 recommended movies for each users
    for i in predMx.index[:]:
        userNot = userNotWatch(table, i)
        mv5 = recomandMovie5(predMx, i, userNot)
        mv5 = mv5.index.tolist()
        count += 1
        print(f'In Progress: {count}    Remaining: {len(predMx.index) - count}', end='\r')
        result.append(mv5)
        i += 1
    end_time = timeit.default_timer()
    print('Computation time: ', end_time - start_time)
    print("Completed finding 5 recommended movies!!!")
    # Dump
    print("Dump in progress...")
    start_time = timeit.default_timer()
    # all users id
    for i in result:
        i.insert(0, us)
        us += 1
    dump_out(result)
    end_time = timeit.default_timer()
    print('Computation time: ', end_time - start_time)
    print("Dump completed!!!")


if __name__ == '__main__':
    main()
