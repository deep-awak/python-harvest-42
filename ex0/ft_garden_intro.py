#!/usr/bin/env python3


def ft_garden_intro(name: str, height: float, age: int) -> str:
    return (f"Plant: {name}\nHeight:{height} cm\nAge: {age} days \n")


def main() -> None:
    print("=== Welcome to My garden ===")
    print(ft_garden_intro("Rose", 25.0, 30))
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
