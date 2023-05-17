"""
Chemins augmentants
"""


INF = 1000000000  # +infini


class Graph:
    def __init__(self, nodes, source, sink, arcs, capacities):
        self.n = nodes       # nombre de noeuds
        self.s = source      # numéro de la source
        self.t = sink        # numéro du puits
        self.a = arcs        # nombre d'arcs
        self.u = capacities  # capacités des arcs

        self.f = [[0 for _ in range(nodes)] for _ in range(nodes)]  # flot

        self.mark = {}  # marque

    def augmenting_paths(self):
        optimal = False
        while not optimal:
            for i in range(self.n):  # réinitialise la marque de chaque noeud
                self.mark[i] = [0, 0]

            optimal = self.marking()  # 1) phase de marquage
            self.augmentation()       # 2) phase d'augmentation

        return sum(self.f[self.s])  # flot maximum (=somme des flots sortant de s)

    def marking(self):
        self.mark[self.s] = [0, INF]
        L = [self.s]
        while len(L) > 0 and self.mark[self.t] == [0, 0]:
            i = L.pop()
            for j in range(self.n):  # pour tout j non marqué tel que (ij) inclus dans A
                if self.mark[j][1] == 0 and self.f[i][j] < self.u[i][j]:
                    alpha_i = self.mark[i][1]
                    alpha_j = min(alpha_i, self.u[i][j] - self.f[i][j])
                    self.mark[j] = [i, alpha_j]
                    L.append(j)
            for j in range(self.n):  # pour tout j non marqué tel que (ji) inclus dans A
                if self.mark[j][1] == 0 and self.f[j][i] > 0:
                    alpha_i = self.mark[i][1]
                    alpha_j = min(alpha_i, self.f[j][i])
                    self.mark[j] = [i, alpha_j]
                    L.append(j)
        if self.mark[self.t][1] == 0:
            return True  # plus de chemin augmentant - STOP
        return False

    def augmentation(self):
        j = self.t
        while j != self.s:
            (i, alpha_j) = self.mark[j]
            alpha_t = self.mark[self.t][1]
            if self.u[i][j] > 0:
                self.f[i][j] += alpha_t  # (i,j) est un arc en avant
            else:
                self.f[i][j] -= alpha_t  # (i,j) est un arc en arrière
            j = i


def read_instance(file_path):
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
    instance = "Instances/inst-100-0.1.txt"

    nodes, source, sink, arcs, capacities = read_instance(instance)
    g = Graph(nodes, source, sink, arcs, capacities)

    print(g.augmenting_paths())


if __name__ == '__main__':
    main()
