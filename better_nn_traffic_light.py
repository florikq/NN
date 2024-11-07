import numpy as np

alpha = 0.1

weight_1_2 = np.ones((3, 4))
weight_2_3 = np.ones((4, 1))

inp = np.array([[1, 1, 0],
                [0, 1, 0],
                [1, 0, 1],
                [0, 0, 1],
                [1, 1, 1]])

goal_pred = np.array([1, 1, 0, 0, 1])

for iteration in range(1400):
    for i in range(len(inp)):
        layer_2 = np.dot(inp[i], weight_1_2)

        pred = np.dot(layer_2, weight_2_3)
        error = (pred[0] - goal_pred[i]) ** 2
        layer_3_delta = pred[0] - goal_pred[i]
        layer_2_delta = np.dot(layer_3_delta, weight_2_3)

        weight_delta_1_2 = np.zeros((3, 4))
        weight_delta_2_3 = np.zeros((4, 1))

        for k in range(len(weight_delta_1_2)):
            for j in range(len(weight_delta_1_2[k])):
                weight_delta_1_2[k][j] = inp[i][k] * layer_2_delta[k].item()

        for k in range(len(weight_delta_2_3)):
            for j in range(len(weight_delta_2_3[k])):
                weight_delta_2_3[k][j] = layer_2[j] * layer_3_delta

        for k in range(len(weight_1_2)):
            for j in range(len(weight_1_2)):
                weight_1_2[k][j] -= weight_delta_1_2[k][j] * alpha

        for j in range(len(weight_2_3)):
            weight_2_3[j] -= weight_delta_2_3[j] * alpha

    print(error)
