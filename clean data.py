import numpy as np
import pandas as p
import os
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

p.set_option('display.max_columns', 40)
nbracs = 50
inc = 100/nbracs

# Get the paths of the raw data files.

raw = 'C:/Users/jseyhun/OneDrive - Coherent Economics LLC/atp project/betting market graphs/Raw Data/'
files = os.listdir(raw)
nfiles = len(files)
files = [a + b for a, b in zip(np.repeat(raw, nfiles), files)]

# Initialize empty data frame, read in raw data, and stack.

x = p.DataFrame()
for f in files:
    d = p.read_excel(f)
    x = x.append(d)

x.iat[9714, np.where(x.columns == 'EXW')[0].item()] = 2.3 #fix one typo

# Define a function called "floorvec" which will round down each number of an array to the inverse of num. So if num is 50 then
# it will round figures down to the nearest multiple of 0.2.

def floorvec(vec, num):
    no = len(vec)
    vec2 = vec.tolist()
    vec3 = vec2
    for i in range(no):
        if ~np.isnan(vec2[i]):
            vec3[i] = math.floor(num * vec3[i]) / num
    return p.Series(vec3)

# Define the 'vars', which are the shortcuts I will use to define the odds of each of the 4 bookies. for each var, need separate odds
# for the winners and losers.

vars = ['B365', 'EX', 'PS', 'LB']
wvars = [a + b for a,b in zip(vars, np.repeat('W', len(vars)))]
lvars = [a + b for a,b in zip(vars, np.repeat('L', len(vars)))]
vars2 = wvars + lvars


for v in vars2:
    vartry = x[v].tolist()
    for i in range(x.shape[0]):
        try:
            float(vartry[i])
        except ValueError:
            print(i, vartry[i])

# For each bookie and for winners and losers, create "b" variables defining the bracket, and define "p" variables for
# the probability.

for v in vars:
    w = x[v + 'W']
    l = x[v + 'L']
    if w.dtype != 'float64':
        w = w.astype('float64')
    if l.dtype != 'float64':
        l = l.astype('float64')
    wb = v + 'Wb' #bracket for the graph
    lb = v + 'Lb'
    wp = v + 'Wp' #probability from odds
    lp = v + 'Lp'
    e = (1/w) + (1/l)
    x[wp] = (1/(w*e))
    x[lp] = (1/(l*e))
    x[wb] = floorvec(x[wp], nbracs)
    x[lb] = floorvec(x[lp], nbracs)

# Make dataset for graphing. One column per bookie.
# At each bucket value, value of the bookie var is the number of winners at b divided by the winners plus losers at b.

d = p.DataFrame(np.arange(0, 100, 2), columns = ['brac'])
d['brac_lab'] = d['brac'].astype('str') + '%'
d['brac'] = d['brac'] /100
for v in vars:
    print(v)
    w = v + 'W'
    wb = v + 'Wb'
    l = v + 'L'
    lb = v + 'Lb'
    var_for = np.repeat(np.nan, nbracs)
    var_for_n = np.repeat(np.nan, nbracs)
    for ii in range(nbracs):
        b = d['brac'][ii]
        wrows = [i for i in range(x.shape[0]) if x[wb].iloc[i] == b]
        lrows = [i for i in range(x.shape[0]) if x[lb].iloc[i] == b]
        nwins = len(wrows)
        nlose = len(lrows)
        if(nwins + nlose != 0):
            var_for[ii] = nwins / (nwins + nlose)
            var_for_n[ii] = nwins + nlose
    d[v] = var_for
    d[v + 'n'] = var_for_n

d['brac_lab2'] = [d['brac_lab'].iloc[i] if i in np.arange(0, 50, 5) else '' for i in range(d.shape[0])]
p.DataFrame.to_csv(d, "C:\\Users\\jseyhun\\OneDrive - Coherent Economics LLC\\atp project\\betting market graphs\\out\\data.csv")
