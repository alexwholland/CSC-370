# Counts the number of steps required to decompose a relation into BCNF.

from fcntl import FD_CLOEXEC
from re import A

from sqlalchemy import false, true
from relation import *
from functional_dependency import *

# You should implement the static function declared
# in the ImplementMe class and submit this (and only this!) file.
# You are welcome to add supporting classes and methods in this file.
class ImplementMe:

    # Returns the number of recursive steps required for BCNF decomposition
    #
    # The input is a set of relations and a set of functional dependencies.
    # The relations have *already* been decomposed.
    # This function determines how many recursive steps were required for that
    # decomposition or -1 if the relations are not a correct decomposition.
    @staticmethod
    def DecompositionSteps( relations, fds ):
        FD = fds.functional_dependencies
        for functional_dependency in FD:
             print(functional_dependency.left_hand_side)
         #   print(functional_dependency.right_hand_side)
        return -1
