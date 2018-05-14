This repository contains some IPython worksheets designed to demonstrate the relative capabilities of a few interactive plotting modules in python. These worksheets were made by Megan Bedell.

Slides for a companion talk can be found [here](https://docs.google.com/presentation/d/1sGvM4S9nQByNv3_1aj4nH5ynvp_pQt5MI1hk7djMcwk/edit?usp=sharing).

## Contents

The `animated_cepheids.ipynb` notebook shows how to make animated gifs or movies with matplotlib. As an example, we make a (somewhat cartoony) illustration of how Cepheid variable stars change in brightness over time using Gaia DR1 measurements.

The `interactive_exoplanets.ipynb` notebook demonstrates interactive plotting (tooltips, scroll and zoom, cross-linking plots, etc) with bokeh and altair. In this example, we use properties of confirmed exoplanets to make a mass-radius diagram.

The `interactive_gaia.ipynb` notebook scales this up to large datasets with vaex and holoviews.

## Required software

These notebooks run with Python 3 and [Jupyter notebooks](http://jupyter.org/).

To run `animated_cepheids.ipynb` you'll just need a basic scientific stack (numpy, matplotlib, pandas) and astroquery. All of these are easy to install with pip.

To run `interactive_exoplanets.ipynb` you'll additionally need bokeh and altair, also available with pip:

```
pip install bokeh altair
```

If you're going to run from a notebook, you're good to go. If you want to run in Jupyter Labs you'll need an extension to make the bokeh plots render:

```
jupyter labextension install jupyterlab_bokeh
```

Note that altair is recommended for use with Jupyter Labs, but it still works in a notebook (with one extra line of setup code).

For `interactive_gaia.ipynb`, you'll need holoviews and vaex. The installation for these is more complex and has the potential to interfere with your normal python environment. One good way of installing is using [Anaconda distribution](http://continuum.io/downloads) and creating a virtual environment in which to install these packages. Here's a snippet of code to do this:

```
conda create -n dataviz_env python=3.6
source activate dataviz_env
pip install jupyterlab pandas astropy 
conda install -c conda-forge vaex
conda install -c conda-forge holoviews
```

(Some of the conda installs can be done in pip too, but I ran into install issues there that didn't come up with conda. Your mileage may vary.)

Then get the JupyterLab extension for holoviews:

```
jupyter labextension install @pyviz/jupyterlab_holoviews
```

## Using these notebooks

Download this repository by running:

```
git clone https://github.com/megbedell/astro-dataviz
```

Then go into the `astro-dataviz` directory and start a JupyterLab server:

```
jupyter lab
```

Click on a notebook file in the sidebar to run it.