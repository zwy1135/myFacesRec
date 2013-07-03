# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 22:26:39 2013

@author: wy
"""
import numpy as np
class EuclideanDistance():

	def __init__(self):
		self.name="EuclideanDistance"

	def __call__(self, p, q):
		p = np.asarray(p).flatten()
		q = np.asarray(q).flatten()
		return np.sqrt(np.sum(np.power((p-q),2)))