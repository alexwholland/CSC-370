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
    def DecompositionSteps(relations, fds):
        fdep = fds.functional_dependencies
        fset = [[] for i in range(len(fdep))]
        i = 0
        for fd in fdep:
            attributes = fd.left_hand_side.union(fd.right_hand_side)
            if i < len(fdep):
                fset[i] = Helpers.closure(fds, attributes)
                i += 1
        violations, count = Helpers.violations(relations, fset)
        # print(violations)
        # print(count)
        if count == 0:
            return count
        return 500

class Helpers:
    @staticmethod
    def closure(fds, dependency):
        fdep = fds.functional_dependencies
        result = set(dependency)
        more = True
        while more:
            more = False
            for fd in fdep:
                if fd.left_hand_side.issubset(result) and not fd.right_hand_side.issubset(result):
                    result.update(fd.right_hand_side)
                    more = True
        return result

    @staticmethod
    def violations(relations, fset):
        count = 0
        rels = relations.relations
        relation = set()
        for r in rels:
            relation.update(r.attributes)
        
        violations = [[] for i in range(len(fset))]
        for i in range(len(fset)):
            if relation.difference(fset[i]) != set():
                violations[i] = fset[i]
                count = count + 1
  
        return violations, count
