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

    conda install -c anaconda scikit-learn==0.19.2
    conda install --freeze-installed -c conda-forge scikit-optimize

    pip install git+https://github.com/kitchoi/scikit-optimize@fix-762-sklearn-0.21
    pip install tpot
    
## Optional

    conda install -y --freeze-installed -c conda-forge graphviz
    conda install -y --freeze-installed -c conda-forge python-graphviz
    

# TOC


## Part 1: Introduction

### 


## Part 2: Tools and Techniques for Automated Machine Learning

### 2.1 ML Pipelines
### 2.2 Bayesian Hyper-parameter Tuning
### 2.3 Pipeline Optimization

## Part 3: Creating Value using Automated Machine Learning