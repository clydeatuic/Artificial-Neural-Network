# Artificial-Neural-Network
Introduction to Neural Network

### Caffe Setup using Ubuntu 18 Environment
```bash
# Ubuntu Package Requirements
$ sudo apt install python-pip
$ sudo apt install python-pip3

$ sudo apt-get install -y --no-install-recommends libboost-all-dev
$ sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler
$ git clone https://github.com/BVLC/caffe
$ cd caffe
$ cp Makefile.config.example Makefile.config
$ sudo pip install scikit-image protobuf
$ cd python
$ for req in $(cat requirements.txt); do sudo pip install $req; done
$ cd ..
$ sudo vim Makefile.config
  # CPU-only switch (uncomment to build without GPU support).
  CPU_ONLY := 1
  ...
  # Uncomment if you're using OpenCV 3
  OPENCV_VERSION := 3
  ...
  PYTHON_INCLUDE := /usr/include/python2.7 \
          /usr/local/lib/python2.7/dist-packages/numpy/core/include
  ...
  # ANACONDA_HOME := $(HOME)/anaconda2
  ...
  # PYTHON_LIB := $(ANACONDA_HOME)/lib
$ make all
  # if error do this
  $ sudo ln -s /usr/lib/x86_64-linux-gnu/libhdf5_serial.so.10.1.0 /usr/lib/x86_64-linux-gnu/libhdf5.so
  $ sudo ln -s /usr/lib/x86_64-linux-gnu/libhdf5_serial_hl.so.10.0.2 /usr/lib/x86_64-linux-gnu/libhdf5_hl.so
  $ make all
$ make test
$ make runtest
$ make pycaffe
$ sudo vim ~/.bashrc
  #Use your caffe directory
  export PYTHONPATH=$HOME/Desktop/caffe/python:$PYTHONPATH
$ source ~/.bashrc
  #import caffe inside python environment
  $ python
    >>> import caffe
    >>> caffe.__version__

#Download Sample Dataset
$ ~/Desktop/caffe
$ ./data/mnist/get_mnist.sh
$ ./examples/mnist/create_mnist.sh

#Train Sample Model
$ ./examples/mnist/train_lenet.sh
  #if error, modify examples/mnist/lenet_solver.prototxt, replace GPU with CPU, and save it.
  $ vim ~/Desktop/caffe/examples/mnist/lenet_solver.prototxt
    #replace GPU with CPU
  $ ./examples/mnist/train_lenet.sh
  # This will take a while to complete (considering using CPU computing power)

Done!
```

![caffe success](https://github.com/clydeatuic/Artificial-Neural-Network/blob/master/caffe_success.png)


### vim editing guide
```bash
Xmod - [ESC]
i - insert - edit
y - yank - copy
p - place - paste
d - delete - delete
:w - save
:x - save and exit
```
