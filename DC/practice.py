import numpy as np

data_size = 10
num_nodes = 5

learning_rate = 0.1
iterations = 1000

data = [np.random.rand(data_size) for i in range(num_nodes)]

print(data)

global_model = np.zeros(data_size)

for i in range(iterations):
    for j in range(num_nodes):
        local_model = data[j]
        local_model -= (local_model - global_model) * learning_rate
        data[j] = local_model
    
    global_model = np.mean(data , axis=0)

print(global_model)
