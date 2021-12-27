from decimal import Decimal


def f(t:float,C:float,citizen_votes:list[list]) -> list:
    liner_fun=[]
    median=[]
    temp_l=[]
    for j in range (0,len(citizen_votes[0])):
        for i in range(0,len(citizen_votes)):
            temp_l.append(citizen_votes[i][j])
        median.append(temp_l)
        temp_l=[]
    for i in range (1,len(citizen_votes)):
        liner_fun.append(C*min(1,i*float(t)))
    budget=[]
    for l in median:
        l+=liner_fun
        l.sort()
        budget.append(l[int(len(l)/2)])
    return budget

def compute_budget(total_budget:float, citizen_votes:list[list]) ->list[float]:
    C=total_budget
    l, r = 0, 1
    t = 0.1
    budget = f(t, C, citizen_votes)
    sum_bud = sum(budget)

    while C != sum_bud:
        if C>sum_bud:
            l=t
        else: # C> budget
            r=t
        t = (Decimal(l) + Decimal(r)) / Decimal(2)
        budget=f(t,C,citizen_votes)
        sum_bud=sum(budget)
    return budget




if __name__ == '__main__':
    print(compute_budget(100, [[100,0,0],[0,0,100]]))
    print(compute_budget(30,[[6,6,6,6,0,0,6,0,0],[0,0,6,6,6,6,0,6,0],[6,6,0,0,6,6,0,0,6]]))
    print(compute_budget(30,[[15,15,0],[0,20,10],[3,0,27]]))

