# Pipeline-Prep
Resources, materials, and tutorials used to prep someone to use various PSA image processing pipelines

## Table of Contents
- [Pipeline-Prep](#pipeline-prep)
  - [Table of Contents](#table-of-contents)
  - [Tools](#tools)
    - [Choose an IDE](#choose-an-ide)
    - [Virtual Environment](#virtual-environment)
    - [Git](#git)
    - [Github](#github)
  - [Image processing](#image-processing)
  - [Configuration](#configuration)

## Tools

I highly recommend [The Missing Semester of Your CS Education.](https://missing.csail.mit.edu/) It goes in depth about how to use the shell, scripting, built-in code editors like VIM (a bit too dogmatic for me but helpful for quick fixes in the CL). If this feels a bit too much, leave it for some other time or skip around.

### Choose an IDE

What is an [IDE?](https://www.codecademy.com/article/what-is-an-ide)

VS code is the best [duh!](https://code.visualstudio.com/)

But honestly, there are dozens and it really comes down to personal preferences. To keep things simple, choose one and try to stick to it. You can try others once you get a grasp of the more important topics. 

### Virtual Environment

[MiniConda](https://docs.conda.io/en/latest/miniconda.html) - An absolute must for handling complicated image processing and deep learning dependencies.

### Git
What is [Git?](https://www.atlassian.com/git/tutorials/what-is-version-control)

How [we use Git?](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

### Github
Create a github [account](https://github.com/) if you haven't already.

## Image processing
Familiarize yourself with the basics of image processing in Python. We don't just use OpenCV, but their tutorial is well developed and useful for learning some of the basics.

[OpenCV Tutorial](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

## Configuration
We run all the pipelines by using [Hydra.](https://hydra.cc/docs/intro/)