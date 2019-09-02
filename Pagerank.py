import networkx as nx
import matplotlib.pyplot as plt

def pagerank(Graph, alpha=0.85, personalization = None , max_iteration = 50 , tolerance = 1.0e-8, initial_set_rank = None , weight='weight', dangling=None):

    if len(Graph) == 0:
        return {}
    #check directed of graph
    if not Graph.is_directed():
        Directed_Graph = Graph.to_directed()
    else:
        Directed_Graph = Graph
    #get graph to stochastic graph
    stochastic_graph = nx.stochastic_graph(Directed_Graph, weight=weight)
    Number_node = stochastic_graph.number_of_nodes()

    #set initial rank for each node
    if initial_set_rank is None:
        x = dict.fromkeys(stochastic_graph, 1.0 / Number_node)
    else:
        sum_initial_set_rank = float(sum(initial_set_rank.values()))
        x = dict((key, value / sum_initial_set_rank) for key, value in initial_set_rank.items())


    #craete fake link between each node
    if personalization is None:
        personalization_vector = dict.fromkeys(stochastic_graph, 1.0 / Number_node)
    else:

        sum_personalization_vector = float(sum(personalization.values()))
        personalization_vector = dict((key, value / sum_personalization_vector) for key, value in personalization.items())


    #set stochastic value for node without outlink
    if dangling is None:
        dangling_weights = personalization_vector
    else:

        sum_dangling_weights = float(sum(dangling.values()))
        dangling_weights = dict((key, value / sum_dangling_weights) for key, value in dangling.items())
    dangling_nodes = [n for n in stochastic_graph if stochastic_graph.out_degree(n, weight=weight) == 0.0]

    #calculate the rank for matrix A = αP +(1−α)1/n*eeT
    for i in range(max_iteration):
        print("iteration {} : the rank of page is :\n".format(i))
        last_rank = x
        x = dict.fromkeys(last_rank.keys(), 0)
        danglesum = alpha * sum(last_rank[n] for n in dangling_nodes)
        for n in x:
            for nbr in stochastic_graph[n]:
                x[nbr] += alpha * last_rank[n] * stochastic_graph[n][nbr][weight]
            x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * personalization_vector[n]
        print(x)
        print("\n----------------------------------------------------------")
        err = sum([abs(x[n] - last_rank[n]) for n in x])
        if err < Number_node * tolerance:
            print("The algoritm is converge and the last rank is :\n")
            return x

Graph_barabashi = nx.barabasi_albert_graph(60,40)
nx.draw(Graph_barabashi, axis = 1 ,with_labels= True , arrows = True ,node_color = "m" , node_shape = "o" , edge_color = "c",alpha=1.0)

plt.show()
result_of_rank = pagerank(Graph_barabashi)
print(result_of_rank)