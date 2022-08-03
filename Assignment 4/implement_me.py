# Implementation of B+-tree functionality.

from index import *
import math


class ImplementMe:

  @staticmethod
  def InsertIntoIndex( index, key ):
    '''
    Returns a B+-tree obtained by inserting a key into a pre-existing
    B+-tree index if the key is not already there. If it already exists,
    the return value is equivalent to the original, input tree.
    
    Complexity: Guaranteed to be asymptotically linear in the height of the tree
    Because the tree is balanced, it is also asymptotically logarithmic in the
    number of keys that already exist in the index.
    '''
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


  @staticmethod
  def LookupKeyInIndex( index, key ):
    '''
    Returns a boolean that indicates whether a given key
    is found among the leaves of a B+-tree index.
  
    Complexity: Guaranteed not to touch more nodes than the
    height of the tree
    '''
    return (ImplementMe.findNode(index.root, key)).keys.keys.count(key) != 0


  @staticmethod
  def RangeSearchInIndex( index, lower_bound, upper_bound ):
    '''
    Returns a list of keys in a B+-tree index within the half-open
    interval [lower_bound, upper_bound)
  
    Complexity: Guaranteed not to touch more nodes than the height
    of the tree and the number of leaves overlapping the interval.
    '''
    node = ImplementMe.findNode(index.root, lower_bound)
    start_index = None

    if ((ImplementMe.LookupKeyInIndex(index, lower_bound)) 
      and lower_bound == upper_bound):
      return [lower_bound]

    for index, value in enumerate(node.keys.keys):
      if value >= lower_bound:
        start_index = index
        break
    
    if start_index == None or node.keys.keys[start_index] >= upper_bound:
      return []

    key = node.keys.keys[start_index]
    key_list = ImplementMe.getRange(upper_bound, node, start_index, key)      
    key_list = list(filter(None, key_list))
    return key_list


  def getRange(upper_bound, node, start_index, key):
    '''
    Purpose:    Determine keys in the index within specified range
    Parameters: upper_bound - the upper range
                node - the node to be checked
                start_index - the index of the node
                key - the keys of the node
    Return:     key_range - a list of keys in the specified range
    '''
    key_range = [key]
    while key < upper_bound:
      if start_index == 0:
        start_index += 1
        key = node.keys.keys[1]
        if key is None:
          key = node.keys.keys[0]
          continue
      else:
        node = node.pointers.pointers[2]
        if node is None:
          return key_range
        start_index = 0
        key = node.keys.keys[0]
      ImplementMe.addKey(key, upper_bound, key_range)
    return key_range


  def addKey(key, upper_bound, key_range):
    '''
    Purpose:    Adds a key to the list of keys if it's
                within range
    Parameters: key - the key to be added
                upper_bound - the maximum range that the key can be in
                key_range - a list of keys that are within the bounded range
    '''
    if key < upper_bound:
      key_range.append(key)

  def isLeafNode( node ):
    '''
    Purpose:    Checks if a node is a leaf
    Parameters: node - the current node to be checked
    Returns:    True - if node is a not a leaf
                False - if node is a leaf
    '''
    return node.pointers.pointers[0] is not None


  def isNodeFull( node ):
    '''
    Purpose:    Checks if a node is full
    Parameters: node - the current node to be checked
    Returns:    True - if node is full
                False - if node is not full
    '''
    return node.keys.keys.count(None) == 0
  

  def sortNode(list):
    '''
    Purpose:    Sort the values in the node
    Parameters: list - a list of values in the node
    Returns:    a sorted list of values
    '''
    return sorted(list, key=lambda x: (x is None, x))


  def newRoot(left_point, mid_point, key):
    '''
    Purpose:    creates a new root
    Parameters: left_point - where to point the leftmost pointer
                mid_point - where to point the middle pointer
                key - the nodes key
    Returns:    the new Node() root           
    '''
    return Node(keys=KeySet([key, None]), 
      pointers=PointerSet([left_point, mid_point, None]))


  def splitIndex():
    '''
    Purpose:    split the index of the node by taking the 
                ceiling of a division by 2.
    Parameters: N/A
    Returns:    the index number to split the node at
    '''
    return math.ceil(Index.NUM_KEYS/2)


  def getParent(cur_node, child):
    '''
    Purpose:    Get the parent node information
    Parameters: cur_node - current node to check
                child - child of the cur_node
    Returns:    parent node information
    '''
    for p in cur_node.pointers.pointers:
      if p is None:
        continue
      elif p == child:
        return cur_node

    for index, key in enumerate(cur_node.keys.keys):
      if (key is None or key > child.keys.keys[0]):
        cur_node = cur_node.pointers.pointers[index]
        return ImplementMe.getParent(cur_node, child)

    return ImplementMe.getParent(cur_node.pointers.pointers[Index.NUM_KEYS], child)


  def findNode(root, key):
    '''
    Purpose:    Finds a node to place a key
    Parameters: root - the root of the B+ tree
                key - the key to find or place in the B+ tree
    Reuturn:    the node where the key must be contained          
    '''
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
    '''
    Purpose:    Create a temporary node when adjusting the B+ tree
    Parameters: node - a node to be made into a temporary node
                key - key of the node
    Returns:    B+ tree with the temporary node
    '''
    temp_nodes = node.keys.keys.copy()
    temp_nodes.append(key)        
    temp_nodes = ImplementMe.sortNode(temp_nodes)
    return Node(), temp_nodes, ImplementMe.splitIndex(), 0

  
  def connectPointers(key_index, node, new_node, new_child):
    '''
    Purpose:    Connect the pointers of newely constructed nodes
    Parameters: key_index - index of the node
                node - pre-existing node
                new_node - the new node to be connected to the B+ tree
                new_child - the new child node 
    '''
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
    '''
    Purpose:    shift keys to add new element
    Parameters: node - the node with keys to shift
                index - the index of the node
                key - the keys to shift
    '''
    for i in range(Index.NUM_KEYS - 1, index, -1): 
      node.keys.keys[i] = node.keys.keys[i - 1]
    node.keys.keys[index] = key
  

  def shiftPointers(node, index, new_child):
    '''
    Purpose:    shift pointers to add new element
    Parameters: node - the node with pointers to shift
                index - the index of the node 
                new_child - the new child to point to
    '''
    for idx in range(Index.FAN_OUT -1, index + 1, -1):
      node.pointers.pointers[idx] = node.pointers.pointers[idx - 1]
    node.pointers.pointers[index + 1] = new_child


  def noOverflow(node, key, child):
    '''
    Purpose:    If theres no insertion overflow,
                insert direclty into the node
    Parameter:  node - the node to insert to
                key - the key to insert
                child - child of the node to be pointed to
    Returns:    index of insertion
    '''
    insert_idx = None
    for index, value in enumerate(node.keys.keys):
      if value == None:
        node.keys.keys[index] = key
        node.pointers.pointers[index+1] = child
      elif value > key:
        insert_idx = index 
        continue
    return insert_idx


  def allocateNode(node, temp_nodes, split_index, new_node, new_index, split):
    '''
    Purpose:    Insert into a node after a split
    Parameters: node - the old node that has been split
                temp_nodes - the temporary nodes used for B+ restructuring
                split_index - the index to split the node
                new_node - the new node created
                new_index - the index of the new node
                split - determines if a split occurred
    Returns:    key of the parent if a split occurred
    '''
    parent_key = None
    for index, value in enumerate(temp_nodes):
      if index < split_index:
        node.keys.keys[index] = value
      elif index == split_index and split == True:
        parent_key = value
        node.keys.keys[index] = None
      else:
        new_node.keys.keys[new_index] = value
        if index < Index.NUM_KEYS:
          node.keys.keys[index] = None
        new_index += 1
    return parent_key


  def splitTree(root, node, new_child, key):
    '''
    Purpose:    Splits keys into the previous node and a new node
    Parameters: root - root of the B+ tree
                node - the original node before being split
                new_child - the new child created
                key - the key of the nodes
    Return:     root - the new root after the split
    '''
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
    '''
    Purpose:    Move the key up the tree
    Parameters: node - the orginal node
                root - the root of the B+ tree
                new_node - the new node for the key
                parent - the parent of the node
    Return      the new root
    '''
    return (ImplementMe.newRoot(node, new_node, parent) if node == root 
    else ImplementMe.splitTree(root, ImplementMe.getParent(root, node), new_node, parent))   


  def splitNode(root, node, key):
    '''
    Purpose:    Splits nodes that need to be inserted too and are full
    Parameters: root - the root of the B+ tree      
                node - the node to be split
                key - the key to insert once the node has been split
    Returns:    the new B+ tree
    '''
    new_node, temp_list, split_idx, new_idx = ImplementMe.createTempNodes(node, key)
      
    ImplementMe.allocateNode(node, temp_list, split_idx, new_node, new_idx, False)

    new_node.pointers.pointers[Index.FAN_OUT-1] = node.pointers.pointers[Index.FAN_OUT-1]
    node.pointers.pointers[Index.FAN_OUT-1] = new_node

    return ImplementMe.moveKey(node, root, new_node, new_node.keys.keys[0])
    
