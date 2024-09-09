from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive

def get_star_radius(kepler_id):
    try:
        # Query the NASA Exoplanet Archive for the given Kepler ID
        result = NasaExoplanetArchive.query_criteria(table="q1_q17_dr25_stellar", select="radius", where=f"kepler_id={kepler_id}")
        
        # Check if the result is empty
        if len(result) == 0:
            return "No data found for the given Kepler ID."
        
        # Extract the radius from the result
        radius = result['radius'][0]
        return f"The radius of the star with Kepler ID {kepler_id} is {radius} solar radii."
    
    except Exception as e:
        return f"An error occurred: {e}"

# Input the Kepler ID
kepler_id = input("Enter the Kepler ID of the target: ")
print(get_star_radius(kepler_id))
