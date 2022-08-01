# Implementation of B+-tree functionality.

from index import *

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
    return index


  # Returns a boolean that indicates whether a given key
  # is found among the leaves of a B+-tree index.
  #
  # Complexity: Guaranteed not to touch more nodes than the
  # height of the tree
  @staticmethod
  def LookupKeyInIndex( index, key ):
    return (ImplementMe.getNode(index.root, key)).keys.keys.count(key) != 0


  # Returns a list of keys in a B+-tree index within the half-open
  # interval [lower_bound, upper_bound)
  #
  # Complexity: Guaranteed not to touch more nodes than the height
  # of the tree and the number of leaves overlapping the interval.
  @staticmethod
  def RangeSearchInIndex( index, lower_bound, upper_bound ):
    return []

  
  def isLeaf(node):
    return node.pointers.pointers[0] is not None

  # returns node that key should be added to or key is inside.
  def getNode(root, key):
    cur = root 
    # while the current node points to atleast one other node
    if (ImplementMe.isLeaf(cur)):
      for index, value in enumerate(cur.keys.keys):
        print(value)
        if (value == None or value > key):
          cur = cur.pointers.pointers[index]
          break           
        elif (index == cur.get_num_keys() - 1):
          cur = cur.pointers.pointers[index + 1]
          break
    return cur
