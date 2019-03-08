import joblib
import json
from sklearn import metrics
import numpy as np
import time
from sklearn import neighbors
from scipy import stats
from sklearn.model_selection import cross_val_score

class RegressionTests():
    def __init__(self,
                 reg,
                 test_data,
                 target_name,
                 column_names):
        self.reg = reg
        self.column_names = column_names
        self.target_name = target_name
        self.test_data = test_data
        self.y = test_data[target_name]
        self.X = test_data[column_names]
        
    def mse_upper_boundary(self, upper_boundary):
        y_pred = self.reg.predict(self.X)
        if metrics.mean_squared_error(self.y, y_pred) > upper_boundary:
            return False
        return True

    def mae_upper_boundary(self, upper_boundary):
        y_pred = self.reg.predict(self.X)
        if metrics.median_absolute_error(self.y, y_pred) > upper_boundary:
            return False
        return True

    def regression_testing(self, mse_upper_boundary, mae_upper_boundary):
        mse_test = self.mse_upper_boundary(mse_upper_boundary)
        mae_test = self.mae_upper_boundary(mae_upper_boundary)
        if mse_test and mae_test:
            return True
        else:
            return False

    def run_time_stress_test(self, performance_boundary):
        for performance_info in performance_boundary:
            n = int(performance_info["sample_size"])
            max_run_time = float(performance_info["max_run_time"])
            data = self.X.sample(n, replace=True)
            start_time = time.time()
            self.reg.predict(data)
            model_run_time = time.time() - start_time
            if model_run_time > run_time:
                return False
        return True

class RegressionComparison():
    def __init__(self,
                 reg_one,
                 reg_two,
                 test_data,
                 target_name,
                 column_names):
        self.reg_one = reg_one
        self.reg_two = reg_two
        self.column_names = column_names
        self.target_name = target_name
        self.test_data = test_data
        self.y = test_data[target_name]
        self.X = test_data[column_names]
        
    def two_model_prediction_run_time_stress_test(self, performance_boundary):
        for performance_info in performance_boundary:
            n = int(performance_info["sample_size"])
            data = self.X.sample(n, replace=True)
            start_time = time.time()
            self.reg_one.predict(data)
            model_one_run_time = time.time() - start_time
            start_time = time.time()
            self.reg_two.predict(data)
            model_two_run_time = time.time() - start_time
            # we assume model one should be faster than model two
            if model_one_run_time > model_two_run_time:
                return False
        return True

    def mse_result(self, reg):
        y_pred = reg.predict(self.X)
        return metrics.mean_squared_error(self.y, y_pred)

    def mae_result(self, reg):
        y_pred = reg.predict(self.X)
        return metrics.median_absolute_error(self.y, y_pred)

    def two_model_regression_testing(self):
        mse_one_test = self.mse_result(self.reg_one)
        mae_one_test = self.mae_result(self.reg_one)
        mse_two_test = self.mse_result(self.reg_two)
        mae_two_test = self.mae_result(self.reg_two)
        if mse_one_test < mse_two_test and mae_one_test < mae_two_test:
            return True
        else:
            return False
