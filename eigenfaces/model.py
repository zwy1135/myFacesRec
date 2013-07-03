# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 22:24:54 2013

@author: wy
"""

import numpy as np
#from util import asRowMatrix
import cv2
from distance import EuclideanDistance

class EigenfacesModel:
    def __init__(self, X=None, y=None, dist_metric=EuclideanDistance(), num_components=0):
        self.dist_metric = dist_metric
        self.projections = []
        self.W = []
        self.m = []
        if (X is not None) and (y is not None):
            self.compute(X,y)
        
    
    def compute(self,X,y):
        self.m , self.W = cv2.PCACompute(X.flatten())
        self.y = y
        for xi in X:
            self.projections.append(cv2.PCAProject(xi.flatten(),self.m,self.W))
            
    def predict(self,X):
        minDist = np.float('inf')
        minclass = None
        Q = cv2.PCAProject(X.flatten(),self.m,self.W)
        for i in xrange(len(self.projections)):
            dist = self.dist_metric(self.projections[i],Q)
            if dist<minDist:
                minDist = dist
                minclass = self.y[i]
        return minclass
        