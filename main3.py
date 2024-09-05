import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt

from astroquery.mast import Mast
from astroquery.mast import Observations

keplerObs = Observations.query_criteria(target_name='kplr008957091', obs_collection='Kepler')
keplerProds = Observations.get_product_list(keplerObs[0])
yourProd = Observations.filter_products(keplerProds,extension='kplr008957091-2012277125453_lpd-targ.fits.gz',
                                        mrp_only=False)
yourProd



Observations.download_products(yourProd, mrp_only=False, cache=False)

filename = "./mastDownload/Kepler/kplr008957091_lc_Q000000000011111111/kplr008957091-2012277125453_lpd-targ.fits.gz"
fits.info(filename)


with fits.open(filename) as hdulist: 
    header1 = hdulist[1].header
  
print(repr(header1[1:25])) #repr() prints the info into neat columns


print("\n\n\n\n")


with fits.open(filename) as hdulist:
    binaryext = hdulist[1].data

binarytab = Table(binaryext)
binarytab[0:4]

plt.title('Flux Row 0')
plt.xlabel('Column')
plt.ylabel('Row')

plt.imshow(binarytab['FLUX'][0], cmap=plt.cm.YlGnBu_r)
plt.colorbar()
plt.clim(0,300)
plt.show()