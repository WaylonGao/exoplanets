from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive

def get_star_radius(kepler_id):
    try:
        # Query the NASA Exoplanet Archive for the given Kepler ID
        result = NasaExoplanetArchive.query_criteria(table="q1_q17_dr25_stellar", select="radius", where=f"kepid={kepler_id}")
        
        # Check if the result is empty
        if len(result) == 0:
            return f"No data found for the given Kepler ID: {kepler_id}. Please check the ID and try again."
        
        # Extract the radius from the result
        radius = result['radius'][0]
        radius_value = str(radius).split()[0]
        return radius_value
    
    except Exception as e:
        return f"An error occurred: {e}"

# Input the Kepler ID
kepler_id = input("Enter the Kepler ID of the target: ")
kepler_id = 757076
print(get_star_radius(kepler_id))
