class MySet:
    def __init__(self):
        self.elements = []

    def add_elements(self, n):
        for i in range(n):
            x = input("Enter element: ")
            if x not in self.elements:
                self.elements.append(x)

    def is_member(self, x):
        return x in self.elements

    def power_set(self):
        ps = [[]]
        for e in self.elements:
            ps += [subset + [e] for subset in ps]
        return ps

    def is_subset(self, other):
        for e in self.elements:
            if e not in other.elements:
                return False
        return True

    def union(self, other):
        result = MySet()
        result.elements = self.elements[:]
        for e in other.elements:
            if e not in result.elements:
                result.elements.append(e)
        return result

    def intersection(self, other):
        result = MySet()
        for e in self.elements:
            if e in other.elements:
                result.elements.append(e)
        return result

    def difference(self, other):
        result = MySet()
        for e in self.elements:
            if e not in other.elements:
                result.elements.append(e)
        return result

    def symmetric_difference(self, other):
        return self.difference(other).union(other.difference(self))

    def complement(self, universal):
        return universal.difference(self)

    def cartesian_product(self, other):
        return [(a, b) for a in self.elements for b in other.elements]

    def display(self):
        print(self.elements)


# -------- MAIN PROGRAM --------
A = MySet()
B = MySet()

print("Enter elements for Set A")
n = int(input("Number of elements: "))
A.add_elements(n)

print("\nEnter elements for Set B")
n = int(input("Number of elements: "))
B.add_elements(n)

while True:
    print("\n----- SET OPERATIONS MENU -----")
    print("1. Is Member")
    print("2. Power Set")
    print("3. Subset Check")
    print("4. Union")
    print("5. Intersection")
    print("6. Complement")
    print("7. Difference")
    print("8. Symmetric Difference")
    print("9. Cartesian Product")
    print("0. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # ---------- SINGLE SET OPERATIONS ----------
    if ch in [1, 2, 6]:
        set_choice = input("Operate on which set? (A/B): ").upper()
        current = A if set_choice == 'A' else B

    if ch == 1:
        x = input("Enter element to check: ")
        print("Result:", current.is_member(x))

    elif ch == 2:
        print("Power Set:")
        print(current.power_set())

    elif ch == 3:
        print("A ⊆ B :", A.is_subset(B))
        print("B ⊆ A :", B.is_subset(A))

    elif ch == 4:
        print("Union of A and B:")
        A.union(B).display()

    elif ch == 5:
        print("Intersection of A and B:")
        A.intersection(B).display()

    elif ch == 6:
        U = MySet()
        print("Enter Universal Set")
        n = int(input("Number of elements: "))
        U.add_elements(n)
        print("Complement:")
        current.complement(U).display()

    elif ch == 7:
        diff_choice = input("Choose difference (A-B / B-A): ").upper()
        if diff_choice == "A-B":
            A.difference(B).display()
        elif diff_choice == "B-A":
            B.difference(A).display()
        else:
            print("Invalid option")

    elif ch == 8:
        print("Symmetric Difference:")
        A.symmetric_difference(B).display()

    elif ch == 9:
        print("Cartesian Product A × B:")
        print(A.cartesian_product(B))

    elif ch == 0:
        print("Program terminated")
        break

    else:
        print("Invalid choice!")
