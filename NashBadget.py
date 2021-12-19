import cvxpy
import functools

def nashBudget(total: float, subject: list[str], pref: list[list[str]]):
    allocations = cvxpy.Variable(len(subject))
    donations = total / len(pref)

    utilities = []
    for i in range(0, len(pref)):
        utilities.append(0)
        for j in range(0, len(pref[i])):
            utilities[i] += allocations[subject.index(pref[i][j])]

    sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])
    positivity_constraints = [v >= 0 for v in allocations]
    sum_constraint = [cvxpy.sum(allocations) == total]
    problem = cvxpy.Problem(
        cvxpy.Maximize(sum_of_logs),
        constraints=positivity_constraints + sum_constraint)
    problem.solve()

    utility_values = [u.value for u in utilities]
    print("BUDGET: a={}, b={}, c={}, d={}".format(*allocations.value))
    print("UTILS : {}, {}, {}, {}, {}".format(*utility_values))
    utility_product = functools.reduce(lambda a, b: a * b, utility_values)
    print("PRODUCT: {}".format(utility_product))

    for i in range(0, len(pref)):
        print("Citizen {} should donate:".format(i)),
        for u in subject:
            if u in pref[i]:
                print("{} to {}".format(allocations[subject.index(u)].value * donations / utilities[i].value, u)),
        print()


if __name__ == '__main__':
    utilities = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['a']]
    nashBudget(500, ['a', 'b', 'c', 'd'], utilities)
