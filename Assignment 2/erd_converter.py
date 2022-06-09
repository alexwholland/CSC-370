from erd import *
from table import *

# This function converts an ERD object into a Database object
# The Database object should correspond to a fully correct implementation
# of the ERD, including both data structure and constraints, such that the
# CREATE TABLE statements generated by the Database object will populate an
# empty MySQL database to exactly implement the conceptual design communicated
# by the ERD.
#
# @TODO: Implement me!
def getMultiplicity(es, r_name):
    temp_con = []
    for con in es.connections:
        if con[0] == r_name:
            temp_con.append(con[1])
    return temp_con[0]

def allInList(dep_names, existing_names):
    for name in dep_names:
        if name not in existing_names:
            return False
    return True

def getParents(dependencies, erd):
    for e in erd.entity_sets:
        if len(e.parents) > 0:
            for p in e.parents:
                dependencies[e.name] = [(p, "isA")]
        else:
            dependencies[e.name] = []
    return dependencies

def getForeignKeys(attrs, f_keys, p_keys, dependencies, entity_set, tables, erd):
    for d in dependencies[entity_set.name]:
            temp_keys = []
            for table in tables:
                if table.name == d[0]:
                    temp_keys.append(table)
                    keys = temp_keys[0].primary_key

            f_keys = f_keys.union(set([(tuple(keys), d[0], tuple(keys))]))
            attrs = attrs.union(keys)
          
            if d[1] == "isA" or d[1] in entity_set.supporting_relations:
                p_keys = p_keys.union(keys)
            elif d[1] in entity_set.supporting_relations:
                temp_rel = []
                for rel in erd.relationships:
                    if rel.name == d[1]:
                        temp_rel.append(rel)
                attrs = attrs.union(set(temp_rel[0].attributes))
    return attrs, f_keys, p_keys

def createTable(attrs, f_keys, p_keys, erd, relationship_members, no_table, tables):
    for r in erd.relationships:
        if r.name not in no_table:
            for rel in [r]:
                attrs, p_keys, f_keys = set(rel.attributes), set(rel.primary_key), set()

                for mem in relationship_members[rel.name]:
                    for t in tables:
                        if t.name in mem[0]:
                            for table in [t]:
                                attrs = attrs.union(table.primary_key)
                                f_keys = f_keys.union(set([(tuple(table.primary_key), table.name, tuple(table.primary_key))]))

                                temp_mem = []
                                for mem in relationship_members[rel.name]:
                                    if mem[0] == table.name:
                                        temp_mem.append(mem)
                                if temp_mem[0][1] == Multiplicity.MANY:
                                    p_keys = p_keys.union(table.primary_key)
                tables += [Table(rel.name, attrs, p_keys, f_keys)]
    return tables


def convert_to_table(erd):
    dependencies, relationship_members = {}, {}
    tables = []
    no_table = set()
    
    dependencies = getParents(dependencies, erd)

    for r in erd.relationships:
        es_in_r = []
        for es in erd.entity_sets:
            for con in es.connections:
                if r.name in con[0]:
                    es_in_r.append(es)

        count = 0
        for es in es_in_r:
            if getMultiplicity(es, r.name) == Multiplicity.MANY:
                count += 1

        if len(r.primary_key) == 0 and count == 1:
            es_many, es_one = [], []
            for es in es_in_r:
                if getMultiplicity(es, r.name) == Multiplicity.MANY:
                    es_many = [es.name][0]
            for es in es_in_r:
                if getMultiplicity(es, r.name) == Multiplicity.ONE:
                    es_one.append(es.name)
            for es in es_one:
                dependencies[es_many].append((es, r.name))
            no_table = no_table.union({r.name})
        elif len(es_in_r) == 1:
            count = 0
            for es in erd.entity_sets:
                if r.name in es.supporting_relations:
                    count += 1
            if count != 0:
                for es in erd.entity_sets:
                    if r.name in es.supporting_relations:
                        dependencies[[es][0].name].append((es_in_r[0].name, r.name))
            no_table = no_table.union({r.name})
        
        temp_es = []
        for es in es_in_r:
            temp_es.append((es.name, getMultiplicity(es, r.name)))
            relationship_members[r.name] = temp_es

    entity_sets = list(erd.entity_sets)
    while len(entity_sets) != 0:
        entity_set = None
        for es in entity_sets:
            temp_dependencies, temp_tables = [], []
            for d in dependencies[es.name]:
               temp_dependencies.append(d[0])
            for t in tables:
                temp_tables.append(t.name)

            if allInList(temp_dependencies, temp_tables):
                entity_set = es
                entity_sets.remove(es)
                break

        attrs = set(entity_set.attributes)
        f_keys = set()
        p_keys = set(entity_set.primary_key)

        attrs, f_keys, p_keys = getForeignKeys(attrs, f_keys, p_keys, dependencies, entity_set, tables, erd)       

        tables += [Table(entity_set.name, attrs, p_keys, f_keys)]

    return Database(createTable(attrs, f_keys, p_keys, erd, relationship_members, no_table, tables))