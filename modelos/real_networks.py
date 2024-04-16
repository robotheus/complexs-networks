import networkx as nx
import csv
import sys 

def extract_edges_from_dataset(diretorio : str) -> list:
    try:
        with open(diretorio) as csv_file:
            file = csv.reader(csv_file, delimiter=',')

            return list(file)
    except:
        print("Informe um diretorio válido dos dados de entrada.")

def create_network(edges_list : list, diretorio : str) -> nx.Graph:
    try:
        graph = nx.Graph()

        for edge in edges_list:
            graph.add_edge(edge[0], edge[1])
        
        nx.write_gml(graph, diretorio)
        
        return graph
    except:
        print("Informe um diretório válido dos dados de saída.")
        
if __name__ == '__main__':
    diretorio_e = str(sys.argv[1])
    diretorio_s = str(sys.argv[2])

    edges = extract_edges_from_dataset(diretorio_e)
    print(edges)
    graph = create_network(edges, diretorio_s)

    print(diretorio_e, len(graph.edges()), len(graph.nodes()))
