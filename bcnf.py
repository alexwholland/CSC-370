from relation import *
from functional_dependency import *

# You should implement the static function declared
# in the ImplementMe class and submit this (and only this!) file.
# You are welcome to add supporting classes and methods in this file.
counter = 0
class ImplementMe:
    # Returns the number of recursive steps required for BCNF decomposition
    #
    # The input is a set of relations and a set of functional dependencies.
    # The relations have *already* been decomposed.
    # This function determines how many recursive steps were required for that
    # decomposition or -1 if the relations are not a correct decomposition.
    @staticmethod
    def DecompositionSteps(relations, fds):
        rels = relations.relations
        R = set()
        for r in rels:
            R.update(r.attributes)

        O = 0
        print(Helpers.decompose(O, R, fds))

        return 500

class Helpers:
    @staticmethod
    def closure(fds, attributes):
        fdep = fds.functional_dependencies
        result = set(attributes)
        more = True
        while more:
            more = False
            for fd in fdep:
                if fd.left_hand_side.issubset(result) and not fd.right_hand_side.issubset(result):
                    result.update(fd.right_hand_side)
                    more = True

        return result

    @staticmethod
    def violations(relations, fds):
        fdep = fds.functional_dependencies
        fset = [[] for i in range(len(fdep))]

        i = 0
        for fd in fdep:
            attributes = fd.left_hand_side.union(fd.right_hand_side)
            if i < len(fdep):
                fset[i] = Helpers.closure(fds, attributes)
                i += 1
        
        violations = [[] for i in range(len(fset))]
        for i in range(len(fset)):
            if relations.difference(fset[i]) != set():
                violations[i] = fset[i]

        lhs = [FunctionalDependency for i in range(len(violations))]
        i = 0
        for fd, v in zip(fdep, violations):
            if v:
                lhs[i] = fd
                i += 1
        lhs = [i for i in lhs if i is not FunctionalDependency]
        
        return lhs

    @staticmethod
    def project(fds, attributes):
        fdep = fds.functional_dependencies
        result = set()
        for fd in fdep:
            if fd.left_hand_side.issubset(attributes) and fd.right_hand_side.issubset(attributes):
                result.add(fd)
        
        return FDSet(result)
    
    @staticmethod
    def decompose(O, R, fds):
        violations = Helpers.violations(R, fds)
        if len(violations) == 0:
            return R
        else:
            c = Helpers.closure(fds, violations[0].left_hand_side.union(violations[0].right_hand_side))
            R1 = c
            F1 = Helpers.project(fds, R1)

            R2 = R.difference(c).union(violations[0].left_hand_side)
            F2 = Helpers.project(fds, R2)
            print("R1: ", R1, "F1: ", F1, end='')
            print("R2: ", R2, "F2: ", F2)   
            #return Helpers.decompose(O, R1, F1).union(Helpers.decompose(O, R2, F2))
