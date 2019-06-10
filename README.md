# rdsa
(re)studying data structures and algorithms

# What is this repo for
Preparation for coding interviews with concentration on data structures and algorithms.

## How does this repo work
This repo uses jupyter notebook. The contents include a good mix of coursera/edx lectures and coding quizzes from the Internet.

## Viewing from Github
Github supports reading jupyter notebook on web, but image files on the web can only be read on a local notebook launch. 
If you want to view the images (mostly PPT slides), download a clone and launch the notebook.

## Contents 
### [Algorithmic toolbox](https://www.coursera.org/learn/algorithmic-toolbox?specialization=data-structures-algorithms)
* [Week 1: Programming Challenges](https://github.com/9oelM/rdsa/tree/master/1-algorithmic-toolbox/week-1-programming-challenges)
* [Week 2: Algorithmic warm up](https://github.com/9oelM/rdsa/tree/master/1-algorithmic-toolbox/week-2-algorithmic-warm-up)
* [Week 3: Greedy algorithms](https://github.com/9oelM/rdsa/tree/master/1-algorithmic-toolbox/week-3-greedy-algorithms)
* [Week 4: Divide and Conquer](https://github.com/9oelM/rdsa/tree/master/1-algorithmic-toolbox/week-4-divide-and-conquer)
* [Week 5: Dynamic programming 1](https://github.com/9oelM/rdsa/tree/master/1-algorithmic-toolbox/week-5-dynamic-programming-1)
* [Week 6: Dynamic programming 2](https://github.com/9oelM/rdsa/tree/master/1-algorithmic-toolbox/week-6-dynamic-programming-2)

### [Data structures: an active learning approach](https://stepik.org/course/579/syllabus)
* [1. Time complexity](https://github.com/9oelM/rdsa/blob/master/2-Data-Structures-An-Active-Learning-Approach/1-time-complexity.ipynb)
* [2. Computational complexity](https://github.com/9oelM/rdsa/blob/master/2-Data-Structures-An-Active-Learning-Approach/2-computational-complexity.ipynb)
* [3. Fundamentals of cpp](https://github.com/9oelM/rdsa/blob/master/2-Data-Structures-An-Active-Learning-Approach/3-fundamentals-of-cpp.ipynb)

# Getting started on your computer
* clone this repo
```bash
git clone https://github.com/9oelM/rdsa.git

cd rdsa
```

* [make sure you are up to date beforehand](https://askubuntu.com/questions/94102/what-is-the-difference-between-apt-get-update-and-upgrade)
```bash
sudo apt-get update 

sudo apt-get upgrade 
```

* install the packages needed
```bash
pip3 install -r requirements.txt
```

* start the notebook
```bash
jupyter notebook
```

# Nice help & resources
* [Jupyter docs](https://jupyter.readthedocs.io/en/latest/index.html#)
* [Jupyter notebook docs](https://jupyter-notebook.readthedocs.io/en/latest/index.html)
* [Python time complexity](https://wiki.python.org/moin/TimeComplexity)

# Running on cloud
```bash
jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser
```

# Troubleshooting for Jupyter notebook installation 
First, try basic things:

```bash
sudo apt-get update

sudo apt-get -y install python3-pip
```

or..
```bash
sudo pip3 install --upgrade pip

sudo pip3 install --upgrade setuptools
```
For more, see [this issue](https://github.com/jupyter/notebook/issues/2605)
