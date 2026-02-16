r = ["Ensign", "Lieutenant", "Lieutenant Commander", "Commander","Captain"]
p = {"Ensign": 200, "Lieutenant": 400, "Lieutenant Commander": 600, "Commander": 800, "Captain": 1000}

def find_index(ids):
    try:
        target = int(input("Enter ID: "))
        return ids.index(target)
    except:
        print("ID not found.")
        return None


def init_database():
    return (["Picard", "Riker", "Data", "Worf", "Kirk"],
    ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Commander"],
    ["Command", "Command", "Operations", "Operations", "Sciences"],
    [1001, 1002, 1003, 1004, 1005])


def display_menu(user):
    print("\n=== Starfleet Manager ===")
    print(f"Logged in: {user}")
    print("1 Add Member")
    print("2 Remove Member")
    print("3 Update Rank")
    print("4 Display Roster")
    print("5 Search Crew")
    print("6 Filter Division")
    print("7 Calculate Payroll")
    print("8 Count Officers")
    print("9 Exit")
    return input("Choice: ")


def add_member(names, ranks, divs, ids):
    name = input("Name: ")

    try:
        new_id = int(input("ID: "))
        if new_id in ids:
            print("Duplicate ID.")
            return
    except:
        print("Invalid ID.")
        return

    rank = input(f"Rank {r}: ").title()
    if rank not in r:
        print("Invalid rank.")
        return

    div = input("Division (Command/Operations/Sciences): ").title()

    names.append(name)
    ranks.append(rank)
    divs.append(div)
    ids.append(new_id)

    print("Added.")


def remove_member(names, ranks, divs, ids):
    idx = find_index(ids)
    if idx is None:
        return

    for lst in (names, ranks, divs, ids):
        lst.pop(idx)

    print("Removed.")


def update_rank(names, ranks, ids):
    idx = find_index(ids)
    if idx is None:
        return

    new_rank = input(f"New Rank {r}: ").title()
    if new_rank not in r:
        print("Invalid rank.")
        return

    ranks[idx] = new_rank
    print("Rank updated.")


def display_roster(names, ranks, divs, ids):
    print("\nID    Name                     Rank                     Division")
    print("-"*65)

    for i in range(len(names)):
        print(f"{ids[i]:<6}{names[i]:<25}{ranks[i]:<25}{divs[i]}")


def search_crew(names, ranks, divs, ids):
    term = input("Search name: ").lower()

    found = False
    for n, r, d, i in zip(names, ranks, divs, ids):
        if term in n.lower():
            print(i, n, r, d)
            found = True

    if not found:
        print("No matches.")


def filter_by_division(names, divs):
    choice = input("Division (Command/Operations/Sciences): ").title()

    for n, d in zip(names, divs):
        if d == choice:
            print(n, "-", d)


def calculate_payroll(ranks):
    total = sum(p.get(r, 0) for r in ranks)
    print("Total Payroll:", total)
    return total


def count_officers(ranks):
    count = sum(1 for r in ranks if r in ("Captain", "Commander"))
    print("Senior Officers:", count)
    return count


def Start_up():
    names, ranks, divs, ids = init_database()
    user = input("Enter name: ")

    while True:
        opt = display_menu(user)

        if opt == "1":
            add_member(names, ranks, divs, ids)

        elif opt == "2":
            remove_member(names, ranks, divs, ids)

        elif opt == "3":
            update_rank(names, ranks, ids)

        elif opt == "4":
            display_roster(names, ranks, divs, ids)

        elif opt == "5":
            search_crew(names, ranks, divs, ids)

        elif opt == "6":
            filter_by_division(names, divs)

        elif opt == "7":
            calculate_payroll(ranks)

        elif opt == "8":
            count_officers(ranks)

        elif opt == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

Start_up()


