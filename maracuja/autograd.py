import numpy as np


class Variable():
    def __init__(data,_func_name=''):
        self.data=data
        self.grad=grad
        self._prev=set()
        self._func_name=_func_name


    def __add__(self, other):
        if not isinstance(other,Variable):
            Variable(other)
        
        output=Variable(self.data+other.data,'+')
        def _backward():
            self.grad+=output.grad
            value.grad+=output.grad

        output._prev.add((self,other))
        return output


    def top_sort():
        def _top_sort():
            visited={}
            visited.add(node)
            if node not in visited:
                for n in node._parents:
                    top_sort(n)
                nodes.append(node)
            top_sort(self)


    def backward():
        t_sort=top_sort(self)
        
        self.grad=1
        for n in reversed(t_sort):
            n._backward()














        



        
        





