class Walk:
    """
    Walk objects can be used to build walks from Graphs.
    A Walk is simply a list of vertices in the order in which they occur in the walk.  The edges are not listed.

    Note: this class does not verify the validity of the walk,
    i.e. it does not verify whether there are valid edges between two adjacent vertices in the walk.

    DO NOT MODIFY THIS CLASS
    """

    NOVERTEX = -1

    def __init__(self, maxVertices):
        """
        Creates a new empty Walk.

        Parameters:
          int maxVertices: The maximum number of vertices in the Walk.
        """
        # Maximum possible length of Walk, including last edge returning to first vertex.
        self.maxV = maxVertices

        # Actual length of Walk, including last edge returning to first vertex.
        self.totalV = 0

        # The vertices are listed in their order of traversal.
        self.vertices = []
        for i in range(maxVertices):
            self.vertices.append(0)

    def __str__(self):
        """Returns a String representation of the Walk which is simply a list of vertices separated by blanks."""
        if self.totalV == 0:
            return ""
        res = ""
        for i in range(self.totalV - 1):
            res += str(self.vertices[i])
            res += " "
        res += str(self.vertices[self.totalV - 1])
        return res

    def isEmpty(self):
        """Returns True iff the walk has no vertices."""
        return self.totalV == 0

    def isTrivial(self):
        """Returns True iff the walk is a single vertex."""
        return self.totalV == 1

    def isCircuit(self):
        """Returns True iff the walk is a non-empty circuit."""
        if self.totalV == 0:
            return False
        return self.vertices[0] == self.vertices[self.totalV - 1]

    def __len__(self):
        """Returns the number of edges in the Walk.
        Note: an empty Walk and a Walk with a single vertex both have length 0.
        """
        return self.length()

    def length(self):
        """Returns the number of edges in the Walk.
        Note: an empty Walk and a Walk with a single vertex both have length 0.
        """
        if self.totalV == 0:
            return 0
        return self.totalV - 1

    def totalVertices(self):
        """Returns the number of vertices in the Walk."""
        return self.totalV

    def getVertex(self, n):
        """Returns the nth vertex in the Walk or Walk.NOVERTEX if there is no such vertex.

        Parameters:
          int n: position of vertex to be returned.  Counting starts at 0.
        """
        if 0 <= n and n < self.totalV:
            return self.vertices[n]
        else:
            return NOVERTEX

    def getVertices(self):
        """ Returns a copy of the list of vertices in the Walk. """
        return self.vertices.copy()

    def addVertex(self, vertex):
        """Adds another vertex to the end of the Walk if possible.

        Parameters:
          vertex: vertex to be added

        Returns True iff the vertex could be added, i.e maxVertices was not reached
        """
        if self.totalV == self.maxV:
            return False
        self.vertices[self.totalV] = vertex
        self.totalV += 1
        return True

    def removeLastVertex(self):
        """Removes the last vertex added to Walk if possible.
        Returns True iff the last vertex could be removed, i.e Walk was not empty
        """
        if self.totalV == 0:
            return False
        self.totalV -= 1
        self.vertices[self.totalV] = 0
        return True
