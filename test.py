import lightkurve as lk

def fetch_all_kepler_data(kepler_id):
    # Search for all available TPFs using the Kepler ID
    search_result = lk.search_targetpixelfile(kepler_id, mission='Kepler')
    
    # List to store flux arrays
    flux_arrays = []
    
    # Loop through each search result and download the TPF
    for tpf_file in search_result:
        tpf = tpf_file.download()
        
        # Plot the target pixel file
        #tpf.plot()
        
        # Extract the light curve
        lc = tpf.to_lightcurve()
        
        # Append the flux array to the list
        flux_arrays.append(lc.flux)
    
    # Print the flux arrays
    for i, flux in enumerate(flux_arrays):
        print(f"Flux array for TPF {i+1}:")
        for f in flux:
            print(f)

# Example usage
kepler_id = 11904151  # Replace with your Kepler Object ID
fetch_all_kepler_data(kepler_id)
