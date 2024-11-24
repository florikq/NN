weight = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
inp = [8.4, 0.24, 1.1]
goal_pred = [10, 5, 1]
alpha = 0.01


def nn(inp, weight):
    output = [0, 0, 0]

    for i in range(len(weight)):
        output[i] += w_sum(inp, weight[i])

    return output


def w_sum(a, b):
    output = 0

    for i in range(len(a)):
        output += a[i] * b[i]

    return output


for iteration in range(3):
    pred = nn(inp, weight)
    error = [0, 0, 0]
    delta = [0, 0, 0]
    weight_delta = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for j in range(len(goal_pred)):
        delta[j] = pred[j] - goal_pred[j]
        error[j] = delta[j] ** 2
        for k in range(len(delta)):
            weight_delta[j][k] += inp[k] * delta[j]

    print("Iteration:  ", iteration)
    print("Prediction: ", pred)
    print("Error: ", error)
    print("Weight: ", weight)
    print("Weight_delta: ", weight_delta, "\n")
    print()

    for i in range(len(weight)):
        for j in range(len(weight[0])):
            weight[i][j] -= weight_delta[i][j] * alpha
