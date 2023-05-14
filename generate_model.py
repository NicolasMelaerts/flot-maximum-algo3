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


def generateObjectiveFunction(capacities, nodes, source):
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




def generateConstraints(nodes, source, sink, capacities):
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




def generateVariables(nodes):
    variables = []
    for i in range(nodes):
        for j in range(nodes):
            if i != j:
                variable = "x_" + str(i) + "_" + str(j)
                variables.append(variable)
    return variables


def generateLP(file):
    nodes, source, sink, arcs, capacities = readInstance(file)

    obj = generateObjectiveFunction(capacities, nodes, source)

    const = generateConstraints(nodes, source, sink, capacities)

    vars = generateVariables(nodes)

    # Écrire dans le fichier lp
    with open("model.lp", "w") as lp_file:
        lp_file.write("Maximize\n")
        lp_file.write(obj)
        lp_file.write("\nSubject To\n")

        for constraint in const:
            lp_file.write(constraint + "\n")

        lp_file.write("Bounds\n")
        for variable in vars:
            lp_file.write("    0 <= " + str(variable) + " <= 1\n")

        lp_file.write("Integer\n")
        for variable in vars:
            lp_file.write("    " + str(variable) + "\n")

        lp_file.write("End\n")
