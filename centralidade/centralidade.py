import json
import networkx as nx
import matplotlib.pyplot as plt

with open('dataset.json') as file:
    dataset = json.load(file)


def graph_network():
    graph = nx.Graph()
    titles = []
    event = []

    for data in dataset:
        if data["Evento"] == "BRASNAM":
            graph.add_node(data["Pessoa autora"])
            titles.append(data["Titulo"])
            event.append(data["Evento"])
    
    for title in titles:
        matching_authors = [item["Pessoa autora"] for item in dataset if item["Titulo"] == title]
        
        evento = [item["Evento"] for item in dataset if item["Titulo"] == title]
        matching_authors.append(evento[0])

        for author1 in matching_authors:
            for author2 in matching_authors:
                if author1 not in event and author2 not in event and author1 != author2 and not graph.has_edge(author1, author2):
                    graph.add_edge( author1, 
                                    author2, 
                                    title=title, 
                                    classe = matching_authors[len(matching_authors) - 1],
                                    weight = 1)
                elif author1 != author2 and author1 not in event and author2 not in event:
                    p = graph[author1][author2]['weight']
                    graph[author1][author2]['weight'] = p + 1

    return graph


def plot(D : dict, diretorio : str, titulo, color) -> None:
    values = sorted(D.values(), reverse = True)
    values20 = values[:10]
    
    keys20 = [k for k, v in sorted(D.items(), key=lambda item: item[1], reverse=True)[:10]]
    
    plt.bar(range(len(values20)), values20, tick_label=keys20, color=color, width=0.6)
    plt.xlabel("Autor")
    plt.ylabel("Grau")
    plt.title(titulo)
    plt.xticks(rotation = 45, ha = 'right')
    plt.tight_layout()
    plt.savefig(diretorio)
    plt.show()


def centralities(G):
    CG = nx.degree_centrality(G)
    CI = nx.betweenness_centrality(G)
    CP = nx.closeness_centrality(G)
    EV = nx.eigenvector_centrality(G)

    return CG, CI, CP, EV


G = graph_network()
print(len(G.nodes()), len(G.edges()))

CG, CI, CP, EV = centralities(G)
plot(CG, "plots/grau.png", "Centralidade de grau", "red")
plot(CI, "plots/intermediacao.png", "Centralidade de intermediação", "blue")
plot(CP, "plots/proximidade.png", "Centralidade de proximidade", "orange")
plot(EV, "plots/autovetor.png", "Centralidade de autovetor", "green")

nx.write_gml(G, "BRASNAM.gml")