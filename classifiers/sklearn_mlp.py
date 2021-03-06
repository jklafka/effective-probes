import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

for i in range(5):
	df = pd.read_csv("../data/train.csv", header=None)
	# print("Using word " + str(i))
	# df = pd.read_csv("../data/glove_word" + str(i) + "_train.csv", header=None)
	X_train = df.iloc[:, :-1] #first n-1 columns are embeddings
	Y_train = df.iloc[:, -1] #last column is class label

	# df = pd.read_csv("../data/glove_word" + str(i) + "_test.csv", header=None)
	df = pd.read_csv("../data/test.csv", header=None)
	X_test = df.iloc[:, :-1] #first n-1 columns are embeddings
	Y_test = df.iloc[:, -1] #last column is class label
	print("The train balance is {}".format(sum(Y_train)/Y_train.shape[0]))
	print("The test balance is {}".format(sum(Y_test)/Y_test.shape[0]))

	# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20)

	# mlp = MLPClassifier(hidden_layer_sizes = (512), \
	#         max_iter = 1000, \
	#         alpha = .001, solver = "sgd")
	# mlp.fit(X_train, Y_train)
	# Y_hat = mlp.predict(X_test)
	# X = pd.read_csv("../data/simple_test.csv", header=None)
	# X[2] = Y_hat
	# X.to_csv("pred.csv")
	# print(mlp.score(X_test, Y_test))

	mlp = MLPClassifier(hidden_layer_sizes = (20, 20, 20), \
	    max_iter = 1000, \
	    alpha = .001, solver = "sgd")

	mlp.fit(X_train, Y_train)
	print(mlp.score(X_test, Y_test))
