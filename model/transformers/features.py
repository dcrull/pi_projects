import pandas as pd

class Features:
    def __init__(self, scale, window, diff1, diff2):
        self.scale = scale
        self.window = window
        self.diff1 = diff1
        self.diff2 = diff2

    def scale_params(self, X):
        self.mu = X.mean()
        self.std = X.std()

    def get_scale(self, X, y):
        X = (X - self.mu)/self.std
        y = (y - self.mu)/self.std
        return X, y

    def smooth(self, X):
        return X.rolling(self.window).mean()

    def get_diff(self, X, diff_order):
        return X.diff(diff_order)

    def fit(self, X, y=None):
        self.scale_params(X)
        return self

    def transform(self, X, y):
        if self.scale: X, y = self.get_scale(X, y)
        if self.window is not None: X = self.smooth(X)
        if self.diff1 is not None: X = self.get_diff(X, self.diff1)
        if self.diff2 is not None: X = self.get_diff(X, self.diff2)
        return X, y
