import numpy as np



class Conv2D():
    def __init__(filters,kernel_size,padding=0,stride=1):
        self.filters = filters
        self.kernel_size = kernel_size
        self.padding = padding
        self.stride = stride
        

    def __call__(self,x):
        forward(x, filters,)
    
    
    @staticmethod
    def im2col(x, kernel_h, kernel_w, stride=1, p=0):
    
        x = np.pad(x, [(0,0),(p,p),(p,p),(0,0)])
        B,H,W,C = x.shape
        BB, CC, HH, WW = x.strides

        out_h = int(((H-kernel_h + 2*p)/stride)+1)
        out_w = int(((W-kernel_w) + 2*p/stride)+1)
        columns = np.zeros((B,out_h,out_w,C,kernel_h,kernel_w))

        for i in range(out_w-3):
            for j in range(out_h-3):
                columns[:,j,i]=x[:,j*stride:(j*stride)+kernel_h,i*stride:(i*stride)+kernel_w,:]

        #col = np.lib.stride_tricks.as_strided(x, (B, out_h, out_w, C, kernel_h, kernel_w), (BB, stride * HH, stride * WW, CC, HH, WW)).astype(float)
        #return col.reshape(np.multiply.reduceat(col.shape, (0, 3)))

        return columns.reshape(np.multiply.reduceat(columns.shape,(0,3)))

       
    def forward(self, X,W,b):

        n_filters, d_filter, h_filter, w_filter = W.shape
        kernel_b,kernel_h,kernel_w, kernel_c = W.shape
        columns = im2col(X, kernel_h, kernel_w, stride=1, p=0)

        out=np.tensordot(X,W)+b
        out = out.reshape(n_filters, h_out, w_out, n_x)
        out = out.transpose(3, 0, 1, 2)

        cache = (X, W, b, self.stride, self.padding, X_col)

        return out,cache
    
    
    def backward(self,dout,cache):
        #X,W,b,stride,padding,X_col=cache
        #n_filter,d_filter,h_filter,w_filter=W.shape
        pass
        
