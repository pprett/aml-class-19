# Automated Machine Learning

This repository holds the slides and examples of a class on Automated Machine Learning
as Jupyter notebooks. 

# TOC

## 1 Introduction

### [1.1 What is Automated Machine Learning?](https://github.com/pprett/aml-class-19/blob/master/part_1/1.1%20What%20is%20AML.ipynb)
### [1.2 Machine Learning 101](https://github.com/pprett/aml-class-19/blob/master/part_1/1.2%20Machine%20Learning%20101.ipynb)

### [1.3 Model Selection and Assessment](https://github.com/pprett/aml-class-19/blob/master/part_1/1.3%20Model%20Selection%20and%20Assessment.ipynb)

### [1.4 Hyper-parameter Tuning](https://github.com/pprett/aml-class-19/blob/master/part_1/1.4%20Hyper-parameter%20Tuning.ipynb)

## II Tools & Techniques for Automated Machine Learning

### [2.1 Machine Learning Pipelines](https://github.com/pprett/aml-class-19/blob/master/part_2/2.1%20Machine%20Learning%20Pipelines.ipynb)

### [2.2 Bayesian Hyper-parameter Optimization](https://github.com/pprett/aml-class-19/blob/master/part_2/2.2%20Bayesian%20Hyper-parameter%20Optimization.ipynb)

### [2.3 Pipeline Optimization](https://github.com/pprett/aml-class-19/blob/master/part_2/2.3%20Pipeline%20Optimization.ipynb)

### [2.4 Advanced Topics](https://github.com/pprett/aml-class-19/blob/master/part_2/2.4%20Advanced%20Topics.ipynb)

## III Create Value using Automation

### [3.1 Democratizing Machine Learning](https://github.com/pprett/aml-class-19/blob/master/part_3/3%20Creating%20Value%20using%20Automation.ipynb)

### [3.2 Model Factories](https://github.com/pprett/aml-class-19/blob/master/part_3/3%20Creating%20Value%20using%20Automation.ipynb)

### [3.3 Continous Learning](https://github.com/pprett/aml-class-19/blob/master/part_3/3%20Creating%20Value%20using%20Automation.ipynb)

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

