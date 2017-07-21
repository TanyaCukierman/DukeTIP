from __future__ import print_function
import numpy as np

########################################################
# These functions will be used in Phase 3 (skip for now)
########################################################

def findSimilar(iLikeNp, userLikes):
    # Create an And similarity
    similarityAnd = iLikeNp*userLikes # TODO replace 0 with the correct code
    # Create a per user sum (this is the numerator of the jaccard index)
    similarityAndSum = similarityAnd.sum(axis=1) # TODO replace 0 with the correct code
    # Create an Or similarity
    userSimilarityOr = iLikeNp + userLikes # TODO replace 0 with the correct code
    # Create a per user union sum (this is the denominator of the jaccard index)
    similarityOrSum = userSimilarityOr.sum(axis=1) # TODO replace 0 with the correct code

    # Calculate the similarity
    userSimilarity = abs(similarityAnd)/abs(userSimilarityOr) # TODO replace 0 with the correct code to calculate the Jaccard Index for each user

    # Make the most similar user has a new like that the previous user did not have
    # I used a while loop.
    # You can "get rid" of a user that is most similar, but doesn't have any new likes
    # by setting the userSimilarity for them to 0
    # When you get the index, save it in the variable maxIndex
    # TODO Write the loop
    while True:
         maxIndex = userSimilarity.argmax()
         newlikes = userLikes[maxIndex] - iLikeNp
         newCount = len(newlikes[newlikes>0])
         if newCount<=0:
             userSimilarity[maxIndex]=0
         else:
             break


        # set max index = to the index of the user with the highest similarity
        # substract to find out how many movies the new user likes that i dont
        # if more than zero break out of loopp
        # if zero set usersimilarity to zero


        # TODO Print the max similarity number (most times this is something like 0.17

    # Return the index of the user which is the best match
    print(maxIndex)
    print(userSimilarity)
    return maxIndex

def printMovie(id):
    # Print the id of the movie and the name.  This should look something like
    # "    - 430: Duck Soup (1933)" if the id is 430 and the name is Duck Soup (1933)
    print(movieDict[id], "ID: ", id) # TODO replace 0 with the correct code

def processLikes(iLike):
    print("\n\nSince you like:")
    for id in iLike:
        printMovie(id)

    # TODO Print the name of each movie the user reported liking
    # Hint: Use a for loop and the printMovie function.


    # Convert iLike into an array of 0's and 1's which matches the array for other users
    # It should have one column for each movie (just like the userLikes array)
    # Start with all zeros, then fill in a 1 for each movie the user likes
    iLikeNp = np.zeros(maxMovie)

    # TODO replace 0 with the code to make the array of zeros
    # TODO You'll need a few more lines of code to fill in the 1's as needed
    for id in iLike:
        iLikeNp[id] =1
    # Find the most similar user
    user = findSimilar(iLikeNp, userLikes) # TODO replace 0 with the correct code (hint: use one of your functions)
    print("\nYou might like: ")
    # Find the indexes of the values that are ones
    # https://stackoverflow.com/a/17568803/3854385 (Note: You don't want it to be a list, but you do want to flatten it.)
    recLikes = 0 # TODO replace 0 with the needed code

    # For each item the similar user likes that the person didn't already say they liked
    # print the movie name using printMovie (you'll also need a for loop and an if statement)
    # TODO Print the movies

########################################################
# Begin Phase 1
########################################################

# Load Data
# Load the movie names data (u.item) with just columns 0 and 1 (id and name)
# id is np.int, name is S128
movieNames = np.loadtxt('./ml-100k/u.item', dtype = {'names': ("id", "name" ),
'formats':(np.int, 'S128')}, delimiter = '|', usecols = (0, 1))


# TODO replace 0 with the correct cod eto load the movie date

# Create a dictionary with the ids as keys and the names as the values
# Google search for "python merge lists into dictionary"
# Second Result: https://stackoverflow.com/a/26269307/3854385
movieDict = dict(zip(movieNames['id'], movieNames['name'])) # TODO replace 0 with the code to make the dict


# Load the movie Data (u.data) with just columns 0, 1, and 2 (userID, movieID, rating) all are np.int
movieData = np.loadtxt('./ml-100k/u.data', dtype = {'names': ('userID', 'movieID', 'rating'),'formats': (np.int, np.int, np.int)}, delimiter = "\t", usecols = (0, 1, 2))



########################################################
# Begin Phase 2
########################################################

# Compute average rating per movie
# This is non-ideal, pandas, scipy, or graphlib should be used here

# Create a dictionary to hold our temporary ratings
movieRatingTemp = {} # TODO replace 0 with code for an empty dictionary

# TODO For every row in the movie data, add the rating to a list in the dictionary entry
# for that movies ID (don't forget to initialize the dictionary entry)

for row in movieData:
    if row['movieID'] not in movieRatingTemp:
        movieRatingTemp[row['movieID']] = [row['rating']]
    else:
        movieRatingTemp[row['movieID']].append(row['rating'])





# Create an empty dictionary for movieRating and movieRatingCount
movieRating = {} # TODO replace 0 with code for an empty dictionary
movieRatingCount = {} # TODO replace 0 with code for an empty dictionary

# TODO Using numpy place the average rating for each movie in movieRating and the total number of ratings in movieRatingCount
# Note: You will need a for loop to get each dictionary key
for key in movieRatingTemp:
    movieRating[key]=np.mean(movieRatingTemp[key])
    movieRatingCount[key] = len(movieRatingTemp[key])
# Get sorting ratings
# https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
movieRatingS = sorted(movieRating.iteritems(), key=lambda (k,v): (v,k), reverse=True)


# Top 10 Movies
print("Top Ten Movies:")
for i in range(10):
    id = movieRatingS[i][0]
    print(movieDict[id]+" "+str(movieRatingS[i][0])+" "+str(movieRatingS[i][1])+" "+str(movieRatingCount[1]))


# TODO Print the top 10 movies




# It should print the number, title, id, rating and count of reviews for each movie
# ie 2. Someone Else's America (1995) (ID: 1599) Rating: 5.0 Count: 1



# Top 10 Movies with at least 100 ratings
print("\n\nTop Ten movies with at least 100 ratings:")
l = 0
printed = 0
while printed <10:
        ld = movieRatingS[l][0]
        if movieRatingCount[ld] >= 100:
            print(movieDict[ld]+" "+str(movieRatingS[l][0])+" "+str(movieRatingS[l][1])+" "+str(movieRatingCount[ld]))
            printed+=1
        l+=1
# TODO It should print the same thing, but this time all the movies should have over 100 ratings
# The number should be the movie's absolute rank
# ie (16. Close Shave, A (1995) (ID: 408) Rating: 4.49 Count: 112)
# Number 16 is first in this list because it's the first movie with over 100 ratings
#V
   # for l in range(10):

########################################################
# Begin Phase 3
########################################################
'''print(movieData['useID].max()'])
userLike = np.zeros((4,5))
for i in range(0,3):
    userlikes[i,2]=1

iLike = [4,2]
iLikeNp = np.zeros(5)
#dont use ilike, use jaccard index calculations
for id in iLike:
    iLikeNp[id]=1

iLikeNp[3] = 40
print(iLikeNp.argmax())

maxId = iLikeNp.Argmax()
iLikeNp[maxId]=0

list = np.argwhere(userLikes[1, :] ==1)
print(list.flatten())

maxMovie = 5
userLikes = [
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, l, 1, 1, 1],
    [0, 0, 1, 1, 0]
]

iLike = [2,4]
iLikeNp = np.zeros(maxMovie)
for id in iLike:
    iLikeNp[id] = 1

andSum = iLikeNp* userLikes
print(andSum.sum(axis = 1))

print(iLikeNp)'''

# Create a user likes numpy ndarray so we can use Jaccard Similarity
# A user "likes" a movie if they rated it a 4 or 5
# Create a numpy ndarray of zeros with demensions of max user id + 1 and max movie + 1 (because we'll use them as 1 indexed not zero indexed)

# Find the max movie ID + 1
maxMovie = (movieData['movieID'].max())+1 # TODO replace 0 with the correct code
print(maxMovie)

# Find the max user Id + 1
maxUser = (movieData['userID'].max())+1 # TODO replace 0 with the correct code
print(maxUser)

# Create an array of 0s which will fill in with 1s when a user likes a movie
userLikes = np.zeros((maxUser, maxMovie))

# TODO Go through all the rows of the movie data.
# If the user rated a movie as 4 or 5 set userLikes to 1 for that user and movie
# Note: You'll need a for loop and an if statement
for row in movieData:
    if row["rating"]>=4:
        userLikes[row['userID'],row['movieID']] = 1

########################################################
# At this point, go back up to the top and fill in the
# functions up there
########################################################

# First sample user
# User Similiarity: 0.133333333333
iLike = [655, 315, 66, 96, 194, 172]
processLikes(iLike)

# What if it's an exact match? We should return the next closest match
# Second sample case
# User Similiarity: 0.172413793103
iLike = [ 79,  96,  98, 168, 173, 176,194, 318, 357, 427, 603]
processLikes(iLike)

# What if we've seen all the movies they liked?
# Third sample case
# User Similiarity: 0.170731707317
iLike = [79,  96,  98, 168, 173, 176,194, 318, 357, 427, 603, 1]
processLikes(iLike)

# TODO If your code completes the above recommendations properly, you're ready for the last part,
# allow the user to select any number of movies that they like and then give them recommendations.
# Note: I recommend having them select movies by ID since the titles are really long.
# You can just assume they have a list of movies somewhere so they already know what numbers to type in.
# If you'd like to give them options though, that would be a cool bonus project if you finish early.

