import numpy as np


class Tensor():
    def __init__(data, _children=(),_func_name=''):
        self.data=data
        self.grad=grad
        self._backward=lambda: None
        self._prev=set(_children)
        self._func_name=_func_name


    def __add__(self, value):
        value if isinstance(value,Tensor) else Tensor(value)
        output=Tensor(self.data+value.data,(self,value),'+')

        def _backward():
            self.grad+=output.grad
            value.grad+=output.grad

        output._backward=_backward
        return output

    def __mul__(self, value):
        value if isinstance(value,Tensor) else Tensor(value)
        output=Tensor(self.data*self.value,(self,value),'*')

        def _backward():
            self.grad+=value.grad*output.grad
            value.grad+=self.data*output.grad
        out._backward=_backward
        return output

    
    def backward(self):
        pass




        
        


    def backward(self):
        self.backward(dy=self.grad)


    def __repr__(self):
        return f"<Tensor {self.data!r}>"





