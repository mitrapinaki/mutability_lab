def mutate_list(lst):
    print("\nInside mutate_list: before:", lst, "| id:", id(lst))
    lst.append("X")
    print("Inside mutate_list: after :", lst, "| id:", id(lst))


def reassign_list(lst):
    print("\nInside reassign_list: before:", lst, "| id:", id(lst))
    lst = lst + ["Y"]  # creates a new list
    print("Inside reassign_list: after :", lst, "| id:", id(lst))


def mutate_dict(d):
    print("\nInside mutate_dict: before:", d, "| id:", id(d))
    d["mutated"] = True
    print("Inside mutate_dict: after :", d, "| id:", id(d))


def run():
    print("\n--- Function Argument Semantics & Mutability ---")

    nums = [1, 2, 3]
    print("\nInitial nums:", nums, "| id:", id(nums))
    mutate_list(nums)
    print("After mutate_list(nums):", nums, "| id:", id(nums))
    print("Observation: mutating a mutable argument affects the caller’s object.")

    nums2 = [1, 2, 3]
    print("\nInitial nums2:", nums2, "| id:", id(nums2))
    reassign_list(nums2)
    print("After reassign_list(nums2):", nums2, "| id:", id(nums2))
    print("Observation: reassignment inside the function does not affect caller.")

    d = {"a": 1}
    print("\nInitial dict d:", d, "| id:", id(d))
    mutate_dict(d)
    print("After mutate_dict(d):", d, "| id:", id(d))

    print("\nKey idea: Python passes references. Mutating the referred-to object "
          "is visible to the caller; rebinding the local name is not.")
