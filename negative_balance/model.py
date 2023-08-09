from pyomo.environ import *
from negative_balance.data import NBData


class LPModel(object):
    def __init__(self, data):
        self.data = data
        return None
    
    def build(self, data):
        # Define sets
        model = ConcreteModel()

        # Define variables
        model.x = Var(data.ij_set, domain=NonNegativeReals)

        # Define objective
        model.obj = Objective(expr=summation(model.x), sense=maximize)

        # Define constraints
        def _account_balance(model, j):
            return sum(model.x[i, j] for i in data.I_j[j]) <= data.a_j[j]
        model.account_balance = Constraint(data.J, rule=_account_balance)

        def _negative_balance(model, i):
            return sum(model.x[i, j] for j in data.J_i[i]) + data.c_i[i] <= 0
        model.negative_balance = Constraint(data.I, rule=_negative_balance)

        return model
    
    def solve(self):
        model = self.build(self.data)
        solver = SolverFactory('cbc')
        solver.solve(model)
        return model
    
    def print_solution(self, model):
        print(f"Objective: {model.obj()}")
        print("x:")
        for (i, j) in self.data.ij_set:
            print(f"\t{i}, {j}: {model.x[i, j]()}")


if __name__ == '__main__':
    data = NBData().toy()
    model = LPModel(data).solve()
    LPModel(data).print_solution(model)