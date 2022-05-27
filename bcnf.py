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
        R = set()
        L = set()
        count = 0
        for r in relations.relations:
            L.update(r.attributes)
            count = count + 1
        R.add(Relation(L))
        R = RelationSet(R)

        violations = ImplementMe.violations(R, fds)
        if len(violations) == 0 and count > 1:
            return -1
        if len(violations) == 0:
            return 0
        T = ImplementMe.decompose(relations, R, fds)
        if T == relations:
            return 1
        else:
            return -1

    @staticmethod
    def closure(fds, attributes):
        result = set(attributes)
        more = True
        while more:
            more = False
            for fd in fds.functional_dependencies:
                if fd.left_hand_side.issubset(result) and not fd.right_hand_side.issubset(result):
                    result.update(fd.right_hand_side)
                    more = True

        return result

    @staticmethod
    def violations(relations, fds):
        violations = []
        for r in relations.relations:
            for fd in fds.functional_dependencies:
                c = ImplementMe.closure(fds, fd.left_hand_side.union(fd.right_hand_side))
                if r.attributes.difference(c) != set() and fd not in violations:
                    violations.append(fd)
        
        return violations

    @staticmethod
    def project(fds, attributes):
        result = set()
        for fd in fds.functional_dependencies:
            if fd.left_hand_side.issubset(attributes) and fd.right_hand_side.issubset(attributes):
                result.add(fd)

        return FDSet(result)

    @staticmethod
    def decompose(relations, R, fds):
        violations = ImplementMe.violations(relations, fds)
        c = ImplementMe.closure(fds, violations[0].left_hand_side.union(violations[0].right_hand_side))
    
        R1 = c
        L = set()
        for r in R.relations:
            L = r.attributes
            break
        R2 = L.difference(c).union(violations[0].left_hand_side)

        T = set()
        T.add(Relation(R1))
        T.add(Relation(R2))
        T = RelationSet(T)
            
        return T
