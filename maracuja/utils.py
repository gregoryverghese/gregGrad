import numpy as np

def im2col(x, kernel_h, kernel_w, stride=1, p=0):

    x = np.pad(x, [(0,0),(p,p),(p,p),(0,0)])
    B,H,W,C = x.shape

    out_h = int(((H-kernel_h + 2*p)/stride)+1)
    out_w = int(((W-kernel_w) + 2*p/stride)+1)
    columns = np.zeros((B,out_h,out_w,C,kernel_h,kernel_w))

    for i in range(out_w-3):
        for j in range(out_h-3):
            columns[:,j,i]=x[:,j*stride:(j*stride)+kernel_h,i*stride:(i*stride)+kernel_w,:]

    return columns.reshape(np.multiply.reduceat(columns.shape,(0,3)))
