@echo off
REM Batch file to download Kepler target pixel files using curl

cd \Users\Public\Kepler

REM Download each file using curl
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2009166043257_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2009259160929_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2009350155506_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2010078095331_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2010174085026_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2010265121752_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2010355172524_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2011073133259_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2011177032512_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2011271113734_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2012004120508_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2012088054726_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2012179063303_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2012277125453_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2013011073258_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2013098041711_lpd-targ.fits.gz
curl -O https://archive.stsci.edu/missions/kepler/target_pixel_files/0047/004770617/kplr004770617-2013131215648_lpd-targ.fits.gz

echo All files have been downloaded.
pause
