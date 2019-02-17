# rdsa
(re)studying data structures and algorithms

# What is this repo for
Preparation for coding interviews with concentration on data structures and algorithms.

## How does this repo work
This repo uses jupyter notebook. The contents include a good mix of coursera lectures and coding quizzes from the Internet (mainly leetcode and geeksforgeeks). 

If you want to follow along the contents on reading and videos as well, make sure you sign up at [Coursera](coursera.com).

All algorithm quizzes are solved in python. Why? Because it was the simpleset choice for usage with jupyter notebook & I wanted to learn python. 

## Viewing from Github
Github supports reading jupyter notebook on web, but image files on the web can only be read on a local notebook launch. If you want to view the images (mostly PPT slides), please download a clone and launch the notebook.

## Contents 
* [Week 1: Getting a bit of taste](https://github.com/9oelM/rdsa/blob/master/1-algorithmic-toolbox/week-1-getting-a-bit-of-taste.ipynb)
* [Week 2: Algorithmic warm up](https://github.com/9oelM/rdsa/blob/master/1-algorithmic-toolbox/week-2-algorithmic-warm-up.ipynb)

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
