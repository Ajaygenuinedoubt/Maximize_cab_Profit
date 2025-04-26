# utils_map.py
import folium
from streamlit_folium import folium_static

def draw_route(pickup, drop):
    lat_long = {
        "Back Bay": (42.3503, -71.0810),
        "Beacon Hill": (42.3588, -71.0707),
        "Boston University": (42.3505, -71.1054),
        "Fenway": (42.3467, -71.0972),
        "Financial District": (42.3555, -71.0556),
        "Haymarket Square": (42.3637, -71.0589),
        "North End": (42.3656, -71.0545),
        "North Station": (42.3656, -71.0616),
        "Northeastern University": (42.3398, -71.0892),
        "South Station": (42.3522, -71.0552),
        "Theatre District": (42.3519, -71.0625),
        "West End": (42.3613, -71.0677)
    }

    map_center = [42.3601, -71.0589]
    m = folium.Map(location=map_center, zoom_start=13)
    folium.Marker(location=lat_long[pickup], popup="Pickup", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=lat_long[drop], popup="Drop", icon=folium.Icon(color='red')).add_to(m)
    folium.PolyLine(locations=[lat_long[pickup], lat_long[drop]], color='blue').add_to(m)

    folium_static(m)
