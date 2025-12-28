import copy


def run():
    print("\n--- Shallow vs Deep Copy ---")

    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    print("\nInitial state:")
    print("original:", original, "| id:", id(original))
    print("shallow :", shallow,  "| id:", id(shallow))
    print("deep    :", deep,     "| id:", id(deep))

    print("\nInner list identities:")
    print("id(original[0]):", id(original[0]))
    print("id(shallow[0]) :", id(shallow[0]))
    print("id(deep[0])    :", id(deep[0]))

    print("\nMutate original[0].append(99)")
    original[0].append(99)

    print("original:", original)
    print("shallow :", shallow)
    print("deep    :", deep)

    print("\nObservation:")
    print("- shallow copy shares inner lists with original")
    print("- deep copy recursively copies inner lists")

    # Also show behavior with dicts
    data = {"pair": {"ccy": "EURUSD", "px": 1.10}}
    shallow_d = copy.copy(data)
    deep_d = copy.deepcopy(data)

    print("\nDict example:")
    print("data     :", data)
    print("shallow_d:", shallow_d)
    print("deep_d   :", deep_d)

    data["pair"]["px"] = 1.11
    print("\nAfter data['pair']['px'] = 1.11:")
    print("data     :", data)
    print("shallow_d:", shallow_d)
    print("deep_d   :", deep_d)

    print("\nKey idea: copying only the outer container is often not enough "
          "when nested mutables are involved.")
