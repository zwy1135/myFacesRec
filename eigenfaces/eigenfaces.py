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
    sample_path = ''
    test_path = ''
    if len(sys.argv) != 3:
        print u'请输入样本图片地址（绝对路径）'
        sample_path = raw_input()
        print u'请输入测试图片地址（绝对路径）'
        test_path = raw_input()
    else:
        sample_path = sys.argv[1]
        test_path = sys.argv[2]
    
    [X,y] = read_image(sample_path)
    model = EigenfacesModel(X,y)
    [nX,ny] = read_image(test_path)
    count = 0
    total = len(nX)
    for i in xrange(total):
        if y[i]==model.predict(nX[i]):
            count+=1
        print 'expected=',ny[i],r'/ predicted = ',model.predict(nX[i])
    print 'rate=',count/total
        
