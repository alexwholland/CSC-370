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
        rels = relations.relations
        rset = set()
        for r in rels:
            rset.update(r.attributes)

        print(Helpers.decompose(rset, fds))

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
    def decompose(relations, fds):
        violations = Helpers.violations(relations, fds)
        if len(violations) == 0:
           return relations
        else:
            for v in violations:
                """ c = Helpers.closure(fds, v.left_hand_side.union(v.right_hand_side))
                R1 = Helpers.decompose(c, Helpers.project(fds, c))
                R2 = Helpers.decompose(relations.difference(c), Helpers.project(fds, (relations.difference(c)).union(v.left_hand_side)))
                print(R1, "AND", R2) """
                print(v)
