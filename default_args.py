def append_with_default(value, container=[]):
    container.append(value)
    return container


def append_with_safe_default(value, container=None):
    if container is None:
        container = []
    container.append(value)
    return container


def run():
    print("\n--- Default Argument Pitfall ---")

    print("\nCase 1: Using a mutable default argument")
    r1 = append_with_default(1)
    print("First call append_with_default(1):", r1)
    r2 = append_with_default(2)
    print("Second call append_with_default(2):", r2)
    r3 = append_with_default(3)
    print("Third call append_with_default(3):", r3)
    print("Observation: the same list is reused across calls.\n")

    print("id(r1):", id(r1))
    print("id(r2):", id(r2))
    print("id(r3):", id(r3))

    print("\nCase 2: Using a safe default (None + new list inside)")
    s1 = append_with_safe_default(1)
    print("First call append_with_safe_default(1):", s1)
    s2 = append_with_safe_default(2)
    print("Second call append_with_safe_default(2):", s2)

    print("id(s1):", id(s1))
    print("id(s2):", id(s2))

    print("\nKey idea: default argument expressions are evaluated once at function "
          "definition time, not per call.")
