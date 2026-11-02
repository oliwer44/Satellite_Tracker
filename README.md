# ISS Satellite Tracking & Pass Visualization Tools

A collection of Python scripts for predicting, calculating, and visualizing International Space Station (ISS) passes relative to a ground observer's location using live TLE (Two-Line Element) orbital data from CelesTrak.

---

## 📌 Included Scripts

### 1. `ground_track_visualisation.py`
Calculates and plots the trajectory path of the ISS over a defined timeframe on a standard Cartesian grid.
* **X-Axis:** Azimuth angle (degrees, $0^\circ - 360^\circ$)
* **Y-Axis:** Altitude angle above the horizon (degrees, $0^\circ - 90^\circ$)
* **Use Case:** Quick inspection of satellite elevation changes over short duration windows.

### 2. `polar_plot_of_passes.py`
Computes satellite visibility over extended durations (e.g., 48 hours), automatically detects when the ISS crosses above the horizon, and plots the pass on a polar sky chart (zenith view).
* **Center of chart:** Zenith ($90^\circ$ elevation, directly overhead)
* **Outer perimeter:** Horizon ($0^\circ$ elevation)
* **Orientation:** North-Up ($0^\circ$) with clockwise direction
* **Timestamps:** Labels specific timestamps along the trajectory trajectory curve

---

## 📐 Mathematical & Coordinate Transformation Model

Both scripts compute the topocentric horizon coordinates (**Altitude / Azimuth**) of the target satellite relative to the observer's location:

* **Altitude ($a$):** Elevation angle measured from the horizon ($0^\circ$) to the zenith ($90^\circ$).
* **Azimuth ($A$):** Compass bearing angle measured clockwise from True North ($0^\circ$).

### Polar Projection Transformation
For `polar_plot_of_passes.py`, the topocentric coordinates are mapped into polar plot coordinates $(\theta, r)$:

$$
\theta = A_{\text{radians}}
$$

$$
r = 90^\circ - a_{\text{degrees}}
$$

Where:
* $r = 0^\circ$ corresponds to the Zenith (directly above the observer).
* $r = 90^\circ$ corresponds to the local Horizon.

---

## 🛠️ Prerequisites & Installation

Ensure you have Python 3.8+ installed along with the required libraries:

```bash
pip install skyfield matplotlib numpy pytz ephem
```

---

## ⚙️ Configuration & Customization

Before running the scripts, you can customize the observer coordinates, timezone, and evaluation time range directly inside the Python files:

1. **Observer Location (Geocoordinates):**
   ```python
   # Modify latitude and longitude to your target location
   observer = Topos(latitude='20.3123 S', longitude='118.64498 E')
   ```

2. **Timezone (`polar_plot_of_passes.py`):**
   ```python
   # Change to your local timezone
   time_zone = timezone('US/Pacific')
   ```

3. **Evaluation Date & Time Window:**
   ```python
   # Set the start UTC year, month, day, hour
   time_range = time_scale.utc(2024, 3, 21, 2, minutes)
   ```

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd Satellite_and_Orbit_Tracking
   ```

2. Run the ground track trajectory visualization:
   ```bash
   python ground_track_visualisation.py
   ```

3. Run the polar pass predictor & sky chart visualization:
   ```bash
   python polar_plot_of_passes.py
   ```

---

## 📄 Output Summary

* **Console Output:** Displays satellite TLE data, rise/set time predictions, and array indices of calculated passes.
* **Graphical Output:** Displays matplotlib windows showing the path/polar chart of the satellite pass.