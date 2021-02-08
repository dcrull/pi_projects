from sklearn.pipeline import Pipeline
from model.transformers.dataprep import Prep
from pathlib import Path
import pandas as pd

DPATH = Path('~/ds/pi_projects/data/piano_thb.csv')

STEPS = [
    ('prep',Prep(newcols= ['time','temp','baro','rel_hum'], timecol='time')),
]

class predictState:
    def __init__(self,
                 dpath,
                 steps):
        self.pipe = Pipeline(steps)
        self.raw = self.load_data(dpath)

    @staticmethod
    def load_data(dpath):
        return pd.read_csv(dpath)

    def process(self, X):
        return self.pipe.fit_transform(X)

def testing():
    obj = predictState(dpath=DPATH, steps=STEPS)
    data = obj.process(obj.raw)
    X = data.iloc[:-10, :]
    y = data.iloc[-10:, :]
    return X,y