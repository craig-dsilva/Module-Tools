from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Union


class OperatingSystem(Enum):
    MACOS = "MacOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


@dataclass
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]
    current_laptop: Union[Laptop, None]
    def display_laptops(self) -> Union[Laptop, None]:
        return self.current_laptop


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> None:
    for person in people:
        for laptop in laptops:
            if person.preferred_operating_system[0] == laptop.operating_system:
              person.current_laptop = laptop
              laptops.remove(laptop)
    

people = [
    Person(name="Imran", age=22, preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU], current_laptop=None),
    Person(name="Eliza", age=34, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU], current_laptop=None),
]


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]


allocate_laptops(people, laptops)


for person in people:
    print(person.name)
    print(f"Model: {person.current_laptop.model} OS: {person.current_laptop.operating_system.value}")