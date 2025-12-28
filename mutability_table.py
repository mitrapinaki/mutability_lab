def run():
    print("\n--- Mutability Table ---")

    samples = [
        ("int", 42),
        ("float", 3.14),
        ("str", "hello"),
        ("tuple", (1, 2, 3)),
        ("list", [1, 2, 3]),
        ("dict", {"a": 1, "b": 2}),
        ("set", {1, 2, 3}),
        ("frozenset", frozenset({1, 2, 3})),
        ("bytes", b"abc"),
        ("bytearray", bytearray(b"abc")),
    ]

    def is_mutable(obj):
        try:
            original_id = id(obj)
            try:
                # Try a “mutating” operation
                if isinstance(obj, list):
                    obj.append(None)
                elif isinstance(obj, dict):
                    obj["__test__"] = None
                elif isinstance(obj, set):
                    obj.add(None)
                elif isinstance(obj, bytearray):
                    obj.append(0)
                else:
                    # For immutables, attempt reassignment-like ops
                    obj += obj
            except TypeError:
                # Some types simply don't support +=
                pass
            return id(obj) == original_id
        except Exception:
            return False

    for name, value in samples:
        print(f"{name:10} | mutable: {is_mutable(value)}")

    print("\nNote: This is heuristic. Mutability is a property of the type’s API, "
          "not just what this test observes.")
