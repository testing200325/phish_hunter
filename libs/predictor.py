# To perform operations on dataset
import pandas as pd
import numpy as np

# Machine learning model
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Visualization
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import export_graphviz

# My additions
from ucimlrepo import fetch_ucirepo
from sklearn.linear_model import LinearRegression
import pickle

import warnings

warnings.filterwarnings("ignore")

class Predictor(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.loaded_dt_classifier = None

        # Load the model from the file
        with open('decision_tree_model.pkl', 'rb') as file:
            self.loaded_dt_classifier = pickle.load(file)

    def make_prediction(self, data=None):
        #try:
        new_sample = np.array([data])
        prediction = self.loaded_dt_classifier.predict(new_sample)[0]
        pred_prob = self.loaded_dt_classifier.predict_proba(new_sample)[0]
        safe_prob = pred_prob[0]*100
        unsafe_prob = pred_prob[1]*100

        #print(f"Prediction: {prediction}")
        #print(f"Prediction Probability: {pred_prob}")
        #print(f"Safe Probaility: {safe_prob}")
        #print(f"Unsafe Probability: {unsafe_prob}")
        return False if prediction == -1 else True
        #except Exception as err:
        #    return err