# need to write the logic that returns the height
def get_height(heap):
    return 0

# not sure if we need this, we can maybe just have heap class contain
# the data? But its easily refactored if we do that anyways
class node:
    def __init__(self, num = 0):
        self.data = num

class heap:
    # I think all we need here is this right?
    # heap can be instantiated with nothing, or a node
    # maybe instead of root, we can have data? As in self.data
    # and implement l_heap and r_heap, can't imagine actually needing
    # a "root" node here
    def __init__(self, r_node = None):
        self.root = r_node
        self.l_heap = None
        self.r_heap = None

    # if empty, then node becomes root
    # if non-empty, check if node is greater than or less than root
    # if it is, swap them... and then check if to put in left or right
    # sub heap
    def insert(self, node):
        if self.root == None:
            self.root = node
        
        else:
            if self.root.data > node.data:
                temp = self.root
                self.root = node
                self.root.l_heap = temp.l_heap
                self.root.r_heap = temp.r_heap
                node = temp

            if self.l_heap == None:
                self.l_heap = heap(node)
                return

            if self.r_heap == None:
                self.r_heap = heap(node)
                return
                
            if get_height(self.l_heap) >= get_height(self.r_heap):
                self.l_heap.insert(node)
                
            else:
                self.r_heap.insert(node)


##### NEED TO IMPLEMENT A PRINT IN POSTORDER AND PRINT ODD NUMBERS IN PRE ORDER\