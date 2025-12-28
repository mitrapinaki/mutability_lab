def run():
    print("\n--- Aliasing and Mutation ---")

    # Example 1: two separate lists
    a = [1, 2, 3]
    b = [1, 2, 3]
    print("\nCase 1: separate lists with same content")
    print("a:", a, "| id(a):", id(a))
    print("b:", b, "| id(b):", id(b))
    print("a is b:", a is b)
    print("a == b:", a == b)

    b.append(4)
    print("\nAfter b.append(4):")
    print("a:", a)
    print("b:", b)

    # Example 2: aliasing via assignment
    x = [10, 20, 30]
    y = x  # alias
    print("\nCase 2: aliasing via y = x")
    print("x:", x, "| id(x):", id(x))
    print("y:", y, "| id(y):", id(y))
    print("x is y:", x is y)
    print("x == y:", x == y)

    y.append(40)
    print("\nAfter y.append(40):")
    print("x:", x)
    print("y:", y)
    print("Observation: mutation through one name affects the other when both "
          "refer to the same object.")

    # Example 3: aliasing with dicts
    d1 = {"ccy": "EURUSD", "px": 1.10}
    d2 = d1
    print("\nCase 3: dict aliasing")
    print("d1:", d1, "| id(d1):", id(d1))
    print("d2:", d2, "| id(d2):", id(d2))

    d2["px"] = 1.11
    print("\nAfter d2['px'] = 1.11:")
    print("d1:", d1)
    print("d2:", d2)
    print("Observation: aliasing is about references, not types.")
