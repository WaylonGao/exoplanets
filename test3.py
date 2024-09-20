from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive

def GetStarRadius(kepler_id):
    try:
        result = NasaExoplanetArchive.query_criteria(table="q1_q17_dr25_stellar", select="radius", where=f"kepid={kepler_id}")
        
        if len(result) == 0:
            return f"No data found for the given Kepler ID: {kepler_id}. Please check the ID and try again."
        
        radius = result['radius'][0]
        radius_value = str(radius).split()[0]
        return radius_value
    
    except Exception as e:
        return f"An error occurred: {e}"
    

def GetExolanetSize(stdFlux, lowFlux, kepId, ):

    """    
    The simplest way to do it which ought to give a good answer is just to consider two 
    overlapping circles with radius R (the star) and r (the planet) to estimate r when 
    we know R we just think about the maximum depth of the transit light curve and the 
    percentage decrease from normal brightness will just be 4*pi*r^2/4*pi*R^2 which 
    simplifies to the ratio of the square of the radii. This should be more than good 
    enough for your project though there are other factors to consider like light 
    reflected by the planet when it is not transiting, atmospheric effects, variability
    in the star's brightness etc
    """
    #First first step is to confirm the validity of the Kepler ID before sending any web requests.
    #First step is to fetch the radius of the star from the NASA Exoplanet Archive
    

    pass

kepler_id = 757076 #Test Kepler ID
print(GetStarRadius(kepler_id))
