#!/usr/bin/env python3
# Original package: CH7.JAV
import math
import time

class RicherScale:
    
    def RicherScaleEN(self, Magnitude: float, ret: str) -> str:
        power = (Magnitude * (1.5))
        power2u = (power + 11.8)

        # Extract integer and decimal parts 
        power2uDIV = power2u - math.floor(power2u)
        Econtaner = math.pow(10, power2uDIV)
        Econtaner = round(Econtaner * 100.0) / 100.0  # Round for display

        # Compute total energy
        totalEnergy = math.pow(10, power2u)

        # Print results
        print("> total Energy output (Uncompressed): " + str(totalEnergy))
        ret = ("> E ~ " + str(Econtaner) + " x 10^" + str(int(power2u - power2uDIV)))
        return ret

if __name__ == "__main__":
    # Dependencies similar to java.util.Scanner are replaced with input() functionality of Python
    player = RicherScale()

    print("Continue with Richter Scale Calculations? (Y/N)")
    confirm = input().lower()

    if confirm == "y":
        print("Input magnitude: ")
        MAG = float(input())

        print("Calculating...")
        time.sleep(2)

        print(player.RicherScaleEN(MAG, ""))
    else:
        print("Exiting...")
      