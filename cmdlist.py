# Install virtualenv package
pip install virtualenv

# Create a virtual environment named 'env'
virtualenv env

# Activate the virtual environment (Windows)
env\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source env/bin/activate

# Deactivate the virtual environment
deactivate

# Install packages from a requirements file
pip install -r requirements.txt

# Freeze installed packages to a requirements file
pip freeze > requirements.txt

# Create a virtual environment using venv (Python 3.3+)
python -m venv env

# List installed packages in the current environment
pip list

# Show details of a specific package
pip show package_name

# Uninstall a package
pip uninstall package_name

# Upgrade pip to the latest version
pip install --upgrade pip

# Check for outdated packages
pip list --outdated

# Upgrade a specific package
pip install --upgrade package_name

# Create a new Conda environment named 'myenv' with Python 3.8
conda create --name myenv python=3.8

# Activate the Conda environment
conda activate myenv

# Deactivate the Conda environment
conda deactivate

# List all Conda environments
conda env list

# Remove a Conda environment
conda env remove --name myenv

# Export Conda environment to a YAML file
conda env export > environment.yml

# Create a Conda environment from a YAML file
conda env create -f environment.yml





# Data Manipulation and Analysis
pip install pandas numpy

# Data Visualization
pip install matplotlib seaborn plotly

# Machine Learning
pip install scikit-learn xgboost lightgbm catboost

# Deep Learning
pip install tensorflow keras torch torchvision

# Data Cleaning and Processing
pip install openpyxl xlrd beautifulsoup4 requests

# Statistical Analysis
pip install scipy statsmodels

# Jupyter Notebook Support
pip install jupyter jupyterlab ipykernel

# Advanced Data Manipulation
pip install dask modin[all]

# Time Series Analysis
pip install prophet pmdarima

# Database Interaction
pip install sqlalchemy psycopg2 pymysql

# Interactive Data Exploration
pip install pandas-profiling sweetviz

# Natural Language Processing (NLP)
pip install nltk spacy textblob

# Geospatial Data
pip install geopandas folium

# AutoML (for automated machine learning)
pip install autosklearn autokeras

# Excel File Manipulation
pip install openpyxl xlsxwriter

