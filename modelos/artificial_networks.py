import networkx as nx

def create_networks(n, p, k, nb, m):
    for x in range(1,10):
        graph_erdos     = nx.erdos_renyi_graph(n, p)
        graph_watts     = nx.watts_strogatz_graph(n, k, p)
        graph_barabasi  = nx.barabasi_albert_graph(n=nb, m=m)

        nx.write_gml(graph_erdos,    "graphs/erdos/erdos_p=" + str(p) + ".gml")
        nx.write_gml(graph_watts,    "graphs/watts/watts_p=" + str(p) + ".gml")
        nx.write_gml(graph_barabasi, "graphs/barabasi/barabasi_n=" + str(nb) + ".gml")

        p += 0.1
        p = round(p, 2)
        nb += 1000

if __name__ == '__main__':
    n = 1000
    p = 0.1
    k = 6
    nb = 1000
    m = 4

    create_networks(n, p, k, nb, m)