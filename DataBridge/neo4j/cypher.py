"""
cypher.py

Helper functions templating common cypher query components.
More or less just string manipulation.
"""


def gen_cypher_nd(var="a", nd_cls=False, nd_props={}, db_name=None):
  '''
  Generate cypher component for referencing a single node (n:_ {_:_,...})
  '''

  # First build query with var name and optional class
  cypher_q = "({0}{1}{2})"
  query_params = [var, ':' + nd_cls if nd_cls else '']

  # Subsitute property specifiers into the query
  if len(nd_props.items()) == 0:
    query_params.append("")
  else:
    query_params.append(" {" + ', '.join("{!s}:{!r}".format(key, val)
                        for (key, val) in nd_props.items()) + "}")

  # Format and return query
  cypher_q = cypher_q.format(*query_params)
  return cypher_q


def gen_cypher_rel(var="r", rel_cls=False, rel_props={}, db_name=None):
  '''
  Generate cypher component for referencing a single relation [r:_ {_:_,...})
  '''

  # First build query with var name and optional class
  cypher_q = "[{0}{1}{2}]"
  query_params = [var, ':' + rel_cls if rel_cls else '']

  # Subsitute property specifiers into the query
  if len(rel_props.items()) == 0:
    query_params.append("")
  else:
    query_params.append(" {" + ', '.join("{!s}:{!r}".format(key, val)
                        for (key, val) in rel_props.items()) + "}")
  # Format and return query
  cypher_q = cypher_q.format(*query_params)
  return cypher_q


def gen_cypher_nd_match(nd_term=False, nd_cls=False, nd_props={},
                        db_name=None):
  '''
  Return cypher component for matching node
  '''

  # If nd_term provided, plop it into nd_props
  if nd_term:
    nd_props['sem_term'] = nd_term

  cypher_q = """
  MATCH {0}
  """
  cypher_q = cypher_q.format(gen_cypher_nd(var='n', nd_cls=nd_cls,
                                           nd_props=nd_props,
                                           db_name=db_name))
  return cypher_q


def gen_cypher_rel_match(par_nd={'nd_cls': False, 'nd_props': {}},
                         child_nd={'nd_cls': False, 'nd_props': {}},
                         b_directed=False, rel_cls=False,
                         rel_props={}, db_name=None):
  '''
  Return cypher component for matching relation
  '''

  par_nd_q = gen_cypher_nd(var="a", nd_cls=par_nd['nd_cls'],
                           nd_props=par_nd['nd_props'], db_name=db_name)
  child_nd_q = gen_cypher_nd(var="b", nd_cls=child_nd['nd_cls'],
                             nd_props=child_nd['nd_props'], db_name=db_name)
  rel_q = gen_cypher_rel(var='r', rel_cls=rel_cls, rel_props=rel_props,
                         db_name=db_name)

  cypher_q = """
  MATCH {0}-{2}-{3}{1}
  """
  cypher_q = cypher_q.format(par_nd_q, child_nd_q, rel_q, '>'
                             if b_directed else '')
  return cypher_q

