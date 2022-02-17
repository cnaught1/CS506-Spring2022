from .sim import euclidean_dist
import matplotlib.pyplot as plt
import numpy as np

class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def snapshot(self, P, assignments):
        fig, ax = plt.subplots()
        colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
        ax.scatter(self.dataset[:, 0], self.dataset[:, 1], color=colors[assignments].tolist(), s=10, alpha=0.8)
        cir = plt.Circle((self.dataset[P][0], self.dataset[P][1]), self.epsilon, color=colors[assignments].tolist(), s=10, alpha=0.8 )
        ax.add_patch(cir)
        fig.savefig("temp.png")
        plt.close()

    def epsilon_neighborhood(self, P_index):
        neighborhood = []
        for PN in range(len(self.dataset)):
            if P_index != PN and euclidean_dist(self.dataset[PN], self.dataset[P_index]) <= self.epsilon:
                #in the neighborhood
                neighborhood.append(PN)
        return neighborhood
    
    def explore_and_assign_eps_neighborhood(self, P_index, cluster, assignments):
        #to do next class=
        neighborhood = self.epsilon_neighborhood(P_index)

        while neighborhood:
            neighbor_of_P = neighborhood.pop()

            if assignments[neighbor_of_P] != 0:
                #this point has already been assigned
                continue 
            assignments[neighbor_of_P] = cluster

            #self.snapshot(self, assignments)

            next_neighborhood = self.epsilon_neighborhood(neighbor_of_P)
            if len(next_neighborhood) >= self.min_pts:
                #this is a core point
                #Its neighbors should be explored / assigned also
                neighborhood.extend(neighbor_of_P)


        return assignments

    def dbscan(self):

        assignments = [0 for _ in range(len(self.dataset))]
        cluster = 1

        for P_index in range(len(self.dataset)):

            if assignments[P_index] != 0:
                #already part of a cluster
                continue

            if len(self.epsilon_neighborhood(P_index)) >= self.min_pts:
                #core point
                assignments = self.explore_and_assign_eps_neighborhood(P_index, cluster, assignments)

            cluster += 1
        
        return assignments