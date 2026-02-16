r = ["Ensign", "Lieutenant", "Lieutenant Commander", "Commander","Captain"]
p = {"Ensign": 200, "Lieutenant": 400, "Lieutenant Commander": 600, "Commander": 800, "Captain": 1000}


def Start_up():
   
   print("BOOTING SYSTEM...")
   print("...")
   print("WELCOME TO FLEET COMMAND")
   
   names, ranks, divs, ids = database()
   user = input("Enter name: ")

   while True:
    print("\n--- MENU ---")
    print("1. Add Crew")
    print("2. Remove Crew")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
        
    opt = input("Select option: ")

    if opt == "1":
        name = input("Name: ")

        try:
            new_id = int(input("ID: "))
            if new_id in ids:
                print("Duplicate ID.")
                continue
        except:
            print("Invalid ID.")
            continue

        rank = input(f"Rank {r}: ").title()
        if rank not in r:
            print("Invalid rank.")
            continue

        div = input("Division (Command/Operations/Sciences): ").title()

        names.append(name)
        ranks.append(rank)
        divs.append(div)
        ids.append(new_id)

        print("Added.")

    elif opt == "2":
        idx = find_index(ids)
        if idx is None:
            continue

        for lst in (names, ranks, divs, ids):
            lst.pop(idx)

        print("Removed.")

    elif opt == "3":
        idx = find_index(ids)
        if idx is None:
            continue
        
        new_rank = input(f"Rank {r}: ").title()
        if new_rank not in r:
            print("Invalid rank.")
            continue
        
        ranks[idx] = new_rank
        print("Rank updated.")

    elif opt == "4":
        print("Current Crew Roster:")
        for i in range(len(names)):
            print(f"{ids[i]}, {names[i]}, {ranks[i]}, {divs[i]}")

    elif opt == "5":
        term = input("Search name: ").lower()

        found = False
        for crew_id, crew_name, crew_rank, crew_div in zip(ids, names, ranks, divs):
            if term in crew_name.lower():
                print(crew_id, crew_name, crew_rank, crew_div)
                found = True

        if not found:
            print("No matches.")

    elif opt == "6":
        choice = input("Division (Command/Operations/Sciences): ")
        for crew_id, crew_name, crew_rank, crew_div in zip(ids, names, ranks, divs):
            if crew_div == choice:
                print(crew_id, crew_name, "-", crew_div)

    elif opt == "7":
        total = sum(p.get(rank, 0) for rank in ranks)
        print("Total Payroll:", total)

    elif opt == "8":
        count = sum(1 for rank in ranks if rank in ("Captain", "Commander"))
        print("Number of officers:", count)

    elif opt == "9":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")

def database():
    return (["Picard", "Riker", "Data", "Worf", "Kirk"],
    ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Commander"],
    ["Command", "Command", "Operations", "Operations", "Sciences"],
    [101, 102, 103, 104, 105])

def find_index(ids):
    try:
        search_id = int(input("ID: "))
        idx = ids.index(search_id)
        return idx
    except ValueError:
        print("Invalid ID.")
        return None
    except IndexError:
        print("ID not found.")
        return None

Start_up()