"""
    author: wangyuxiang
    date: 2021-3-9
"""

import snap
from matplotlib import pyplot as plt
import numpy as np
from math import log10


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


def Q2(g):
    # 计算每个out-degree对应的结点数
    node_number_to_each_out_degree = dict()
    for n in g.Nodes():
        degree = n.GetOutDeg()
        if node_number_to_each_out_degree.get(degree):
            node_number_to_each_out_degree[degree] += 1
        else:
            node_number_to_each_out_degree.setdefault(degree, 1)
    node_number_to_each_out_degree = sorted(node_number_to_each_out_degree.items(), key=lambda k: k[0], reverse=False)
    x = [d[0] for d in node_number_to_each_out_degree][1:]
    y = [n[1] for n in node_number_to_each_out_degree][1:]
    x_log = list(map(log10, x))
    y_log = list(map(log10, y))
    coefficients = np.polyfit(x_log, y_log, deg=1)
    a, b = coefficients[0], coefficients[1]
    print("Coefficients is: a = %f, b = %f" % (a, b))
    x_min, x_max = x_log[0], 0
    y_min, y_max = (a * x_log[0] + b), 0
    for n in x_log:
        if (n * a + b) <= 0:
            break
        y_max = n * a + b
        x_max = n
    plt.plot([x_min, x_max], [y_min, y_max], c='red')
    plt.plot(x_log, y_log, 'ob')
    plt.show()


def print_top_k(dictionary, k=3):
    items = dict()
    for item in dictionary:
        items[item] = dictionary[item]
    items = sorted(items.items(), key=lambda k: k[1], reverse=True)
    for item in items[:k]:
        print("Node: %d, score: %f" % (item[0], item[1]))
    print()


def Q3(g):
    wcc_number = len(g.GetWccs())
    mxwcc = g.GetMxWcc()
    nodes_number_of_mxwcc = mxwcc.GetNodes()
    edges_number_of_mxwcc = mxwcc.GetEdges()
    PRank = g.GetPageRank()
    NIdHubH, NIdAuthH = g.GetHits()
    print("The number of weakly connected components in the network: %d" % wcc_number)
    print("The number of edges: %d, and the number of nodes: %d, in the largest weakly connected component" %
          (nodes_number_of_mxwcc, edges_number_of_mxwcc))
    print_top_k(PRank)
    print_top_k(NIdHubH)
    print_top_k(NIdAuthH)


def load_simple_network():
    g = snap.TNGraph().New()  # 有向图
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


def load_stackoverflow_java():
    return snap.LoadEdgeList(snap.PNGraph, 'stackoverflow-Java.txt', 0, 1)


def main():
    Q1(load_wiki_vote_data())
    Q2(load_wiki_vote_data())
    Q3(load_stackoverflow_java())


if __name__ == '__main__':
    main()
