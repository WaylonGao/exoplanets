import lightkurve as lk

def get_pixel_brightnesses(kepler_id):
    # Download the target pixel file for the given Kepler ID
    tpf = lk.search_targetpixelfile(kepler_id).download_all()

    # Extract the first frame of the target pixel file
    first_frame = tpf.flux[0]

    # Convert the frame to a 2D list of pixel brightnesses
    pixel_brightnesses = first_frame.value.tolist()

    return pixel_brightnesses

# Example usage
kepler_id = 8462852  # Replace with your Kepler ID
brightnesses = get_pixel_brightnesses(kepler_id)
for row in brightnesses:
    print(row)
