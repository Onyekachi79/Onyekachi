
# Optical Link Budget Calculator

def optical_link_budget():
    print("=== Optical Link Budget Calculator ===\n")

    # User inputs
P_t = float(input("Enter transmitter power (dBm): "))
receiver_sensitivity = float(input("Enter receiver sensitivity (dBm): "))
fiber_length = float(input("Enter fiber length (km): "))
fiber_attenuation = float(input("Enter fiber attenuation (dB/km): "))
num_connectors = int(input("Enter number of connectors: "))
connector_loss = float(input("Enter loss per connector (dB): "))
num_splices = int(input("Enter number of splices: "))
splice_loss = float(input("Enter loss per splice (dB): "))
system_margin = float(input("Enter system margin (dB): "))

 # Calculations
L_fiber = fiber_attenuation * fiber_length
L_connectors = num_connectors * connector_loss
L_splices = num_splices * splice_loss
L_total = L_fiber + L_connectors + L_splices + system_margin
P_r = P_t - L_total
power_margin = P_r - receiver_sensitivity
link_ok = P_r > receiver_sensitivity

# Results
print("\n=== Calculation Results ===")
print(f"Fiber Loss               : {L_fiber:.2f} dB")
print(f"Connector Loss           : {L_connectors:.2f} dB")
print(f"Splice Loss              : {L_splices:.2f} dB")
print(f"System Margin            : {system_margin:.2f} dB")
print("---------------------------------------")
print(f"Total Link Loss          : {L_total:.2f} dB")
print(f"Received Power           : {P_r:.2f} dBm")
print(f"Receiver Sensitivity     : {receiver_sensitivity:.2f} dBm")
print(f"Power Margin             : {power_margin:.2f} dB")

# Verdict
if link_ok:
    print("\n✅ Link is OK — sufficient power margin.")
else:
    print("\n❌ Link FAILS — insufficient received power.")

 
if __name__ == "__main__":
    optical_link_budget()
