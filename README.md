# Automated Machine Learning

This repository holds the slides and examples of a class on Automated Machine Learning
as Jupyter notebooks. 

# TOC

## I Introduction

### [1.1 What is Automated Machine Learning?](https://github.com/pprett/aml-class-19/blob/master/part_1/1.1%20What%20is%20AML.ipynb)
### [1.2 Machine Learning 101](https://github.com/pprett/aml-class-19/blob/master/part_1/1.2%20Machine%20Learning%20101.ipynb)

## II Tools & Techniques for Automated Machine Learning

## III Create Value using Automation

# Requirements

## Python

Create a new conda env:

    conda create -n aml python=3.7
    source activate aml

## Jupyter

    conda install -y -c conda-forge jupyterlab
    conda install -y -c conda-forge ipywidgets

## Pydata & dependencies

    conda install -y -c conda-forge matplotlib
    conda install -y -c conda-forge seaborn

    conda install -c anaconda scikit-learn==0.21.2

    pip install git+https://github.com/kitchoi/scikit-optimize@fix-762-sklearn-0.21
    pip install tpot==0.10.2
    
## Optional

    conda install -y --freeze-installed -c conda-forge graphviz
    conda install -y --freeze-installed -c conda-forge python-graphviz

