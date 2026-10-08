# Energy Consumption Monitoring System
# EEE Student GitHub Project
# Python Simulation

import time
import random
from datetime import datetime

# Electricity tariff
COST_PER_KWH = 6.50  # ₹ per kWh

# Total energy consumed
total_energy = 0.0


def read_sensor_data():
    """Simulate voltage and current sensor readings."""

    voltage = random.uniform(210, 240)  # Volts
    current = random.uniform(1, 10)     # Amps

    return voltage, current


def calculate_power(voltage, current):
    """Calculate electrical power in watts."""

    power = voltage * current
    return power


def calculate_energy(power, time_seconds):
    """Calculate energy consumed in kWh."""

    energy = (power * time_seconds) / 3600000
    return energy


def calculate_cost(energy):
    """Calculate electricity cost."""

    return energy * COST_PER_KWH


def display_data(voltage, current, power, energy, cost):
    """Display monitoring information."""

    print("\n" + "=" * 55)
    print("       ENERGY CONSUMPTION MONITORING SYSTEM")
    print("=" * 55)

    print("Time              :", datetime.now().strftime("%H:%M:%S"))
    print(f"Voltage           : {voltage:.2f} V")
    print(f"Current           : {current:.2f} A")
    print(f"Power             : {power:.2f} W")
    print(f"Energy Consumed   : {energy:.6f} kWh")
    print(f"Electricity Cost  : ₹{cost:.4f}")

    if power < 500:
        status = "LOW CONSUMPTION"
    elif power < 1500:
        status = "NORMAL CONSUMPTION"
    else:
        status = "HIGH CONSUMPTION"

    print(f"System Status     : {status}")
    print("=" * 55)


def main():
    global total_energy

    monitoring_interval = 2

    print("Energy Consumption Monitoring System")
    print("------------------------------------")
    print("Monitoring started...")
    print("Press Ctrl+C to stop.")

    try:

        while True:

            # Read simulated sensor values
            voltage, current = read_sensor_data()

            # Calculate power
            power = calculate_power(voltage, current)

            # Calculate energy
            energy = calculate_energy(
                power,
                monitoring_interval
            )

            # Add to total energy
            total_energy += energy

            # Calculate total cost
            total_cost = calculate_cost(total_energy)

            # Display information
            display_data(
                voltage,
                current,
                power,
                total_energy,
                total_cost
            )

            time.sleep(monitoring_interval)

    except KeyboardInterrupt:

        print("\n\nMonitoring stopped.")
        print("------------------------------------")
        print(f"Total Energy : {total_energy:.6f} kWh")
        print(f"Total Cost   : ₹{calculate_cost(total_energy):.2f}")
        print("------------------------------------")


if __name__ == "__main__":
    main()
