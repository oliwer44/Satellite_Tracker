import ephem
import matplotlib.pyplot as plt
from datetime import datetime
from skyfield.api import utc, load, Topos

station_data = load.tle('https://celestrak.com/NORAD/elements/stations.txt')
iss = station_data['ISS (ZARYA)']
print(iss)

## Change to your specified time range. Current: 2 hours
time_scale = load.timescale()
minutes = range(60 * 2)
time_range = time_scale.utc(2024, 3, 21, 2, minutes)

altitudes = []
azimuths = []

for t in time_range:
    # Calculate satellite position at each time step
    port_hedland = Topos(latitude='20.3123 S', longitude='118.64498 E')
    orbit = (iss - port_hedland).at(t)
    altitude, azimuth, distance = orbit.altaz()
    
    # Append the altitude and azimuth values to the lists
    altitudes.append(altitude.degrees)
    azimuths.append(azimuth.degrees)

plt.figure(figsize=(10, 5))
plt.plot(azimuths, altitudes, marker='o', linestyle='-')
plt.title("Satellite Path - ISS")
plt.xlabel("Azimuth (degrees)")
plt.ylabel("Altitude (degrees)")
plt.grid(True)
plt.show()