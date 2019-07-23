import pylab as plt
import numpy as np

from sklearn.base import BaseEstimator
from sklearn.base import RegressorMixin
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


FIGSIZE = (11, 7)


def true_fn(X):
    return np.cos(1.5 * np.pi * X)


def generate_curve_data(n_samples=30, seed=0):
    rng = np.random.RandomState(seed)
    X = np.sort(rng.rand(n_samples))
    y = true_fn(X) + rng.randn(n_samples) * 0.1
    return X, y


def plot_data(X, y, fn=None, title=None, alpha=0.4, s=20, fig=None):
    x_plot = np.linspace(0, 1, 100)
    if fig is None:
        fig = plt.figure(figsize=FIGSIZE)

    gt = plt.plot(x_plot, fn(x_plot), alpha=alpha, label='ground truth')

    plt.scatter(X, y, s=s, alpha=alpha)
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.ylabel('y')
    plt.xlabel('x')
    if title:
        plt.title(title)
    plt.legend()
    return fig


def plot_estimator(est, fig, label="{}"):
    x_plot = np.linspace(0, 1, 100)
    plt.plot(x_plot, est.predict(x_plot[:, np.newaxis]), label=label.format(est))
    plt.legend()


class PolynomialRegression(BaseEstimator, RegressorMixin):
    """A simple implementation of Polynomial Regression with scikit-learn. """
    def __init__(self, degree=1):
        self.degree = degree

    def fit(self, X, y):
        self.polynomial_transformer_ = PolynomialFeatures(degree=self.degree, 
                                                         include_bias=False)
        X_prime = self.polynomial_transformer_.fit_transform(X, y)
        self.linear_regression_ = LinearRegression()
        self.linear_regression_.fit(X_prime, y)
        return self

    def predict(self, X):
        return self.linear_regression_.predict(self.polynomial_transformer_.transform(X))
