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
    '''
    Purpose:    Determines cardinality of entity
    Parameters: es - entity
                r_name - entity name
    Returns:    the multiplicity
    '''
    temp_con = []
    for con in es.connections:
        if con[0] == r_name:
            temp_con.append(con[1])
    return temp_con[0]


def getManyOrOne(name, ESR, esMany, esOne):
    '''
    Purpose:    Get and store any one-many or many-many relationships
    Parameters: name - name of entity
                ESR - entity sets in relation
                esMany - many-many relationships
                esOne - one-many relationships
    returns:    esMany, esOne
    '''
    for es in ESR:
        if getMultiplicity(es, name) == Multiplicity.ONE:
            esOne.append(es.name)
        if getMultiplicity(es, name) == Multiplicity.MANY:
            esMany = [es.name][0]
    return esMany, esOne


def checkMany(ER, name):
    '''
    Purpose:    Check if relationship is many to many
    Parameters: ER - a list of ERD entity sets
    Returns:    a count of the number of many to many relationships
    '''
    count = 0
    for e in ER:
        if getMultiplicity(e, name) == Multiplicity.MANY:
            count += 1
    return count


def getEntity(erd, name):
    '''
    Purpose:    Get the entity set's and store them in a list
    Parameters: The ERD to retreive the entities from
    Returns:    ER - list of entities  
    '''
    ER = []
    for es in erd.entity_sets:
        for con in es.connections:
            if name in con[0]:
                ER.append(es)
    return ER


def inTable(dep_names, existing_names):
    '''
    Purpose:    Ensure that all dependency names are available
    Parameters: dep_name - available dependency names
                existing_names - all existing dependency names
    Returns:    True - if dependency names are in existing_names
                False - otherwise
    '''
    for name in dep_names:
        if name not in existing_names:
            return False
    return True


def createComponentes(attr, primary):
    '''
    Purpose:    Create sets for attributes, foreign keys, primary keys
    Parameters: attr - the attributes
                primary - primary key
    Returns:    set(atty) - a set of attributes
                set() - empty set for foreign keys
                set(primary) - set of primary keys
    '''
    return set(attr), set(), set(primary)


def getParents(dependencies, erd):
    '''
    Purpose:    Get parent dependencies
    Parameters: dependencies - place to store the parent dependencies
                erd - the entity relationship diagram
    Returns:    dependencies - A dictionary of dependencies containing the parents 
    '''
    for e in erd.entity_sets:
        if len(e.parents) > 0:
            for p in e.parents:
                dependencies[e.name] = [(p, "isA")]
        else:
            dependencies[e.name] = []
    return dependencies


def getForeignKeys(f_keys, tables, dependency):
    '''
    Purpose:    Get the foreign keys
    Parameters: f_keys - holds all foreign keys
                tables - tables of attributes
                dependency - erd dependencies
    Returns:    f_keys - foreign keys
                keys - primary keys
    '''
    temp_keys = []
    for table in tables:
        if table.name == dependency[0]:
            temp_keys.append(table)
            keys = temp_keys[0].primary_key

    f_keys = f_keys.union(set([(tuple(keys), dependency[0], tuple(keys))])) 
    return f_keys, keys


def getKeys(attrs, f_keys, p_keys, dep, entity_set, tables, erd):
    '''
    Purpose:    Get the keys in the erd
    Parameters: attrs - erd attributes
                f_keys - foreign keys
                p_keys - primary keys
                dependencies - erd dependencies
                entity_set - the entities of the erd
                tables - erd tables
                erd - the entity relationship diagram
    Returns:    attrs, f_keys, p_keys
    '''
    for d in dep[entity_set.name]:
            f_keys, keys = getForeignKeys(f_keys, tables, d)
            attrs = attrs.union(keys)
          
            if d[1] == "isA" or d[1] in entity_set.supporting_relations:
                p_keys = p_keys.union(keys)
            elif d[1] in entity_set.supporting_relations:
                temp_rel = [rel for rel in erd.relationships if rel.name == d[1]]
                attrs = attrs.union(set(temp_rel[0].attributes))
    
    return attrs, f_keys, p_keys


def createRelationshipTable(rel, relationship_members, tables):
    '''
    Purpose:    Create a table for relationships in the ERD
    Parameters: rel - a specific relations
                relationship_members - all relationships
                tables - Current ERD tables
    returns:    the list of tables
    '''
    attrs, f_keys, p_keys = createComponentes(rel.attributes, rel.primary_key)
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


def createTable(attrs, f_keys, p_keys, erd, relationship_members, no_table, tables):
    '''
    Purpose:    create a table for relationships
    Parameters: attrs - erd attributes
                f_keys - foreign keys
                p_keys - primary keys
                erd - the entity relationship diagram
                relationship_members - dictionary of relationships in erd
                no_table - set of elements that dont require a table
                tables - erd tables
    '''
    for r in erd.relationships:
        if r.name not in no_table:
            for rel in [r]:
                tables = createRelationshipTable(rel, relationship_members, tables)
    return tables


def noDependencies(entity_sets, dependencies, tables):
    '''
    Purpose:    Determine entity sets with no dependencies
    Parameters: entity_sets - set of erd entities
                dependencies - dependencies of the erd
                tables - erd tables
    Returns:    entity_set - single entity set
                entity_sets - list of entity sets
    '''
    for es in entity_sets:        
        temp_dependencies = [d[0] for d in dependencies[es.name]]
        temp_tables = [t.name for t in tables]

        if inTable(temp_dependencies, temp_tables):
            entity_set = es
            entity_sets.remove(es)
            break
        
    return entity_set


def getRelValues(relationship_vals, ESR, name):
    '''
    Purpose:    Get the members of the relationships 
    Parameters: relationship_vals - list of the relationship members
                ESR - entity sets in relationship
                name - name of entity set
    Returns:    list of relationship members 
    '''
    relationship_vals[name] = [(e.name, getMultiplicity(e, name)) for e in ESR]
    return relationship_vals


def oneToMany(erd, dependencies, relationship_members, no_table):
    '''
    Parameters: Add one to many relationship dependencies
    Parameters: erd - entity relationship diagram
                dependencies - erd dependencies 
                relationship_members - dictionary of relationship members
                no_table - set of elements that dont require a table
    Returns:    no_table, relationship_members, dependencie
    '''
    for r in erd.relationships:
        es_in_r = getEntity(erd, r.name)

        if len(r.primary_key) == 0 and checkMany(es_in_r, r.name) == 1:
            
                esMany, esOne = [], []
                esMany, esOne = getManyOrOne(r.name, es_in_r, esMany, esOne)
            
                for es in esOne:
                    dependencies[esMany].append((es, r.name))
                no_table = no_table.union({r.name})
        elif len(es_in_r) == 1:
            for es in erd.entity_sets:
                if r.name in es.supporting_relations:
                    dependencies[[es][0].name].append((es_in_r[0].name, r.name))
            no_table = no_table.union({r.name})
        
        relationship_members = getRelValues(relationship_members, es_in_r, r.name)
    return no_table, relationship_members, dependencies


def convert_to_table(erd):
    '''
    Purpose:    Convert the erd to a table
    Parameters: erd - The entity relationship diagram
    Returns:    the tables of the erd
    '''
    dependencies, relationship_members = {}, {}
    tables = []
    no_table = set()
    dependencies = getParents(dependencies, erd)    
    no_table, relationship_members, dependencies = oneToMany(erd, dependencies, relationship_members, no_table)
    entity_sets = list(erd.entity_sets)
    while len(entity_sets) != 0:
        entity_set = noDependencies(entity_sets, dependencies, tables)
        attrs, f_keys, p_keys = createComponentes(entity_set.attributes, entity_set.primary_key)
        attrs, f_keys, p_keys = getKeys(attrs, f_keys, p_keys, dependencies, entity_set, tables, erd)       
        tables += [Table(entity_set.name, attrs, p_keys, f_keys)]

    return Database(createTable(attrs, f_keys, p_keys, erd, relationship_members, no_table, tables))
