import numpy as np

cdef int knn2 (trainingSet, testInstance, int k):
    distances = []
    # Calculating distance between each row of training data and test data
    for i in range(len(trainingSet)):
        distances.append(np.linalg.norm(testInstance-trainingSet[i,1:]))
    # Sorting them on the basis of distance, and selecting the k first index
    index_knn = np.argsort(distances)[0:k]
    #Getting list of class of the k nearest neighbours
    knn = trainingSet[index_knn][:,0]
    #Converting them into Integers for bincount function
    knn = [int(i) for i in knn]
    a = np.bincount(knn)
    return np.argmax(a) #return the most recurent label in the k nearest neighbours set

def go(train,x_train):
    prediction = np.zeros(len(x_train))
    for i in range(len(prediction)):
        prediction[i] = knn2(train,x_train[i],3)