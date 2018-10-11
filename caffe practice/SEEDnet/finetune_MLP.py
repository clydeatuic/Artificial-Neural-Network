import numpy as np
import sys
import os
import time
sys.path.insert(0, 'caffe/install/python') 	# UPDATE YOUR CAFFE PATH HERE
import caffe
import csv

caffe.set_mode_cpu()				# set CPU as the main computing unit

feature_list = []				# container for the list of features of the samples
label_list = []					# container for the list of labels of the samples
count = 0					# dynamically monitors the number of samples

for line in open("../train_seeds.csv"):		# load line per line the features and the corresponding labels of the samples
        x = line[0:-1]                          # remove the carriage return (from list to string)
        x = x.split(',')                        # change the string into list of strings
        x = np.array(x,dtype=np.float32)        # change the list of strings to array of numpy#
        feat = x[1:]				# get the features of the sample from second entry up to the last entry
        feat = feat[None,:]			# remove the singleton dimension (e.g. 1x1x7, it becomes 1x7)
        label = x[0] - 1			# get the label of the seeds (type 1,2,3) and change it to caffe labels s.t. it becomes (type 0,1,2,3)
        count = count + 1
        feature_list.append(feat)		# append to the list of features
        label_list.append(label)		# append to the list of labels

# print "Feature list"
# f = np.array(feature_list)
# print f.shape # (147, 1, 7)

# print "Label list"
# l = np.array(label_list)
# print l.shape # (147)

solver = caffe.SGDSolver("solver.prototxt")	# load the solver -- the solver indicates the architecture prototxt (see the solver.prototxt itself)
# solver.net.copy_from("train_output/MLPnet.caffemodel")		# uncomment this IF you have the initial values for the solver -- otherwise, Caffe will randomly initialize your system
EPOCHS = 1000					# the trainer will look at 1000 times on your training set
ave_loss = 0
for epoch in range(EPOCHS):
        for i in range(count):
                feature_to_process = feature_list[i]					# get the ith feature set for processing
                label_to_process = label_list[i]					# get the ith label for processing
                solver.net.blobs['data'].data[...] = feature_to_process			# 'data' is the input blob for the features (see train.prototxt)
                solver.net.blobs['label'].data[...] = label_to_process			# 'label' is the input blob for the label (see train.prototxt)
                solver.step(1)								# show the sample to the model, and perform "learning" -- to be discussed how
                ave_loss = ave_loss + solver.net.blobs['loss'].data			# extract the loss (higher loss means the system is not trained yet)
        ave_loss = ave_loss/(count)							# after performing training for the whole training set, display the average loss
        print "Epoch: ", epoch,  "  loss:", ave_loss					# monitors the loss per epoch -- it should be decreasing
        ave_loss = 0									# reset the monitor for the next epoch

solver.net.save('train_output/MLPnet.caffemodel')					# after training, save the model
