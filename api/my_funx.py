import numpy as np
import os
def results(data):
    for i in range(len(data)):
        if data[i]<0.7:
            data[i] = 0
        else:
            data[i] = 1
    return data

def predict(r1,r2):
    r = (((r1*0.43) + (r2*0.57))) + 0.28
    r = results(r)
    return(r)

def dixchk(sent):

    op = []
    f = open(os.getcwd() + '//Data//A.txt','r')
    A = f.readlines()
    f = open(os.getcwd() + '//Data//B.txt','r')
    B = f.readlines()
    f = open(os.getcwd() + '//Data//Se.txt','r')
    Se = f.readlines()
    f = open(os.getcwd() + '//Data//Sw.txt','r')
    Sw = f.readlines()
    for j in sent:
        x1 = False
        x2 = False
        x3 = False
        x4 = False
        ip = j.split()
        for i in ip:
            if ((i+'\n') in A):
                x1 = True
            if ((i+'\n') in B):
                x2 = True
            if ((i+'\n') in Se):
                x3 = True
            if ((i+'\n') in Sw):
                x4 = True
        if (x1 or x2 or x3 or x4):
            op.append(1)
        else:
            op.append(0)
    op = np.reshape(np.array(op),(len(op),1)) 
    return op
