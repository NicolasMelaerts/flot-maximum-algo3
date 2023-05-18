"""

Auteur :

Date :

But du project :

"""

import glob
import os

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
    fichiers = ['inst-100-0.1.txt', 'inst-100-0.2.txt', 'inst-100-0.3.txt', 'inst-200-0.1.txt', 'inst-200-0.2.txt', 'inst-200-0.3.txt', 'inst-300-0.1.txt', 'inst-300-0.2.txt', 'inst-300-0.3.txt', 'inst-400-0.1.txt', 'inst-400-0.2.txt', 'inst-400-0.3.txt', 'inst-500-0.1.txt', 'inst-500-0.2.txt', 'inst-500-0.3.txt', 'inst-600-0.1.txt', 'inst-600-0.2.txt', 'inst-600-0.3.txt', 'inst-700-0.1.txt', 'inst-700-0.2.txt', 'inst-700-0.3.txt', 'inst-800-0.1.txt', 'inst-800-0.2.txt', 'inst-800-0.3.txt', 'inst-900-0.1.txt', 'inst-900-0.2.txt', 'inst-900-0.3.txt', 'inst-1000-0.1.txt', 'inst-1000-0.2.txt', 'inst-1000-0.3.txt', 'inst-1100-0.1.txt', 'inst-1100-0.2.txt', 'inst-1100-0.3.txt', 'inst-1200-0.1.txt', 'inst-1200-0.2.txt', 'inst-1200-0.3.txt', 'inst-1300-0.1.txt', 'inst-1300-0.2.txt', 'inst-1300-0.3.txt', 'inst-1400-0.1.txt', 'inst-1400-0.2.txt', 'inst-1400-0.3.txt', 'inst-1500-0.1.txt', 'inst-1500-0.2.txt', 'inst-1500-0.3.txt']
    solCheminAugmentant = []
    solGenerateModel = []



    for fichier in fichiers:
        nodes, source, sink, arcs, capacities = read_instance(fichier)
        gCheminAugmentant = GraphCheminAugmentant(nodes, source, sink, arcs, capacities)
        solCheminAugmentant.append(gCheminAugmentant.augmenting_paths())

        gGenerateModel = Graph(nodes, source, sink, arcs, capacities)
        text = gGenerateModel.generate_lp()

        lpfile = "model-" + fichier[5:12] + "lp"

        with open(lpfile, "w") as f:
            f.write(text)

        solFile = lpfile[:-3] + ".sol"

        str = "glpsol --lp " + lpfile + " -o " + solFile

        os.system(str + ' > fichier_sortie.txt')

        solGenerateModel.append(recupSol(solFile))

    for i in range(len(fichiers)):
        print(fichiers[i])

        str1 = "Chemin augmentant : "
        print(str1)
        print(solCheminAugmentant[i])

        str2 = "Generate model : "
        print(str2)
        print(solGenerateModel[i])

        print('\n')










if __name__ == '__main__':
    main()
