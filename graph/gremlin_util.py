from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import Bindings

graph = traversal().withRemote(DriverRemoteConnection('ws://127.0.0.1:8182/gremlin', 'g'))


def add_vertex(graph, label, properties=None):
    """
    add vertex
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :param properties: property dict, like {'p1': 'value1', 'p2': 'value2'}
    :return: vertex, like v[int_id]
    """
    vert = graph.addV(label)
    if properties:
        for key in properties.keys():
            vert.property(key, properties.get(key))
    return vert.next()


def add_edge(graph, label, v_from, v_to, properties=None):
    """
    add edge
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :param v_from: vertex from, like v[from_id]
    :param v_to: vertex to, like v[to_id]
    :param properties: property dict, like {'p1': 'value1', 'p2': 'value2'}
    :return: None
    """
    edge = graph.V(Bindings.of('id', v_from)).addE(label).to(v_to)
    if properties:
        for key in properties.keys():
            edge.property(key, properties.get(key))
    edge.iterate()


def drop_vertex(graph, label=None, properties=None):
    """
    drop all vertex or specific vertex
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: None
    """
    travel = graph.V()
    if label:
        travel = travel.hasLabel(label)
    if properties:
        for p in properties:
            if isinstance(p, dict):
                key = list(p.keys())[0]
                travel = travel.has(key, p.get(key))
            else:
                travel = travel.has(p)
    travel.drop().iterate()


def drop_edge(graph, label=None, properties=None):
    """
    drop all edges or specific edge
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: None
    """
    travel = graph.E()
    if label:
        travel = travel.hasLabel(label)
    if properties:
        for p in properties:
            if isinstance(p, dict):
                key = list(p.keys())[0]
                travel = travel.has(key, p.get(key))
            else:
                travel = travel.has(p)
    travel.drop().iterate()
