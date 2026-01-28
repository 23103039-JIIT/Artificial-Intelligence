def signal_color(traffic_density):
    if traffic_density == "heavy":
        return "GREEN"
    else:
        return "RED"

density = input("Enter traffic density (heavy/low/medium): ").lower()

color = signal_color(density)

print("\nTraffic Signal Decision:")
print("Signal Color:", color)