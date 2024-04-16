import networkx as nx
import csv

def measures(graph : nx.Graph):
    degree = dict(graph.degree())
    vertices = len(graph.nodes())
    s = 0

    for x in degree.values():
        s += x
    
    con_com     = nx.connected_components(graph)
    num_con_com = len(list(con_com))
    sum_con_com = 0

    for C in (graph.subgraph(c).copy() for c in nx.connected_components(graph)):
        sum_con_com += nx.average_shortest_path_length(C)
    
    a_dist = sum_con_com/num_con_com

    return s/vertices, nx.average_clustering(graph), a_dist
    
if __name__ == '__main__':
    networks = ['CSBC', 'twitch', 'barabasi', 'erdos', 'watts']
    
    with open('results/results.csv', 'w', newline='') as file:
        pass

    with open('results/results.csv', 'a', newline='') as file:
        arq = csv.writer(file)
        arq.writerow(["n_vertices", "n_arestas", "grau_medio", "coeficiente_clustering_medio", "distancia_media, network, parametro"])
            
        for x in range(0, 5):
            print(networks[x])

            n = 1000
            p = 0.1
            
            if x < 2:
                graph = nx.read_gml("graphs/reais/" + str(networks[x]) + ".gml")
                a_degree, a_coef_clust, a_dist = measures(graph)
                
                arq.writerow([len(graph.nodes()), len(graph.edges), a_degree, a_coef_clust, a_dist, str(networks[x]), 'NULL'])
            elif x == 2:
                for y in range(1, 10):
                    graph = nx.read_gml("graphs/" + str(networks[x]) + "/" + str(networks[x]) + "_n=" + str(n) + ".gml")
                    a_degree, a_coef_clust, a_dist = measures(graph)

                    arq.writerow([len(graph.nodes()), len(graph.edges), a_degree, a_coef_clust, a_dist, str(networks[x]), n])

                    n += 1000
            else: 
                for y in range(1, 10):
                    graph = nx.read_gml("graphs/" + str(networks[x]) + "/" + str(networks[x]) + "_p=" + str(p) + ".gml")
                    a_degree, a_coef_clust, a_dist = measures(graph)

                    arq.writerow([len(graph.nodes()), len(graph.edges), a_degree, a_coef_clust, a_dist, str(networks[x]), p])

                    p += 0.1
                    p = round(p, 2)