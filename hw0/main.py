"""
    author: wangyuxiang
    date: 2021-3-9
"""

import snap


def Q1(g):
    nodes_number = g.GetNodes()
    self_edge_node_number = set()
    directed_edges_number = 0
    undirected_edges_number = set()
    reciprocated_edges_number = 0
    zero_out_degree_node_number = 0
    zero_in_degree_node_number = 0
    over_10_out_degree_node_number = 0
    less_10_in_degree_node_number = 0

    for n in g.Nodes():
        if n.GetOutDeg() == 0:
            zero_out_degree_node_number += 1
        elif n.GetOutDeg() > 10:
            over_10_out_degree_node_number += 1
        if n.GetInDeg() == 0:
            zero_in_degree_node_number += 1
            less_10_in_degree_node_number += 1
        elif n.GetInDeg() < 10:
            less_10_in_degree_node_number += 1

    for e in g.Edges():
        if e.GetSrcNId() == e.GetDstNId():
            self_edge_node_number.add(e.GetDstNId())
        else:
            directed_edges_number += 1
            if (e.GetDstNId(), e.GetSrcNId()) in undirected_edges_number:
                reciprocated_edges_number += 1
            else:
                undirected_edges_number.add((e.GetSrcNId(), e.GetDstNId()))

    print('The number of nodes in the network: %d' % nodes_number)
    print('The number of nodes with a self-edge (self-loop) in the network: %d' % len(self_edge_node_number))
    print('The number of directed edges in the network: %d' % directed_edges_number)
    print('The number of undirected edges in the network: %d' % len(undirected_edges_number))
    print('The number of reciprocated edges in the network: %d' % reciprocated_edges_number)
    print('The number of nodes of zero out-degree: %d' % zero_out_degree_node_number)
    print('The number of nodes of zero in-degree: %d' % zero_in_degree_node_number)
    print('The number of nodes with more than 10 outgoing edges: %d' % over_10_out_degree_node_number)
    print('The number of nodes with less than 10 ingoing edges: %d' % less_10_in_degree_node_number)


def load_simple_network():
    g = snap.TNGraph().New()       # 有向图
    g.AddNode(1)
    g.AddNode(2)
    g.AddNode(3)
    g.AddEdge(1, 2)
    g.AddEdge(2, 1)
    g.AddEdge(1, 3)
    g.AddEdge(1, 1)

    return g


def load_wiki_vote_data():
    return snap.LoadEdgeList(snap.PNGraph, 'Wiki-Vote.txt', 0, 1)


def main():
    Q1(load_wiki_vote_data())


if __name__ == '__main__':
    main()