#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 11, 2023
# This program calculates the volume and surface area of a hexagonal prism with user-given dimensions.

import math

# Declare variables
volume = 1
surface_area = 1


def main():
    # Introduce the program and get user dimensions.
    print("\033[1;34;40mThis program calculates the volume and surface area of a hexagonal prism")
    print("with user given dimensions and units.\n")
    unit = input("Please enter a unit of measurement: ")
    base_edge = float(input("Please enter a base edge: "))
    height = float(input("Please enter a height: "))

    # Check if base edge or height are negative. If not calculate volume and surface area
    if base_edge <= 0:
        print("\n\033[1;31;40mYou cannot use negative numbers.")
        return
    if height <= 0:
        print("\n\033[1;31;40mYou cannot use negative numbers.")
        return
    else:
        volume = 3 * math.sqrt(3) / 2 * base_edge**2 * height
        surface_area = 6 * base_edge * height + 3 * math.sqrt(3) * base_edge**2

    # Display surface area and volume using user inputted units too
    print("\033[1;32;40mThe surface area is: {:.2f}{}^2".format(surface_area, unit))
    print("The volume is: {:.2f}{}^3".format(volume, unit))


if __name__ == "__main__":
    main()
