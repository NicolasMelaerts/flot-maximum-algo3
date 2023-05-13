"""

Auteur :

Date :

But du project :

"""
from chemin_augmentant import Graph


def readInstance(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        nodes = int(lines[0].split()[1])
        source = int(lines[1].split()[1])
        sink = int(lines[2].split()[1])
        arcs = int(lines[3].split()[1])
        capacities = [[0 for _ in range(nodes)] for _ in range(nodes)]
        for line in lines[4:]:
            i, j, c = line.split()
            capacities[int(i)][int(j)] = int(c)
    return nodes, source, sink, arcs, capacities


def main():
    instance = "Instances/inst-700-0.3.txt"
    #print(readInstance(instance))
    nodes, source, sink, arcs, capacities = readInstance(instance)
    g = Graph(nodes, source, sink, arcs, capacities)
    print(g.augmenting_paths())


if __name__ == '__main__':
    main()
