"""import pickle
file = "batches.meta, data_batch_1, data_batch_2, data_batch_3, data_batch_4, data_batch_5, test_batch"
def unpickle(file):
   
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
"""
Xtr, Ytr, Xte, Yte = load_CIFAR10('cifar_10') # a magic function we provide
# flatten out all images to be one-dimensional
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3) # Xtr_rows becomes 50000 x 3072
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3) # Xte_rows becomes 10000 x 3072
nn = NearestNeighbor() # create a Nearest Neighbor classifier class
nn.train(Xtr_rows, Ytr) # train the classifier on the training images and labels
Yte_predict = nn.predict(Xte_rows) # predict labels on the test images
# and now print the classification accuracy, which is the average number
# of examples that are correctly predicted (i.e. label matches)
print ('accuracy: %f') % ( np.mean(Yte_predict == Yte) )








#import numpy as np
#class NearestNeighbor(object):
 # def _init_(self):
#    pass
#  def train(self, X, y):
 #     self.Xtr = X
 #     self.ytr = y
 # def predict(self, X):
 #  num_test = X.shape[0]
 #  Ypred = np.zeros(num_test, dtype = self.ytr.dtype)
