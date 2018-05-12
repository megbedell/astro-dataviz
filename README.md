This repository contains some IPython worksheets designed to demonstrate the relative capabilities of a few interactive plotting modules in python. These worksheets were made by Megan Bedell.

Slides for a companion talk can be found [here](https://docs.google.com/presentation/d/1sGvM4S9nQByNv3_1aj4nH5ynvp_pQt5MI1hk7djMcwk/edit?usp=sharing).

## Contents
-------------

The `exoplanets.ipynb` notebook demonstrates interactive plotting (tooltips, scroll and zoom, etc) with bokeh and altair.

The `gaia.ipynb` notebook scales this up to large datasets with vaex and holoviews.

## Required software
-------------

To run all of these notebooks, you'll need Python 3 with the standard scientific packages (numpy, matplotlib), [Jupyter labs (or notebooks)](http://jupyter.org/), pandas and astropy for data wrangling, and astroquery for data downloads.

Additionally, you'll want some or all of these plotting packages:
* bokeh
* altair
* glue
* vaex
* holoviews (with datashader)

I recommend installing the [Anaconda distribution](http://continuum.io/downloads). You can then add the additional packages by running:

```
pip install astroquery bokeh altair 
conda install -c glueviz glueviz
conda install -c conda-forge vaex
conda install -c conda-forge holoviews
```

(Some of the conda installs can be done in pip too, but I ran into install issues there that didn't come up with conda. Your mileage may vary.)

Then make sure you have the correct JupyterLab extensions to make the interactive plots render properly:

```
jupyter labextension install jupyterlab_bokeh
jupyter labextension install @pyviz/jupyterlab_holoviews
```

## Using these notebooks
-------------

Download this repository by running:

```
git clone https://github.com/megbedell/astro-dataviz
```

Then go into the `astro-dataviz` directory and start a JupyterLab server:

```
jupyter lab
```

Click on a notebook file in the sidebar to run it.