#!/usr/bin/env python3
# Created by: Spencer.S
# Created on: Sept 28,2022
# Program that calculates Surface Area and Volume of a Sphere
import math
from termcolor import colored


def main():
    # Request the radius from the user
    radius = float(input(colored("What is the radius of the Sphere? (cm): ", "red")))

    # Calculates Surface area
    surface_area = 4 * math.pi * radius**2

    # Calculates Volume
    volume = 4 / 3 * math.pi * radius**3

    # Display end results to user
    print(
        colored(
            "The surface area of the sphere is: {:,.2f}cm^2".format(surface_area),
            "cyan",
        )
    )
    print(colored("The volume of the sphere is: {:,.2f}cm^3".format(volume), "magenta"))


if __name__ == "__main__":
    main()
