"""
Version Manu
"""


class Graph:
    def __init__(self, nodes, source, sink, arcs, capacities):
        self.n = nodes  # nombre de noeuds
        self.s = source  # numéro de la source
        self.t = sink  # numéro du puits
        self.a = arcs  # nombre d'arcs
        self.u = capacities  # capacités des arcs

    def write(self):
        text = "Maximise\n"
        text += self.make_objective()
        text += "\nSubject To\n"
        text += self.make_constraints()
        text += "\nBounds\n"
        text += self.make_bounds()
        text += "\nInteger\n"
        text += self.make_integer()
        text += "\nEnd"
        print(text)

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
            flots_entrants = ""
            flots_sortants = ""
            for j in range(self.n):
                if self.u[i][j] > 0:
                    flots_entrants += " + f_" + str(i) + "_" + str(j)
                elif self.u[j][i] > 0:
                    flots_sortants += " - f_" + str(j) + "_" + str(i)
            if i == self.s:
                flot_source = flots_entrants[3:]  # source
            elif i == self.t:
                flot_puits = flots_sortants[3:]  # puits
            else:
                constraints += "\n    " + flots_entrants[3:] + " - " + flots_sortants[3:] + " = 0"
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


m = [[0, 20, 30, 80,  0],
     [0,  0, 40,  0, 30],
     [0,  0,  0, 10, 20],
     [0,  0,  5,  0, 30],
     [0,  0,  0,  0,  0]]

A = Graph(5, 0, 4, 9, m)

A.write()
