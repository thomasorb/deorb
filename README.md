# deorb
Various codes and notes on the deorbiting projet



## install GMAT API

```bash
conda create -n gmat -c conda-forge -c astropy -c anaconda python=3.9 numpy scipy matplotlib astropy h5py pandas pytables jupyterlab astroquery gitpython

conda activate gmat

cd /path/to/GMAT/api

python BuildApiStartupFile.py

echo '/path/to/GMAT/api' > ~/miniconda3/envs/gmat/lib/python3.9/site-packages/conda.pth

python -c 'import load_gmat' # should return True if install was successful
```

## install other libraries
```bash
conda activate gmat
pip install pymsis # up-to-date atmospheric model
```


