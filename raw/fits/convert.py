from astropy.table import Table
from astropy.io import fits
import pandas as pd
import glob
import os

# making output directory
try:
    os.mkdir("./raw/textfiles")
except:
    print("directory exists")

# getting all files in specified format
os.chdir("./raw/fits/")
files = []
for file in glob.glob("*.fits"):
    files.append(file)

print(files)
# list of columns
cols = "TIME_BIN TIME_MIN TIME TIME_MAX COUNTS STAT_ERR AREA EXPOSURE COUNT_RATE COUNT_RATE_ERR"
cols = cols.split(" ")

# convert files
for file in files[0:2]:
    # accessing fits data
    hdu_list = fits.open(file, memmap=True)
    evt_data = Table(hdu_list[1].data)

    # initialising DataFrame
    df = pd.DataFrame()

    # writing to dataframe
    for col in cols:
        exec(f"df['{col}']=list(evt_data['{col}'])")

    # writing to file
    
    df.to_csv(f"./textfiles/{file}.txt", index=False, sep=" ")
