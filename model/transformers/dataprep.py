from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class Prep(BaseEstimator, TransformerMixin):
    def __init__(self, newcols, timecol, tz='US/Eastern'):
        self.newcols = newcols
        self.timecol = timecol
        self.tz = tz

    def renamecols(self, X):
        X.columns = self.newcols
        return X

    def time_idx(self, X):
        X[self.timecol] = [pd.Timestamp(t, unit='s', tz=self.tz) for t in X[self.timecol].astype(int)]
        return X.set_index(self.timecol)

    def fit(self, X):
        return self

    def transform(self, X):
        return self.time_idx(self.renamecols(X))