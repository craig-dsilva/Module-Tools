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


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]
    current_laptop: Union[Laptop, None]
        

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    allocation = {}
    for person in people:
        for laptop in laptops:
            for os in person.preferred_operating_system:
                if person.preferred_operating_system.count(os) > 0:
                    sadness = person.preferred_operating_system.index(os)
                    allocation[person.name] = {"Sadness": sadness, "Laptop": laptop}
                    laptops.remove(laptop)
                    break
                else:
                    allocation[person.name] = {"Sadness": 100, "Laptop": laptop}
                    laptops.remove(laptop)
                    break
    return allocation
    

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


print(allocate_laptops(people, laptops))