import itertools
from sklearn.cluster import KMeans
from sklearn import metrics
from kneed import KneeLocator


class Model:
    '''
    An ML model implementing K-Means Clustering using sklearn
    '''

    def __init__(self):
        self.model = None
        self.k = 0

    def build_model(self, scaled_df, num_playlists):
        '''
        A function using the Elbow Method to get optimal number of K and using the KMeans
        from sklearn to build a model
        '''
        clusters = list()
        inertia = list()
        models = dict()
        for i in range(2, num_playlists + 1):
            model = KMeans(n_clusters = i)
            model.fit(scaled_df)
            
            models[i] = model

            clusters.append(i)
            inertia.append(model.inertia_)

        self.k = KneeLocator(clusters, inertia, curve = 'convex', direction = 'decreasing')
        

        self.model = models[self.k]

        # return self.model