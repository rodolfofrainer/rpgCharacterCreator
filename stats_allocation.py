class Stats():
    def __init__(self):
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

    def stats_allocation(self):
        # subtract points from spending_points and add to selected stat
        spending_points = 27
        print("Initial stats:")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")
        attributes = ["strength", "dexterity", "constitution",
                      "intelligence", "wisdom", "charisma"]
        while spending_points > 0:
            print(f"You have {spending_points} points left to spend.")
            print(f"Which stat do you want to allocate points to?:")
            for index, attribute in enumerate(attributes):
                print(f"{index + 1}. {attribute}")
            stat = int(input())

            points = int(
                input("How many points do you want to spend on this stat? "))

            if points > spending_points:
                print("You cannot spend more points than you have available.")
                continue

            if stat == 1:
                self.strength += points
            elif stat == 2:
                self.dexterity += points
            elif stat == 3:
                self.constitution += points
            elif stat == 4:
                self.intelligence += points
            elif stat == 5:
                self.wisdom += points
            elif stat == 6:
                self.charisma += points
            else:
                print("Invalid stat selection. Please try again.")
                continue

            spending_points -= points
            print("Updated stats:")
            print(f"Strength: {self.strength}")
            print(f"Dexterity: {self.dexterity}")
            print(f"Constitution: {self.constitution}")
            print(f"Intelligence: {self.intelligence}")
            print(f"Wisdom: {self.wisdom}")
            print(f"Charisma: {self.charisma}")

        print("All points allocated.")

    def stats_return(self):
        return {
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Constitution": self.constitution,
            "Intelligence": self.intelligence,
            "Wisdom": self.wisdom,
            "Charisma": self.charisma
        }
