"""

Auteur :

Date :

But du project :

"""

import glob

from chemin_augmentant import GraphCheminAugmentant
from generate_model import Graph


def read_instance(file_path):
    file_path = "Instances/" + file_path
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

def recupSol(fichier):
    with open(fichier, "r") as file:
        ligneSol = [next(file) for i in range(6)]

    ligneSol = ligneSol[5]
    deb = ligneSol.find("=") + 1
    fin = ligneSol.find("(")
    ligneSol = ligneSol[deb:fin].strip()

    return ligneSol


def main():

    fichiers = glob.glob('Instances/*')

    for i in range(len(fichiers)):
        fichiers[i] = fichiers[i][10:]

    fichiers.sort()

    for fichier in fichiers:
        print(fichier)
        nodes, source, sink, arcs, capacities = read_instance(fichier)
        g = GraphCheminAugmentant(nodes, source, sink, arcs, capacities)

        g2 = Graph(nodes, source, sink, arcs, capacities)
        text = g2.generate_lp()
        nomSol = g2.solTest(fichier, text)


        print(g.augmenting_paths())

        print(recupSol(nomSol))



    print(fichiers)








if __name__ == '__main__':
    main()
