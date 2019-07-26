import warnings
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import tree

from skopt.benchmarks import branin as branin


def plot_branin():
    """Plot the skopt benchmark `branin` with its 3 minima. """
    fig, ax = plt.subplots()

    x1_values = np.linspace(-5, 10, 100)
    x2_values = np.linspace(0, 15, 100)
    x_ax, y_ax = np.meshgrid(x1_values, x2_values)
    vals = np.c_[x_ax.ravel(), y_ax.ravel()]
    fx = np.reshape([branin(val) for val in vals], (100, 100))

    cm = ax.pcolormesh(x_ax, y_ax, fx,
                       norm=LogNorm(vmin=fx.min(), 
                                    vmax=fx.max()))

    minima = np.array([[-np.pi, 12.275], [+np.pi, 2.275], [9.42478, 2.475]])
    ax.plot(minima[:, 0], minima[:, 1], "r.", markersize=14, lw=0, label="Minima")

    cb = fig.colorbar(cm)
    cb.set_label("f(x)")

    ax.legend(loc="best", numpoints=1)

    ax.set_xlabel("$X_0$")
    ax.set_xlim([-5, 10])
    ax.set_ylabel("$X_1$")
    ax.set_ylim([0, 15])
    

def plot_sklearn_tree(dt, feature_names=None):
    """Plots a sklearn.tree.BaseDecisionTree `dt` using graphviz. """
    try:
        import graphviz 
    except ImportError:
        warnings.warn('skipping plot_tree; graphviz not installed.')
        return
    dot_data = tree.export_graphviz(dt, out_file=None, 
        feature_names=feature_names,  
        filled=True, rounded=True,  
        special_characters=True)
    graph = graphviz.Source(dot_data) 
    return graph


class ColumnGroupSelector(BaseEstimator, TransformerMixin):
    """Selects a group of columns from a pandas.DataFrame and returns a numpy array.

    Parameters
    ----------
    columns : list of str, required
        Column names to be selected.
    """
    def __init__(self, columns):
        self.columns = columns

    def fit(self, x, y=None):
        return self

    def transform(self, df):
        dtypes = set(df.dtypes[self.columns].values.tolist())
        if len(dtypes) > 1:
            raise ValueError('{} must select homogenious dtypes but selected {}'.format(self, dtypes))
        return df[self.columns].values