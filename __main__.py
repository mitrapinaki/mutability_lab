from . import mutability_table
from . import aliasing
from . import default_args
from . import shallow_vs_deep
from . import function_semantics


def main():
    print("\n=== Mutability Lab ===\n")

    mutability_table.run()
    aliasing.run()
    default_args.run()
    shallow_vs_deep.run()
    function_semantics.run()

    print("\n=== End of Mutability Lab ===\n")


if __name__ == "__main__":
    main()
