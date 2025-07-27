import subprocess
import re
import os

def run_ngspice_simulation(netlist_content):
    # Save the netlist to a temporary file
    netlist_file = "temp_circuit.cir"
    with open(netlist_file, "w") as f:
        f.write(netlist_content)

    # Run Ngspice in batch mode
    result = subprocess.run(["ngspice", "-b", netlist_file], capture_output=True, text=True)

    # Extract power value from Ngspice output (example: "Total Power: X mW")
    power_match = re.search(r"Total Power:\s+([\d\.]+)", result.stdout)
    power_value = float(power_match.group(1)) if power_match else None

    # Clean up
    os.remove(netlist_file)

    return power_value

def generate_netlist(gate_type, num_gates, frequency, voltage):
    # A simple RC load netlist to approximate power
    return f"""
* Simple {gate_type} power estimation circuit
Vdd vdd 0 {voltage}
Rload vdd out 1k
Cload out 0 {num_gates * 2}f
.tran 0.1n 10n
.measure TRAN TotalPower AVG power
.end
"""
