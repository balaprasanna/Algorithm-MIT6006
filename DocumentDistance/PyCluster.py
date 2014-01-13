# -*- coding: utf-8 -*-
__author__ = 'zym'
import DocumentDistance



class Cluster():
    def __init__(self,id=0):
        self.id=id
        self.points=[]
        self.birth=0
        self.gender=''


def dbscan(data,eps,min_pts=1):
    cluster_id=0
    visited={}
    clusters=[]
    for point in data:
        #for each unvisited points in dataset
        if point[0] not in visited:
            visited[point[0]]=True
            neighbors=get_neighbors(point,data,eps)
            if len(neighbors)<=min_pts:
                cluster_id+=1
                c=Cluster(cluster_id)
                c.points.append(point)
                clusters.append(c)
            else:
                cluster_id+=1
                c=Cluster(cluster_id)
                clusters.append(c)
                expand_cluster(point,data,neighbors,visited,c,clusters,eps)
    return clusters

def expand_cluster(point,data,neighbors,visited,c,clusters,eps):
    c.points.append(point)
    for neighbor_point in neighbors:
        if neighbor_point[0] not in visited:
            visited[neighbor_point[0]]=True
            new_neighbors=get_neighbors(neighbor_point,data,eps)
            join_neighbors(neighbors,new_neighbors)
        if not find_in_cluster(neighbor_point,clusters):
            c.points.append(neighbor_point)


def join_neighbors(n1,n2):
    for point in n2:
        if point not in n1:
            n1.append(point)


def find_in_cluster(point,clusters):
    for cluster in clusters:
        if point in cluster.points:
            return True
    return False

def get_neighbors(point_a,data,eps):
    """
    neighbors=[id1,id2,...]
    """
    neighbors=[point_a]
    for point_b in data:
        if point_a[0]!=point_b[0]:
            distance=DocumentDistance.get_distance(point_a[1],point_b[1])
            if point_a[2]!=point_b[2]:
                distance+=0.45
            if distance<=eps:
                neighbors.append(point_b)
    return neighbors

def compute_cluster(cluster):
    birth_dict={}
    points=cluster.points
    cluster.gender=points[0][2]
    for point in points:
        birth=point[3]
        birth_dict[birth]=birth_dict.get(birth,0)+1
    cluster.birth=get_mode(birth_dict)

def get_mode(dict):
    max_key=max(dict,key=dict.get)
    return max_key

def scan_other_points(data,clusters):
    visited={}
    cluster_id=clusters[len(clusters)-1].id
    for point in data:
        gender=point[2]
        birth=point[3]
        for cluster in clusters:
            if gender==cluster.gender and birth==cluster.birth:
                cluster.points.append(point)
                visited[point[0]]=True
                break
        if point[0] not in visited:
            cluster_id+=1
            c=Cluster(cluster_id)
            c.points.append(point)
            compute_cluster(c)
            clusters.append(c)

def scan_similar_names(data):
    '''
    data=[(id,cv,gender,birth,catagory),()...]
    '''
    data_with_cv=[]
    data_without_cv=[]
    for d in data:
        if d[1] is None:
            data_without_cv.append(d)
        else:
            data_with_cv.append(d)
    clusters=dbscan(data_with_cv,0.55)
    for cluster in clusters:
        compute_cluster(cluster)
    scan_other_points(data_without_cv,clusters)
    return clusters

