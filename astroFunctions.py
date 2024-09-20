import lightkurve as lk
import numpy as np

"""
Python file to contain functional elements to interact with NASA Exoplanet Archive  
"""

def FetchFluxSeries(kepler_id, mission="Kepler"):
    """
    Function to fetch the flux series of a given Kepler ID
    """
    search_result = lk.search_targetpixelfile(kepler_id, "Kepler")
    for i in search_result:
        ##Print each attribute of i
        print(i.target_name)


FetchFluxSeries(11904151)