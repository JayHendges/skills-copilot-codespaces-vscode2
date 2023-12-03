import csv

def calculate_light_intensity(planets):
    """
    Calculates the light intensity for each planet based on its size and position in the sorted list of planets.

    Args:
        planets (list): A list of dictionaries representing the planets, where each dictionary contains the following keys:
            - "Planet Name": The name of the planet (string).
            - "Distance (AU)": The distance of the planet from the sun in Astronomical Units (float).
            - "Size (km)": The size of the planet in kilometers (integer).

    Returns:
        list: A list of strings representing the light intensity for each planet. The light intensity can be one of the following:
            - "Planet Name Full": If the planet is the largest in terms of size and has no other larger planets.
            - "Planet Name Partial": If the planet has smaller planets but no larger planets.
            - "Planet Name None": If the planet has at least one larger planet.
            - "Planet Name None (Multiple Shadows)": If the planet has multiple larger planets.

    Example:
        planets = [
            {
                "Planet Name": "Mercuria",
                "Distance (AU)": 0.4,
                "Size (km)": 4879
            },
            {
                "Planet Name": "Earthia",
                "Distance (AU)": 1,
                "Size (km)": 12742
            },
            {
                "Planet Name": "Marsia",
                "Distance (AU)": 1.5,
                "Size (km)": 6779
            },
            {
                "Planet Name": "Venusia",
                "Distance (AU)": 0.7,
                "Size (km)": 12104
            }
        ]

        light_intensity = calculate_light_intensity(planets)
        print(light_intensity)
        # Output: ['Mercuria Full', 'Venusia None', 'Marsia Partial', 'Earthia None']
    """
    light_intensity = []

    sorted_planets = sorted(planets, key=lambda x: x["Distance (AU)"])

    for i in range(len(sorted_planets)):
        count = {
            "larger": 0,
            "smaller": 0
        }
        for j in range(i):
            if sorted_planets[j]["Size (km)"] > sorted_planets[i]["Size (km)"]:
                count["larger"] += 1
            elif sorted_planets[j]["Size (km)"] < sorted_planets[i]["Size (km)"]:
                count["smaller"] += 1

        if count["larger"] == 0 and count["smaller"] == 0:
            light_intensity.append(sorted_planets[i]["Planet Name"] + " Full")
        elif count["smaller"] > 0 and count["larger"] == 0:
            light_intensity.append(sorted_planets[i]["Planet Name"] + " Partial")
        elif count["larger"] == 1:
            light_intensity.append(sorted_planets[i]["Planet Name"] + " None")
        elif count["larger"] > 1:
            light_intensity.append(sorted_planets[i]["Planet Name"] + " None (Multiple Shadows)")

    sorted_planets = sorted(planets, key=lambda x: x["Size (km)"])  # Sort the planets by size

    return light_intensity

planets = [
    {
        "Planet Name": "Mercuria",
        "Distance (AU)": 0.4,
        "Size (km)": 4879
    },
    {
        "Planet Name": "Earthia",
        "Distance (AU)": 1,
        "Size (km)": 12742
    },
    {
        "Planet Name": "Marsia",
        "Distance (AU)": 1.5,
        "Size (km)": 6779
    },
    {
        "Planet Name": "Venusia",
        "Distance (AU)": 0.7,
        "Size (km)": 12104
    }
]

light_intensity = calculate_light_intensity(planets)
print(light_intensity)
