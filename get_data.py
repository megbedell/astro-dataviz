'''
Helper functions to download data for tutorials.
'''

from astropy.utils.data import download_file
from astropy.io import ascii
from astropy.table import Table
from astroquery.gaia import Gaia

def get_confirmed_planets(cache=True, show_progress=True,
                            select=None):
    """
    Download (and optionally cache) a table from the `NExScI Exoplanet Archive 
                                <http://exoplanetarchive.ipac.caltech.edu/index.html>`_.
    Based on the code from `astroquery <https://github.com/astropy/astroquery>`_.
                                
    Parameters
    ----------
    cache : bool (optional)
        Cache table to local astropy cache? Default is `True`.
    show_progress : bool (optional)
        Show progress of table download (if no cached copy is
        available). Default is `True`.
    select : str (optional)
        Comma-separated, no spaces string indicating columns to be
        returned. Default `None` will select all default columns
        as set by the Exoplanet Archive API. `*` will select all.
    Returns
    -------
    table : `~astropy.table`
        Astropy table of requested data.
    """
    url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets'
    url += '&format=csv'
    if not select is None:
        url += '&select='+select
    table_path = download_file(url, cache=cache,
                                   show_progress=show_progress,
                                   timeout=120)
    table = ascii.read(table_path)
    
    # Store column of planet names:
    pl_names = [host_name.replace(' ', '') + letter
                       for host_name, letter in
                       zip(table['pl_hostname'].data,
                           table['pl_letter'].data)]
    table['pl_name'] = pl_names
    
    return table
    
def get_cepheids():
    """
    Execute ADQL query for Gaia DR1 Cepheids using astroquery's TAP+ utils.
    
    Returns
    -------
    table : `~astropy.table`
        Astropy table of requested data.
    """
    job = Gaia.launch_job("SELECT cep.*, gaia.ra, gaia.dec \
        FROM gaiadr1.cepheid AS cep \
        INNER JOIN gaiadr1.gaia_source as gaia \
        on cep.source_id = gaia.source_id")
    return job.get_results()