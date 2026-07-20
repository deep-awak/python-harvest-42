#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self) -> float:
        self.height = round(self.height + 0.8, 1)
        self.age += 1
        return self.height


def main() -> None:
    rose: Plant = Plant("Rose", 25.0, 30)
    oak: Plant = Plant("Oak", 200.0, 365)
    cactus: Plant = Plant("Cactus", 5.0, 90)
    sunflower: Plant = Plant("Sunflower", 80.0, 45)
    fern: Plant = Plant("Fern", 15.0, 120)
    list_flower: list[Plant] = [rose, oak, cactus, sunflower, fern]
    for flower in list_flower:
        print(f"Created: {flower.show()}")


if __name__ == "__main__":
    main()
