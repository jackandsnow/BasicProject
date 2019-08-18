from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal

graph = traversal().withRemote(DriverRemoteConnection('ws://127.0.0.1:8182/gremlin', 'g'))


def vertex_to_dict(graph, vertex):
    """
    transfer Vertex's info to dict
    :param graph: graph, type: GraphTraversalSource
    :param vertex: vertex, Vertex(id, label)
    :return: vertex info dict
    """
    properties = graph.V(vertex).valueMap().toList()[0]
    for key in properties.keys():
        properties[key] = properties.get(key)[0]
    return {
        'id': vertex.id,
        'label': vertex.label,
        'properties': properties
    }


def edge_to_dict(graph, edge):
    """
    transfer Edge's info to dict
    :param graph: graph, type: GraphTraversalSource
    :param edge: edge, Edge(id, label, outV, inV)
    :return: edge info dict
    """
    e_id = edge.id.get('@value').get('relationId')
    properties = graph.E(e_id).valueMap().toList()[0]
    return {
        'id': e_id,
        'label': edge.label,
        'properties': properties
    }


def add_vertex(graph, label, properties=None):
    """
    add vertex
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :param properties: property dict, like {'p1': 'value1', 'p2': 'value2'}
    :return: vertex, Vertex(id, label)
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
    :param v_from: long vertex id or Vertex(id, label) of from
    :param v_to: long vertex id or Vertex(id, label) of to
    :param properties: property dict, like {'p1': 'value1', 'p2': 'value2'}
    :return: None
    """
    # edge = graph.V(Bindings.of('id', v_from)).addE(label).to(v_to)
    edge = graph.V(v_from).addE(label).to(v_to)
    if properties:
        for key in properties.keys():
            edge.property(key, properties.get(key))
    edge.next()


def drop_vertex(graph, v_id=None, label=None, properties=None):
    """
    drop all vertex or specific vertex
    :param graph: graph, type: GraphTraversalSource
    :param v_id: long vertex id or Vertex(id, label)
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: None
    """
    travel = graph.V(v_id) if v_id else graph.V()
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


def drop_edge(graph, e_id=None, label=None, properties=None):
    """
    drop all edges or specific edge
    :param graph: graph, type: GraphTraversalSource
    :param e_id: edge id, type str
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: None
    """
    travel = graph.E(e_id) if e_id else graph.E()
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


def query_vertex_id_list(graph, label=None):
    """
    query vertex id list
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :return: long(id) list, like [long_id1, long_id2, long_id3]
    """
    travel = graph.V()
    if label:
        travel = travel.hasLabel(label)
    return travel.id().toList()


def query_edge_id_list(graph, label=None):
    """
    query edge id list
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :return: str(id) list, like ['id1', 'id2', 'id3']
    """
    travel = graph.E()
    if label:
        travel = travel.hasLabel(label)
    temp_id_list = travel.id().toList()
    id_list = list(map(lambda t: t.get('@value').get('relationId'), temp_id_list))
    return id_list


def query_vertex(graph, v_id=None, label=None, properties=None):
    """
    query graph vertex data list
    :param graph: graph, type: GraphTraversalSource
    :param v_id: long vertex id or Vertex(id, label)
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: valueMap list
    """
    travel = graph.V(v_id) if v_id else graph.V()
    if label:
        travel = travel.hasLabel(label)
    if properties:
        for p in properties:
            if isinstance(p, dict):
                key = list(p.keys())[0]
                travel = travel.has(key, p.get(key))
            else:
                travel = travel.has(p)
    return travel.valueMap().toList()


def query_edge(graph, e_id=None, label=None, properties=None):
    """
    query graph data list
    :param graph: graph, type: GraphTraversalSource
    :param e_id: edge id, type str
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: valueMap list
    """
    travel = graph.E(e_id) if e_id else graph.E()
    if label:
        travel = travel.hasLabel(label)
    if properties:
        for p in properties:
            if isinstance(p, dict):
                key = list(p.keys())[0]
                travel = travel.has(key, p.get(key))
            else:
                travel = travel.has(p)
    return travel.valueMap().toList()


def query_first_vertex(graph, label=None, properties=None):
    """
    query first vertex for some conditions
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: vertex, Vertex(id, label)
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
    return travel.next()


def query_first_edge(graph, label=None, properties=None):
    """
    query first edge for some conditions
    :param graph: graph, type: GraphTraversalSource
    :param label: label, type: str
    :param properties: property list, like ['p1', 'p2', {'p3': 'value'}]
    :return: edge, Edge(id, label, outV, intV)
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
    return travel.next()


def query_near_vertex(graph, v_id):
    """
    query near vertex of v_id
    :param graph: graph, type: GraphTraversalSource
    :param v_id: v_id: long vertex id or Vertex(id, label)
    :return: vertex list
    """
    result = []
    out_v = graph.V(v_id).out().toList()
    in_v = graph.V(v_id).in_().toList()
    result.extend(out_v)
    result.extend(in_v)
    return result


def get_all_edge_info(graph):
    """
    get all information of edges
    :param graph: graph, type: GraphTraversalSource
    :return: edge info list,
        like [{'outV': o_id, 'inV': i_id, 'property1': 'value', 'property2': 'value', ...}, {...}, {...}]
    """
    result = []
    edge_id_list = graph.E().id().toList()
    for edge_id in edge_id_list:
        e_id = edge_id.get('@value').get('relationId')
        out_v, in_v = graph.E(e_id).bothV().toList()
        edge_dict = {'outV_id': out_v.id, 'inV_id': in_v.id}
        e_values = graph.E(e_id).valueMap().toList()
        for value in e_values:
            edge_dict.update(value)
        result.append(edge_dict)
    return result
