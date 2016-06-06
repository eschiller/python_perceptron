import random
import nn_util

class Perceptron:
    parameters = []
    param_weights = []
    outputs = []
    weight_max = 0.0
    param_len = 0
    output_len = 0
    learning_interval = 0.0


    def __init__(self, plen, olen, weight_max=1, learning_interval=.1):
        self.param_len = plen
        self.output_len = olen
        self.weight_max = weight_max
        self.learning_interval = learning_interval
        #calc random weights
        for i in range(0, plen):
            self.param_weights.append(random.uniform(0, weight_max))



    def train(self, train_inputs, train_target):
        total_input = 0.0

        #calculate input
        for i in range(0, len(train_inputs)):
            total_input += train_inputs[i] * self.param_weights[i]

        #sigmoid function to output
        activated_input = nn_util.tobin(total_input)

        #calc error
        error = activated_input - train_target

        #re-weight
        for i in range(0, len(self.param_weights)):
            self.param_weights[i] -= error * self.learning_interval * train_inputs[i]



    def train_reps(self, reps):
        for i in range(1, reps):
            x = random.randint(-20, 20)
            y = random.randint(-20, 20)
            if y > x:
                target = 1
            else:
                target = 0
            tinputs = [x, y]
            self.train(tinputs, target)
            self.print_weights()




    def test(self, test_inputs):
        total_input = 0.0

        #calculate input
        for i in range(0, len(test_inputs)):
            total_input += test_inputs[i] * self.param_weights[i]

        #sigmoid function to output
        activated_input = nn_util.sigmoid(total_input)

        for i in range(0, len(test_inputs)):
            print("input" + str(i) + ": " + str(test_inputs[i]))

        print ("output: " + str(activated_input))



    def print_weights(self):
        index = 0
        for weight in self.param_weights:
            print(str(index) + ": " + str(weight))
            index += 1


