#!/Users/administrator/anaconda/bin/python

import numpy as np

weights = np.array([0.5,0.48,-0.7])
alpha   = 0.1

streetlights = np.array( [[1,0,1],
			  [0,1,1],
                          [0,0,1],
                          [1,1,1],
                          [0,1,1],
                          [1,0,1]])

walk_vs_stop = np.array([0,1,0,1,1,0])

input = streetlights # [1,0,1]
goal_prediction = walk_vs_stop # equals 0... i.e "stop"

for iteration in range(100):
    prediction = input.dot(weights)
    error = np.sum(( prediction - goal_prediction) ** 2)
    delta = prediction - goal_prediction
    weights -= (alpha * (input.T.dot(delta)))
    print("Average Error: " + str(error) + " Prediction:" + str(prediction))


