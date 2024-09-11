"""ex01 Tea Party"""

__author__ = "730731576"


def main_planner(guests: int) -> None:
    """the entrypoint of your program"""

    print("A Cozy Tea Party For", guests, "People!")

    print("Tea Bags:", tea_bags(people=guests))

    print("Treats:", treats(people=guests))

    """Conjoining things with a "," puts a space between them.
    Python does not allow you to add a float to a string using the + so
    you need to convert it into a str"""
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates number of tea bags needed based on number of people"""
    return people * 2


def treats(people: int) -> int:
    """calculates numbre of treats based on number of tea bags"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates total cost"""
    return treat_count * 0.75 + tea_count * 0.5


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
