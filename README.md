# global-attribute-creator
Tool to add global attributes to a netCDF file
Jupyter notebook to facilitate the addition of global attributes to a netCDF file, following the ACDD convention. 
Requirements are set to allow dataset upload to NIRD/Sigma2 using the NorDataNet upload interface. 

Files:
- CreateNetCDF.ipynb: notebook to be run
- vocabularies: function to fetch controlled vocabularies
- files: example files

## How to run the notebook

- conda env create -f environment.yml
- conda activate global-attributes
- jupyter-notebook CreateNetCDF.ipynb
