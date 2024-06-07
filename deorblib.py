import numpy as np
import astropy.constants as constants
import astropy.units as u
import astropy.time
import pandas as pd
import scipy.interpolate
from pymsis import msis


G = constants.G.value # si unit
M_earth = constants.M_earth.value # kg
R_earth = constants.R_earth.value # m
mu_earth = G * M_earth

def get_atm_density_function(max_alt=2000, lat=0, lon=0, f107=150, Ap=3, date="2003-01-01T00:00", version=2.1):
    """
    MSIS 2.1 atmospheric density model
    
    https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EA001321
    https://pypi.org/project/pymsis/
    """
    date = np.datetime64(date)
    alts = np.linspace(0, max_alt, 10000)
    f107a = f107
    aps = [[Ap] * 7]

    columns = [
        "Total mass density",
        "N2",
        "O2",
        "O",
        "He",
        "H",
        "Ar",
        "N",
        "Anomalous O",
        "NO",
        "Temperature",
    ]
    model_output = pd.DataFrame(np.squeeze(msis.run(date, lon, lat, alts, f107, f107a, aps, version=version)),
                                columns=columns)
    fdens = scipy.interpolate.interp1d(alts, model_output['Total mass density'])
    return fdens

def kepler_velocity(alt):
    """
    alt in m
    v in m/s
    """
    v = np.sqrt(mu_earth / (R_earth + alt))
    return v

def kepler_altitude(v):
    """
    v in m/s
    alt in m
    """
    alt = mu_earth / v**2 - R_earth
    return alt

def taimodjd2date(taimodjd):
    return np.datetime64(astropy.time.Time(taimodjd + 2430000, format='jd', scale='tai').utc.datetime)
    