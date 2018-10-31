# exo-or-not

This project focuses on the classification of exoplanet candidates. It uses a dataset from NASAs exoplanet archive with 7,000 candidates. In the end I used a Random Forest model with .91 Recall and .90 AUC. 

I also built a Flask app to make predictions on-demand.

Please read the project summary pdf for more information.

## Folders

* `flask_app` - HTML, CSS, and Python code for Flask app

## Files

* `Classification of Exoplanet Candidates.pdf` pdf of presentation
* `EDA-clean.ipynb` data cleaning and exploratory data analysis of dataset
* `cumulative.csv` original dataset
* `finalize-model.ipynb` choose final model based on previously unseen test data
* `keplerutils.py` utility file primarily used for different resampling methods
* `model-kepler.ipynb` narrow down potential models using cross-validation
* `model.pkl` a pickled version of my final model, trained on all my data. My Flask app uses this to make predictions
* `proposal.pdf` my initial proposal for this project
* `summary.pdf` summary of all my work in the project
