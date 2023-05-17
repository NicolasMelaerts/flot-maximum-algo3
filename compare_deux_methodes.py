"""
Comparaison des deux versions sur un graphe très simple
"""


# VERSION MANU


class Graph:
    def __init__(self, nodes, source, sink, arcs, capacities):
        self.n = nodes  # nombre de noeuds
        self.s = source  # numéro de la source
        self.t = sink  # numéro du puits
        self.a = arcs  # nombre d'arcs
        self.u = capacities  # capacités des arcs

    def writeManu(self):
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


# VERSION NICOLAS


    def generateObjectiveFunction(self):
        capacities = self.u
        nodes = self.n
        source = self.s

        obj = "    obj: "
        fonct = ""

        for i in range(nodes):
            for j in range(nodes):
                if capacities[i][j] > 0:
                    if i == source:
                        fonct += " + x_" + str(i) + "_" + str(j)
                    elif j == source:
                        fonct += " - x_" + str(i) + "_" + str(j)

        return obj + fonct[2:]

    def generateConstraints(self):
        capacities = self.u
        nodes = self.n
        source = self.s
        sink = self.t

        used_vars = set()
        constraints = []
        for i in range(nodes):
            if i != source and i != sink:
                temp = []
                for j in range(nodes):
                    if capacities[i][j] > 0:
                        temp.append(" + x_" + str(i) + "_" + str(j))
                        used_vars.add((i, j))
                    if capacities[j][i] > 0 and (j, i) not in used_vars:
                        temp.append(" - x_" + str(j) + "_" + str(i))
                constraint = "    c_" + str(i) + ":"
                for t in temp:
                    constraint += t
                constraint += " = 0"
                constraints.append(constraint)

        return constraints

    def generateVariables(self):
        nodes = self.n

        variables = []
        for i in range(nodes):
            for j in range(nodes):
                if i != j:
                    variable = "x_" + str(i) + "_" + str(j)
                    variables.append(variable)
        return variables

    def writeNico(self):
        obj = self.generateObjectiveFunction()

        const = self.generateConstraints()

        vars = self.generateVariables()

        # Écrire
        print("Maximize\n")
        print(obj)
        print("\nSubject To\n")

        for constraint in const:
            print(constraint + "\n")

        print("Bounds\n")
        for variable in vars:
            print("    0 <= " + str(variable) + " <= 1\n")

        print("Integer\n")
        for variable in vars:
            print("    " + str(variable) + "\n")

        print("End\n")


m = [[0, 20, 30, 80,  0],
     [0,  0, 40,  0, 30],
     [0,  0,  0, 10, 20],
     [0,  0,  5,  0, 30],
     [0,  0,  0,  0,  0]]

A = Graph(5, 0, 4, 9, m)

print(
    "\n\n\n#####################################\n"
    "            METHODE MANU\n#####################################\n\n\n")
A.writeManu()

print(
    "\n\n\n#####################################\n"
    "            METHODE NICO\n#####################################\n\n\n")
A.writeNico()

