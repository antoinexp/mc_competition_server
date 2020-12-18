import pandas as pd
import numpy as np
import scipy as sp
from scipy.spatial import ConvexHull


class Scoring(object):
    def __init__(self, dataset, _lambda):
        self.dataset = dataset
        self.coordinates = dataset[["coordinates_x", "coordinates_y"]]._values
        self.costs = dataset["population"]._values
        self.N = len(dataset)
        self._lambda = _lambda

    def get_convex_hull_id(self, state):
        if state.sum() < 3:
            return state.nonzero()[0]
        hull = ConvexHull(self.coordinates[state == 1])
        idx_hull = (state.nonzero()[0])[hull.vertices]
        return idx_hull

    def get_extremal_points(self, state):
        hull_id = self.get_convex_hull_id(state)
        u, v = hull_id[0], hull_id[0]
        diameter = 0.
        for i in range(len(hull_id)):
            for j in range(i+1, len(hull_id)):
                new_diameter = np.linalg.norm(
                    self.coordinates[hull_id[i]]-self.coordinates[hull_id[j]])
                if new_diameter > diameter:
                    diameter = new_diameter
                    u = hull_id[i]
                    v = hull_id[j]
        return u, v, 0.5*diameter

    def score(self, sample):
        state = (self.dataset
                 .join(sample)["include"]
                 .fillna(0)
                 .map(lambda x: 1 if x > 0.5 else 0)
                 ._values
                 )

        # no cities ?
        if state.sum() == 0:
            return 0.

        _, _, f = self.get_extremal_points(state)
        return self.costs[state == 1].sum() - self._lambda*self.N*np.pi*(f**2.)


def runScoring(scoring, path):
    # try:
    df = pd.read_csv(path, index_col="id")
    return (True, scoring.score(df))
    # except e:
    #  return (False, "scoring error", e)


config1 = dict(
    dataset=pd.read_csv("./datasets/dataset1.csv", index_col="id"),
    _lambda=1.0
)

config2 = dict(
    dataset=pd.read_csv("./datasets/dataset2.csv", index_col="id"),
    _lambda=1.25
)

scoring1 = Scoring(**config1)
scoring2 = Scoring(**config2)
