# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 22:45:29 2013

@author: wy
"""

import sys
import numpy as np
from util import read_image
from model import EigenfacesModel

if __name__=='__main__':
    path = ''
    if len(sys.argv) != 2:
        print '请输入图片地址'
        path = raw_input()
    else:
        path = sys.argv[1]
    
    [X,y] = read_image(path)
    model = EigenfacesModel(X,y)
    
    count = 0
    total = 50
    for j in xrange(50):
        i = np.random.randint(len(X))
        if y[i]==model.predict(X[i]):
            count+=1
        print 'expected=',y[i],r'/ predicted = ',model.predict(X[i])
    print 'rate=',count/total
        
