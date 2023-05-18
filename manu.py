"""
Version Manu
"""
import os


class Graph:
    def __init__(self, nodes, source, sink, arcs, capacities):
        self.n = nodes  # nombre de noeuds
        self.s = source  # numéro de la source
        self.t = sink  # numéro du puits
        self.a = arcs  # nombre d'arcs
        self.u = capacities  # capacités des arcs

    def write(self):
        text = "Maximize\n"
        text += self.make_objective()
        text += "\nSubject To\n"
        text += self.make_constraints()
        text += "\nBounds\n"
        text += self.make_bounds()
        text += "\nInteger\n"
        text += self.make_integer()
        text += "\nEnd"
        print(text)

    def generate_lp(self):
        text = "Maximize\n"
        text += self.make_objective()
        text += "\nSubject To\n"
        text += self.make_constraints()
        text += "\nBounds\n"
        text += self.make_bounds()
        text += "\nInteger\n"
        text += self.make_integer()
        text += "\nEnd"
        with open("model.lp", "w") as lp_file:
            lp_file.write(text)
            lp_file.write("End\n")

    def make_objective(self):
        obj = "    obj: "
        objective = ""
        for i in range(self.n):
            if self.u[self.s][i] > 0:
                objective += " + f_" + str(self.s) + "_" + str(i)
        return obj + objective[3:]

    def make_constraints(self):
        constraints = ""
        flot_source = ""
        flot_puits = ""
        for i in range(self.n):
            flots_sortants = ""
            flots_entrants = ""

            if i == self.s:
                for j in range(self.n):
                    if self.u[i][j] > 0 and j != self.t:
                        flots_sortants += " + f_" + str(i) + "_" + str(j)
                flot_source = flots_sortants[3:]  # source

            elif i == self.t:
                for j in range(self.n):
                    if self.u[j][i] > 0 and j != self.s:
                        flots_entrants += " - f_" + str(j) + "_" + str(i)
                flot_puits = flots_entrants[3:]  # puits

            else:
                for j in range(self.n):
                    if self.u[i][j] > 0:
                        flots_sortants += " + f_" + str(i) + "_" + str(j)
                    elif self.u[j][i] > 0:
                        flots_entrants += " - f_" + str(j) + "_" + str(i)
                constraints += "\n    " + flots_sortants[3:] + " - " + flots_entrants[3:] + " = 0"

        constraints += "\n    " + flot_source + " - " + flot_puits + " = 0"
        return constraints[1:]

    def make_bounds(self):
        bounds = ""
        for i in range(self.n):
            for j in range(self.n):
                if self.u[i][j] > 0:
                    bounds += "\n    " + "0 <= f_" + str(i) + "_" + str(j) + " <= " + str(self.u[i][j])
        return bounds[1:]

    def make_integer(self):
        integer = ""
        for i in range(self.n):
            for j in range(self.n):
                if self.u[i][j] > 0:
                    integer += "\n    " + "f_" + str(i) + "_" + str(j)
        return integer[1:]


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

    g.generate_lp()

    os.system("glpsol --lp model.lp -o model.sol")


if __name__ == '__main__':
    main()
