# Automated Machine Learning

This repository holds the slides and examples of a class on Automated Machine Learning
as Jupyter notebooks. 

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

# TOC

## I Introduction

## II Tools & Techniques for Automated Machine Learning

## III Create Value with Automated Machine Learning
