import numpy as np
import caffe
import csv
import os.path

feature_list = [] 	# contains the features of the samples
label_list = []		# contains the labels of the samples (type 1, type 2, or type 3 wheat kernel seed)
count = 0		# dynamically determine the number of samples

# this section reads the CSV file to get the samples line by line
for line in open("../test_seeds.csv"):
      	x = line[0:-1]                          # remove the carriage return (from list to string)
        x = x.split(',')                        # convert the string to list of strings
        x = np.array(x,dtype=np.float32)        # convert the list of strings to array of numpy
        feat = x[1:]				# get the features by reading the 2nd element up to the last element
        feat = feat[None,:]			# remove the singleton dimension, e.g. from 1x1x7 to simply 1x7
        label = x[0] -1 			# Caffe starts the label at 0 (i.e. type 1, 2, 3 becomes type 0, 1, 2 seeds)
        count = count + 1
        feature_list.append(feat)		# list of features of the test samples
        label_list.append(label)		# list of labels of the test samples

caffe.set_mode_cpu()				# set the CPU as the main computing device

if os.path.isfile("train_output/MLPnet.caffemodel"):						# ensure that there is a trained model in the path
	SOMnet = caffe.Net('deploy.prototxt','train_output/MLPnet.caffemodel',caffe.TEST)	# load the architecture prototxt and the computed model, test phase
	TP = 0
	for i in range(count):
		feature_to_process = feature_list[i]						# load the feature of the sample to be tested
		label_to_process = label_list[i]						# load its corresponding label
		SOMnet.blobs['data'].data[...] = feature_to_process				# 'data' is the blob of the input (see the deploy.prototxt)
		SOMnet.blobs['label'].data[...] = label_to_process				# 'label' is the blob for the label (see deploy.prototxt)
		SOMnet.forward()
		prob_item = SOMnet.blobs['prob'].data						# 'prob' outputs three probabilities, each for type 0, 1, 2
	        prob_item = prob_item.squeeze()							# remove unnecessary singleton dimension
		# print "probabilities: ", prob_item						# uncomment if you want to see the probabilities
		if np.argmax(prob_item)==label_to_process:					# if the max prob or the best guess is also the actual label
			TP = TP + 1;								# True positive (TP) ++
			prob_item = np.append(prob_item,np.argmax(prob_item))			# for displaying purposes (see last line)
			prob_item = np.append(prob_item,label_to_process)			# for displaying purposes (see last line)

		print "[probilities (1x3), predicted, actual: ", prob_item
	Acc = float(TP)/count * 100
	print "Accuracy: ", Acc
