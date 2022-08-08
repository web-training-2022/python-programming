employees = [ ["Dinesh", "IT"], ["Amit","Staff"],
 ["Sumit", "IT"], ["Priyanka","HR"] , ["Pavan","IT"] ]

def declare_bonus(**args):
    def get_amount(name, salary):
        dept=None
        for employee in employees:
            if employee[0] == name:
                dept = employee[1]
        bonus_amount = args.get(dept)
        return salary * bonus_amount
    return get_amount

if __name__ == "__main__":
    bonuses = {
        "IT": 1,
        "Staff": 2,
        "HR": 4
    }
    get_bonus = declare_bonus(**bonuses)

    print(f"Dinesh bonus = {get_bonus('Dinesh', 10000)} ")
    print(f"Amit bonus = {get_bonus('Amit', 10000)} ")
    print(f"Sumit bonus = {get_bonus('Sumit', 10000)} ")
    print(f"Priyanka bonus = {get_bonus('Priyanka', 10000)} ")
    print(f"Pavan bonus = {get_bonus('Pavan', 10000)} ")


