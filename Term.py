class Term:
    def __init__(self, arity, degree):
        self.arity = arity
        self.degree = degree

    def __str__(self):
        if self.degree == 0:
            return str(self.arity)
        elif self.degree == 1:
            return str(self.arity) + "x"
        else:
            return str(self.arity) + "x^" + str(self.degree)
