from Graph import Graph
from Walk import Walk


def main():
    """
    Main test program calculates score for program.
    It first tests the getEuler method on graphs in test files.
    Then tests it on randomly generated undirected simple graphs.
    """
    dirPath = "./tests/"
    score = 0

    # Run test files to check correctness
    print("\n=======================  TEST CORRECTNESS  =======================\n")

    print("\n-------  There are no Euler circuits in the first two tests  -----\n")

    score += 4 - testInput(dirPath + "disconnected", 0)
    print("Score so far: " + str(score))

    score += 5 - testInput(dirPath + "noEuler", 0)
    print("Score so far: " + str(score))

    print("\n-------  From now on all test graphs have Euler circuits  -------\n")

    score += testInput(dirPath + "small", 6)
    print("Score so far: " + str(score))

    score += testInput(dirPath + "medium", 5)
    print("Score so far: " + str(score))

    score += testInput(dirPath + "large", 6)
    print("Score so far: " + str(score))

    score += 4 * testInput(dirPath + "verylarge", 1)
    print("Correctness score: " + str(score) + " out of 30.")

    # Test very large graphs
    print("\n=======================  TEST EFFICIENCY  =======================\n")

    score += 2 * testInput(dirPath + "huge1", 1)
    print("Score so far: " + str(score) + " out of 40.")

    score += 2 * testInput(dirPath + "huge2", 1)
    print("Score so far: " + str(score) + " out of 40.")

    score += 2 * testInput(dirPath + "huge3", 1)
    print("Score so far: " + str(score) + " out of 40.")

    score += 2 * testInput(dirPath + "huge4", 1)
    print("Score so far: " + str(score) + " out of 40.")

    score += 2 * testInput(dirPath + "huge5", 1)
    print("Final score: " + str(score) + " out of 40.")


def testInput(filename, expected):
    """
    Reads graphs from a file and tests the getEuler method on these graphs.

    Parameters:
      str filename: path of file
      int expected: number of graphs in file which have an Euler circult

    Returns the number of valid Euler circuits for the graphs in the file.
    """
    print("\n-------  Test " + filename + "  -------\n")
    found = 0
    graphList = Graph.fromFile(filename)
    for graph in graphList:
        found += testOnGraph(graph)
    print("\nEuler circuits expected: " + str(expected) + ", found: " + str(found))
    return found


def testOnGraph(graph):
    """
    Tests the getEuler method for a graph.  Prints the results.

    Parameters:
      Graph graph: graph on which the getEuler method will be tested

    Returns 1 if a valid Euler circuit has been found and 0 otherwise
    """
    print("Graph has " + str(graph.totalVertices())
          + " vertices, and " + str(graph.totalEdges()) + " edges.")
    circuit = graph.findEuler
    if (circuit is None):
        print("Graph has no Euler Circuit")
        return 0
    elif (isValidEuler(graph, circuit)):
        print("Valid Euler Circuit")
        return 1
    else:
        print("Invalid Euler Circuit")
        return 0


def isValidEuler(graph, circuit):
    """
    Verifies whether a walk is a valid Euler circuit for a graph.

    Parameters:
      Graph graph: original graph
      Walk circuit: potential Euler circuit for graph

    Returns True iff circuit is a valid Euler circuit for graph.
    """

    # First check if the path is a circuit
    if not circuit.isCircuit():
        print("Error: Path returned is not a circuit")
        return False

    # Then check if the circuit has the correct number of edges
    circuitLength = circuit.length()
    totalEdges = graph.totalEdges()
    if circuitLength < totalEdges:
        print("Error: Some edges have not been visited")
        return False
    if circuitLength > totalEdges:
        print("Error: Too many edges in circuit")
        return False

    # Now traverse the circuit to verify that it is a correct Euler circuit for this graph
    edges = graph.getEdges()
    path = circuit.getVertices()
    v1 = path[0]
    for i in range(1, circuitLength):
        v2 = path[i]
        if edges[v1][v2] == 0:
            print("Error: The graph does not have enough edges between " + str(v1) + " and" + str(
                v2) + " to support the circuit found.")
            return False
        edges[v1][v2] -= 1
        edges[v2][v1] -= 1
        v1 = v2

    return True


# calls main program
if __name__ == '__main__':
    main()