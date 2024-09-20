import lightkurve as lk
import numpy as np
import csv



def fetch_all_kepler_data1(kepler_id):
    #Append the data to CSV
    f=open("keplerData.csv")
    w = csv.writer(f)
    
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
            w.writerow(f)
    print("CSV File data written successfully")


def fetch_all_kepler_data(kepler_id):
    # Open the CSV file in write mode
    with open("keplerData.csv", mode='w', newline='') as f:
        w = csv.writer(f)
        
        # Search for all available TPFs using the Kepler ID
        search_result = lk.search_targetpixelfile(kepler_id, mission='Kepler')
        
        # List to store flux arrays
        flux_arrays = []
        
        # Loop through each search result and download the TPF
        for tpf_file in search_result:
            tpf = tpf_file.download()
            
            # Extract the light curve
            lc = tpf.to_lightcurve()
            
            # Append the flux array to the list
            flux_arrays.append(lc.flux)
        
        # Write the flux arrays to the CSV file
        for i, flux in enumerate(flux_arrays):
            print(f"Flux array for TPF {i+1}:")
            for f in flux:
                w.writerow([f])


# Example usage
kepler_id = 11904151  # Replace with your Kepler Object ID
fetch_all_kepler_data(kepler_id)