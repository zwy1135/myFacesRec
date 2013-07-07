# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 21:59:55 2013

@author: wy
"""

import os, sys
import numpy as np
from PIL import Image

def read_image(path):
    X, y = [],[]
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname,subdirname)
            for filename in os.listdir(subject_path):
                try:
                    im = Image.open(os.path.join(subject_path,filename))
                    im = im.convert('L')
                    X.append(np.array(im,dtype=np.uint8))
                    y.append(subdirname)
                except IOError:
				print "I/O error({0}): {1}".format(errno, strerror)
                except:
				print "Unexpected error:", sys.exc_info()[0]
				raise
    return [np.array(X), y]
    
