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



def generateObjectiveFunction():
    obj = "    obj: "

    # TO DO

    return obj





def generateLP(file):
    nodes, source, sink, arcs, capacities = readInstance(file)

    obj = generateObjectiveFunction()



    # écrire dans le fichier lp

    lp_file = open("model.lp", "w")
    lp_file.write("Maximize\n")
    lp_file.write(obj)
    lp_file.write("\nSubject To\n")

    #for constraint in constraints:
    #    lp_file.write(constraint + "\n")

    lp_file.write("Bounds\n")

    lp_file.write("Integer\n")

    lp_file.write("End")

    lp_file.close()

