from pyomo.environ import *


class LPModel(object):
    def __init__(self) -> None:
        pass

    def build(self, rhs):
        # Define model
        model = ConcreteModel()

        # Define variables
        model.x1 = Var(within=NonNegativeReals)
        model.x2 = Var(within=NonNegativeReals)

        # Define objective function
        model.obj = Objective(expr= 3*model.x1 + 4*model.x2, sense=minimize)

        # Define constraints
        r1, r2 = rhs
        model.con1 = Constraint(expr= 2*model.x1 + 3*model.x2 >= r1)
        model.con2 = Constraint(expr= 4*model.x1 + 2*model.x2 >= r2)

        return model
