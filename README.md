# Pipeline-Prep
Resources, materials, and tutorials used to prep someone to use various PSA image processing pipelines

## Table of Contents
- [Pipeline-Prep](#pipeline-prep)
  - [Table of Contents](#table-of-contents)
  - [Basic Tools](#basic-tools)
    - [The Shell](#the-shell)
    - [Virual Environments](#virual-environments)
      - [Conda](#conda)
    - [Choose an IDE](#choose-an-ide)
    - [Git](#git)
    - [Github](#github)
  - [Azure](#azure)
  - [Fundamental Concepts](#fundamental-concepts)
    - [Documentation](#documentation)
    - [Hydra Configuration](#hydra-configuration)
    - [Object Oriented Programming](#object-oriented-programming)
  - [Image processing](#image-processing)
  - [Resources](#resources)
  - [Point-and-Click Tools](#point-and-click-tools)


## Basic Tools

### The Shell

I highly recommend [The Missing Semester of Your CS Education.](https://missing.csail.mit.edu/) It goes in depth about how to use the shell, scripting, built-in code editors like VIM (a bit too dogmatic for me but helpful for quick fixes in the CL). If this feels a bit too much, leave it for some other time or skip around.

- What is [the shell](https://www.datacamp.com/blog/what-is-shell)

- [Best practices](https://sharats.me/posts/shell-script-best-practices/)

### Virual Environments

"A virtual environment is a Python tool for dependency management and project isolation. They allow Python site packages (third party libraries) to be installed locally in an isolated directory for a particular project, as opposed to being installed globally (i.e. as part of a system-wide Python).

Virtual environments provide a simple solution to a host of potential problems. In particular, they help you to:

- Resolves dependency issues
- Promotes modularity and reproducibility
- Encourages organization by keeping your global site-packages and directory tidy"

([Matthew Sarmiento, 2019](https://towardsdatascience.com/virtual-environments-104c62d48c54#ee81))

#### [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)

- We use [MiniConda](https://docs.conda.io/en/latest/miniconda.html), an absolute must for handling complicated image processing and deep learning dependencies.

### Choose an IDE

What is an [IDE?](https://www.codecademy.com/article/what-is-an-ide)

[VS code](https://code.visualstudio.com/)

There are dozens of IDEs and it really comes down to personal preferences. To keep things simple, choose one and try to stick to it. You can try others once you get a grasp of the more important topics. 

### Git

What is [Git?](https://www.atlassian.com/git/tutorials/what-is-version-control)

How [we use Git?](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
  A helpful youtube tutorial: (https://youtu.be/RGOj5yH7evk)
  
### Github
Create a github [account](https://github.com/) if you haven't already.

## Azure

We use:
- [blob containers](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) 

- [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/#features)
A point-and-click tool for navigating cloud storage resources and blob containers.

- [SAS tokens](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?source=recommendations&tabs=Containers) 
To move data between the server and cloud blob container resources.

  **CAUTION**: Be familiar with [SAS permissions](https://learn.microsoft.com/en-us/rest/api/storageservices/create-user-delegation-sas#specify-permissions). This is very important for security and for making sure you don't accidently delete or overwrite the wrong type of data.

- [Azcopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10):
A command line tool for moving data between the local server and cloud storage location 

## Fundamental Concepts

### Documentation

- [Why](https://softwareengineering.stackexchange.com/a/121787)
- RealPython [Tutorial](https://realpython.com/documenting-python-code/)
- Python's [PEP (Python enhancement proposal) 8 style guide](https://peps.python.org/pep-0008/) for questoins like: 
  - Should I use " " or ' ' for strings? [(answer)](https://peps.python.org/pep-0008/#string-quotes)

### Hydra Configuration

I consider this a fundamental concept because it plays a major role in how the pipeline is strucutred and operates.

We run all the pipelines by using [Hydra.](https://hydra.cc/docs/intro/) 

### Object Oriented Programming

- RealPython.com [tutorial](https://realpython.com/python3-object-oriented-programming/)

## Image processing

Familiarize yourself with the basics of image processing in Python.

- [OpenCV Tutorial](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
- [SciKit-Image](https://scikit-image.org/docs/stable/auto_examples/)
- [Scipy](https://scipy-lectures.org/advanced/image_processing/)

## Resources

Computer Vision: Algorithms and Applications, 2nd ed. [Richard Szeliski, 2022](https://szeliski.org/Book/)

## Point-and-Click Tools

For inspecting and preprocessing raw images
- [RawTherapee](https://www.rawtherapee.com/)

For inspecting orthomosaics (this website may be blocked on University networks)
- [Agisoft](https://www.agisoft.com/)

Popular GIS software that can be used to create shapefiles of the potting areas.
- [QGIS](https://www.qgis.org/en/site/)
