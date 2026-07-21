#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = height
        self._age: int = age

    def show(self) -> str:
        return f"{self.name}: {self._height}cm, {self._age} days old"

    def grow(self) -> float:
        self._height = round(self._height + 0.8, 1)
        self._age += 1
        return self._height

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def _validate_positive(self, value: float, field_name: str) -> bool:
        if value < 0:
            print(f"{self.name}: Error, {field_name} can't be negative")
            print(f"{field_name.capitalize()} update rejected")
            return False
        return True

    def set_height(self, new_height: float) -> None:
        if self._validate_positive(new_height, "height"):
            self._height = round(float(new_height), 1)
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if self._validate_positive(new_age, "age"):
            self._age = new_age
            print(f"Age updated: {self._age} days\n")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-1)
    rose.set_age(-10)
    print("")
    print(f"Current state: {rose.show()}")


if __name__ == "__main__":
    main()
