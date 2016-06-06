#!/usr/bin/python

#initialize
import Perceptron
p = Perceptron.Perceptron(2,1, weight_max=1, learning_interval=.2)
p.print_weights()


print("TRAINING!\n")

p.train_reps(500)


print("TESTING!\n")
tlist = [0, 6]
p.test(tlist)

tlist = [0, -2]
p.test(tlist)

tlist = [4, 1]
p.test(tlist)

tlist = [-2, 0]
p.test(tlist)