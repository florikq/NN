import numpy as np

inp = 5
goal_pred = 0.75
weight_1_2 = 1
weight_2_3 = 1
alpha = 0.01

for i in range(300):
    layer_2 = np.dot(inp, weight_1_2)
    pred = np.dot(layer_2, weight_2_3)

    error = (pred-goal_pred)**2
    layer_3_delta = pred - goal_pred
    layer_2_delta = np.dot(layer_3_delta, weight_2_3)

    weight_delta_1_2 = inp * layer_2_delta
    weight_delta_2_3 = layer_2 * layer_3_delta

    weight_1_2 -= weight_delta_1_2 * alpha
    weight_2_3 -= weight_delta_2_3 * alpha

    print(pred, weight_1_2, weight_2_3)