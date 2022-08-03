# Implementation of B+-tree functionality.

from index import *
import math

# You should implement all of the static functions declared
# in the ImplementMe class and submit this (and only this!) file.
class ImplementMe:

  # Returns a B+-tree obtained by inserting a key into a pre-existing
  # B+-tree index if the key is not already there. If it already exists,
  # the return value is equivalent to the original, input tree.
  #
  # Complexity: Guaranteed to be asymptotically linear in the height of the tree
  # Because the tree is balanced, it is also asymptotically logarithmic in the
  # number of keys that already exist in the index.
  @staticmethod
  def InsertIntoIndex( index, key ):
    # Return original tree if already exists
    if (ImplementMe.LookupKeyInIndex(index, key)):
      return index

    # Find where to insert key
    cur_node = ImplementMe.findNode(index.root, key)
    
    # Insert into leaf
    if ImplementMe.isNodeFull(cur_node):
      # Overflow 
      root = ImplementMe.splitNode(index.root, cur_node, key)   
      return Index(root)

    else:
      # No Overflow
      for i, value in enumerate(cur_node.keys.keys):
        if value == None:
          cur_node.keys.keys[i] = key
          break
      cur_node.keys.keys = ImplementMe.sortNode(cur_node.keys.keys)
    
    return index


  # Returns a boolean that indicates whether a given key
  # is found among the leaves of a B+-tree index.
  #
  # Complexity: Guaranteed not to touch more nodes than the
  # height of the tree
  @staticmethod
  def LookupKeyInIndex( index, key ):
    return (ImplementMe.findNode(index.root, key)).keys.keys.count(key) != 0


  # Returns a list of keys in a B+-tree index within the half-open
  # interval [lower_bound, upper_bound)
  #
  # Complexity: Guaranteed not to touch more nodes than the height
  # of the tree and the number of leaves overlapping the interval.
  @staticmethod
  def RangeSearchInIndex( index, lower_bound, upper_bound ):
    return []


  # Helper Functions:
  def isLeafNode( node ):
    return node.pointers.pointers[0] is not None


  def isNodeFull( node ):
    return node.keys.keys.count(None) == 0
  

  def sortNode(list):
    return sorted(list, key=lambda x: (x is None, x))


  def newRoot(lc, rc, key):
    return Node(keys=KeySet([key, None]), pointers=PointerSet([lc, rc, None]))

  def splitIndex():
    return math.ceil(Index.NUM_KEYS/2)


  def getParentRec(cur_node, child):
    # Basecase
    for p in cur_node.pointers.pointers:
      if p is None:
        continue
      elif p == child:
        return cur_node

    for index, key in enumerate(cur_node.keys.keys):
      if (key is None or key > child.keys.keys[0]):
        cur_node = cur_node.pointers.pointers[index]
        return ImplementMe.getParentRec(cur_node, child)

    return ImplementMe.getParentRec(cur_node.pointers.pointers[Index.NUM_KEYS], child)



  # returns node that key should be added to or key is inside.
  def findNode(root, key):
    cur_node = root 
    while(ImplementMe.isLeafNode(cur_node)):
      for index, value in enumerate(cur_node.keys.keys):
        if (value is None or value > key):
          cur_node = cur_node.pointers.pointers[index]
          break           
        elif (index == cur_node.get_num_keys() - 1):
          cur_node = cur_node.pointers.pointers[index + 1]
          break
    return cur_node


  def createTempNodes(node, key):
    temp_nodes = node.keys.keys.copy()
    temp_nodes.append(key)        
    temp_nodes = ImplementMe.sortNode(temp_nodes)

    return Node(), temp_nodes, ImplementMe.splitIndex(), 0

  
  def connectPointers(key_index, node, new_node, new_child):
    if key_index == 0:
      new_node.pointers.pointers[0] = node.pointers.pointers[1]
      new_node.pointers.pointers[1] = node.pointers.pointers[2]
      node.pointers.pointers[1] = new_child
    elif key_index == 1:
      new_node.pointers.pointers[0] = new_child
      new_node.pointers.pointers[1] = node.pointers.pointers[2]
    else:
      new_node.pointers.pointers[0] = node.pointers.pointers[2]
      new_node.pointers.pointers[1] = new_child
    node.pointers.pointers[2] = None
    

  def shiftKeys(node, index, key):
    for i in range(Index.NUM_KEYS - 1, index, -1): 
      node.keys.keys[i] = node.keys.keys[i - 1]
    node.keys.keys[index] = key
  
  def shiftPointers(node, index, new_child):
    for idx in range(Index.FAN_OUT -1, index + 1, -1):
      node.pointers.pointers[idx] = node.pointers.pointers[idx - 1]
    node.pointers.pointers[index + 1] = new_child

  def noOverflow(node, key, child):
    insert_idx = None
    for index, value in enumerate(node.keys.keys):
      if value == None:
        node.keys.keys[index] = key
        node.pointers.pointers[index+1] = child
      elif value > key:
        insert_idx = index 
        continue
    return insert_idx

  def allocateNode(node, temp_nodes, split_idx, new_node, new_index, split):
    parent_key = None
    for index, value in enumerate(temp_nodes):
      if index < split_idx:
        node.keys.keys[index] = value
      elif index == split_idx and split == True:
        parent_key = value
        node.keys.keys[index] = None
      else:
        new_node.keys.keys[new_index] = value
        if index < Index.NUM_KEYS:
          node.keys.keys[index] = None
        new_index += 1
    return parent_key


  def internalSplit(root, node, new_child, key):
    # splits keys into node and new_node
    if ImplementMe.isNodeFull(node):
      new_node, temp_list, split_idx, new_idx = ImplementMe.createTempNodes(node, key)
      new_key_idx = temp_list.index(key)
      parent_key = ImplementMe.allocateNode(node, temp_list, split_idx, new_node, new_idx, True)
      ImplementMe.connectPointers(new_key_idx, node, new_node, new_child)
      return ImplementMe.moveKey(node, root, new_node, parent_key)
    else:
      insert_idx = ImplementMe.noOverflow(node, key, new_child) 
      ImplementMe.shiftKeys(node, insert_idx, key)
      ImplementMe.shiftPointers(node, insert_idx, new_child)

    return root 


  def moveKey(node, root, new_node, parent): 
    return (ImplementMe.newRoot(node, new_node, parent) if node == root 
    else ImplementMe.internalSplit(root, ImplementMe.getParentRec(root, node), new_node, parent))   

  # Splits node and returns updated tree. Works for all overflow cases
  def splitNode(root, node, key):
    new_node, temp_list, split_idx, new_idx = ImplementMe.createTempNodes(node, key)
      
    ImplementMe.allocateNode(node, temp_list, split_idx, new_node, new_idx, False)

    new_node.pointers.pointers[Index.FAN_OUT-1] = node.pointers.pointers[Index.FAN_OUT-1]
    node.pointers.pointers[Index.FAN_OUT-1] = new_node

    return ImplementMe.moveKey(node, root, new_node, new_node.keys.keys[0])
