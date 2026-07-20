#!/usr/bin/env python3


def ft_garden_intro(name: str, height: float, age: int):
    print(f"Plant: {name}\nHeight:{height} cm\nAge: {age} days \n")


if __name__ == "__main__":
    print("=== Welcome to My garden ===")
    ft_garden_intro("Rose", 25, 30)
    print("=== End of Program ===")
