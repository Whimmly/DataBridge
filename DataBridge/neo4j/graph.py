"""
Helper function for wrapping Neo4j driver and
bolt requests.
"""


from .logger import graph_logger


class Graph():
  '''
  Graph class for holding basic graph logic.
  '''

  def __init__(self, driver):
    self.driver = driver
    graph_logger.info('Creating new Neo4j graph')

  def run(self, query, batched=False):
    '''
    Wrapper for executing fucntions on the driver.
    Log all cypher queries, offer batching support.
    '''

    with self.driver.session() as sess:
      if batched is True:
        # If queries are batched, iterate through
        # queries and return concatenated results.
        results = []
        for q in query:
          graph_logger.debug("Cypher: " + q)
          results.append(sess.run(q))
        return results
      else:
        # Return unbatched query.
        graph_logger.debug("Cypher: " + query)
        return sess.run(query)

  def get_entity(self, node):
    '''
    Get an entity.
    '''

    query = "MATCH %s RETURN properties(n), ID(n)" % node
    return self.run(query)

  def get_relationship(self, parent_nd, child_nd, edge):
    '''
    Get a relationship from the graph.
    '''

    query = "MATCH %s-%s->%s RETURN properties(r)" % (parent_nd,
                                                      edge, child_nd)
    return self.run(query)

  def add_entity_property(self, node, key, value):
    '''
    Update an entity on the graph.
    '''

    query = "MATCH %s SET n.%s = '%s' RETURN n" % (node, key, value)
    return self.run(query)

  def add_entity(self, node):
    '''
    Add an entity to the graph.
    '''

    query = "CREATE %s" % node
    return self.run(query)

  def add_relationship(self, parent_nd, child_nd, edge):
    '''
    Add a relationship to the graph.
    '''

    query = "MATCH %s,%s CREATE (p)-%s->(c)" % (parent_nd, child_nd, edge)
    return self.run(query)

  def wipe(self):
    '''
    Wipe all nodes from graph.
    '''

    query = "MATCH (n) DETACH DELETE n"
    graph_logger.info('Wiping all nodes...')
    return self.run(query)

