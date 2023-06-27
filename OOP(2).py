class Y:
    """The  vertical  motion  of  a  ball."""

    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2

    def formula(self):
        return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0

y = Y(5)
t = 0.2
v = y.value(t)
print('y(t=%g; v0=%g) = %g' % (t, y.v0, v))
print(y.formula())