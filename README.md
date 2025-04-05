# Rice Dataset Analysis Pipeline by ZFVG

# Documents Of Interest
[![DOI](https://zenodo.org/badge/DOI/10.11591/ijict.v14i1.pp164-173.svg)](https://zenodo.org/records/15067408)

https://www.pnrjournal.com/index.php/home/article/view/5182
https://www.mdpi.com/2079-9292/12/10/2285

## Overview

This project mainly analyzed the rice dataset from the UCI archive with the entire workflow stored in this repository. 
* The rice data set had two classes (Cammeo and Osmancik). Moreover, the dataset has seven numerical features: Area Integer, Perimeter Real, Major_Axis_Length Real, Minor_Axis_Length Real, EccentricityReal, Convex_AreaInteger, and	Extent Real.
* Using the provided Python file on logistic regression, you can predict whether a new data with the features mentioned above is either Cammeo or Osmancik.
* You can obtain the accuracy score of the classification model above as well as a confusion matrix graph for the testing data to examine the level of effectiveness of the provided model.

## Contributions:

**Elena Zen: ...**
**Lorenzo Forcucci: ...**
**Matteo Vanzanelli: ...**
**Luca Graziadei: ...**

## Analysis

* Using logistic regression with gridsearch on the rice dataset ...
  
## Workflow 

1. Lorem Ipsum Dolor
2. Lorem Ipsum Dolor
3. Lorem Ipsum Dolor
4. Lorem Ipsum Dolor

This project performs analysis using machine learning models. The pipeline includes data loading, preprocessing, model training, evaluation, and result storage in an SQLite database.

## Project Structure
```
│── data/                          # Raw and processed data
│   ├── raw/                       # Original Raw files
│   ├── processed/                 # Preprocessed data
│── database/                      # SQLite database and schema
│── logs/                          # Logs for debugging
│   ├── pipeline.log               # Log file capturing pipeline execution
│── models/                        # Tmporary store for Models
│   ├── model.pickle              # Trained model in python serialized object format
│── notebooks/                     # Jupyter notebooks for analysis
│── src/                           # Source code
│   ├── config.py                  # Configuration settings
│   ├── load_data.py               # Load tweets from Excel
│   ├── preprocess.py              # Preprocessing functions
│   ├── make_model.py              # Model training & prediction
│── scripts/                       # Scripts for execution
│   ├── run_pipeline.py            # End-to-end execution
│── requirements.txt               # Dependencies 2DO!
│── README.md                      # Project documentation
```
