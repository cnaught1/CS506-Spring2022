from collections import defaultdict
from math import inf
from itertools import compress
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    if points ==[]:
        column_ave=[]
    else:
        column_ave = [None]*len(points[0])
        for i in range(len(points[0])):
            column_ave[i] = sum(item[i] for item in points)/len(points)    
    return column_ave


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    if dataset ==[]:
        centers=[]
    else:
        k = max(assignments)+1
        centers = [None]*k
        for i in range(0,k):
            boolean = list(map(lambda x: x==i, assignments))
            res = list(compress(dataset, boolean))
            centers[i] = point_avg(res)
    return centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    res = 0
    if a==[] or b==[]:
        res = 0
    else:
        for i in range(len(a)):
            res += (a[i] - b[i])**2
    return res**(1/2)

def distance_squared(a, b):
    res = 0
    if a==[] or b==[]:
        res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    data = [None]*k
    for i in range(k):
        data[i]=random.choice(dataset)
    return data

def cost_function(clustering):
    cost =0
    for key in clustering:
        center = point_avg(clustering[key])
        for point in clustering[key]:
            cost = cost + distance(point, center)
    return cost


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    data = [None]*k
    for i in range(k):
        data[i]=random.choice(dataset)
    return data



def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
