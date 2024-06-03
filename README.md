# Rainfall_Project

## Overview
This project aims to analyze and predict weather conditions using historical weather data for Raleigh, NC. The data is fetched using the Meteostat API, processed to clean and convert the relevant metrics, and then used to train a machine learning model to predict rainfall. Additionally, a Flask web application is provided to make predictions based on user inputs. We analyzed historical rainfall data to understand the interplay between humidity, temperature, pressure, and precipitation in predicting rainfall. Our goal is to develop a predictive model that can improve weather forecasting accuracy.

## Table of Contents
- [Data Collection](#Data-Collection)
- [Installation](#Installation)
- [Tools and Technologies](#Tools-and-Technologies)
- [Data Source](#Data-Source)
- [Usage](#Usage)
- [Results](#Results)
- [Rainfall Analysis and Conclusion](#Rainfall-Analysis-and-Conclusion)

## Data Collection
The project uses the Meteostat library to pull daily weather data for Raleigh, NC from January 1, 2000, to May 17, 2024.

## Installation
To run this project, you need to install the following dependencies:
pip install pandas meteostat numpy scikit-learn flask tensorflow flask-cors


### Tools and Technologies

- HTML
- JavaScript
- Flask
- Postgres
- Python
- Google Colab
- SQLAlchemy

## Data Source
We will utilize historical weather data from the following reputable sources:

Weather Underground: Monthly weather history data from Weather Underground 
(https://www.wunderground.com/history/monthly/us/nc/morrisville/KRDU/date/2024-5).

Meteostat: Historical weather data formatted according to Meteostat standards (https://dev.meteostat.net/python/#installation).

The data will span 23 years to ensure a comprehensive analysis. We will validate the data by cross-referencing with other local weather stations and official meteorological records to ensure accuracy and completeness.

## Usage

To recreate the analysis:
Clone this repository to your local machine. In PostgreSQL, create a database entitled "Rainfall" Within the "Rainfall_project" database, use the Rain_no_rain.sql file to create a table named Rainfall Import the file to the "" table just created in PostgreSQL
1.	### Data Fetching and Processing
a.	Fetch daily weather data for Raleigh, NC using the Meteostat library.

b.	Clean and convert the data, including temperature conversion to Fahrenheit, rainfall to inches, pressure to inHg, and wind speed to mph.

2.	### Database Schema
a.	Create tables for rainfall and humidity data using the provided SQL schema.

3.	### Model Training and Prediction
a.	Split the cleaned data into training and testing datasets.

b.	Train a logistic regression to predict rainfall.

c.	Evaluate the model and generate predictions.

4.	### Flask Web Application
a.	Set up a Flask app to serve predictions.

b.	Load the trained model and create an API endpoint for predictions based on user inputs.

5.	### User Interface
a.	Create an HTML form for user input.

b.	Use JavaScript (D3.js) to send user inputs to the Flask API and display the prediction.


## Rainfall Analysis and Conclusion
The Rainfall Analysis provides a comprehensive approach to understanding and predicting rainfall in Raleigh, NC. By using historical data and machine learning, this project offers valuable insights and a practical tool for weather prediction.
This project demonstrates the process of fetching, cleaning, and analyzing weather data, and building a machine learning model to predict rainfall. Additionally, it includes a Flask web application to provide predictions based on user inputs. 
The Rainfall Analysis provides a comprehensive approach to understanding and predicting rainfall in Raleigh, NC. This project demonstrates the process of fetching, cleaning, and analyzing weather data, and building a machine learning model to predict 
