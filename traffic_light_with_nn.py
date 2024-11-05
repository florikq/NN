weight = [0, 0, 0]
inp = [[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]
goal_pred = [0, 0, 1]
alpha = 0.1



def nn(inp, weight):
    output = 0
    for i in range(len(inp)):
        output += weight[i] * inp[i]
    return output


for iteration in range(50):
    for i in range(len(inp)):
        pred = nn(inp[i], weight)
        delta = pred - goal_pred[i]
        error = delta ** 2
        weight_delta = [0, 0, 0]

        for j in range(len(weight_delta)):
            weight_delta[j] = inp[i][j] * delta

        for j in range(len(weight_delta)):
            weight[j] -= weight_delta[j] * alpha



import random
ran = random.randint(0, 2)
print("Traffic light state:", inp[ran])
pred = nn(inp[ran], weight)

if pred > 0.95:
    print("Go")
else:
    print("Stay")
    print(pred)