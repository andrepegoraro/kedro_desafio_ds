"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.0
"""

from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def split_data(df, test_size = 0.3, random_state = 457):
    """ Splits data into train and test datasets """

    # Defining X and y:

    X = df.drop('slowness_in_traffic', axis=1)
    y = df['slowness_in_traffic']
               
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state = 457
    )
    return X_train, X_test, y_train, y_test

def fit_model(X_train, X_test, y_train, y_test):
    """ fits a Random Forest model using a training dataset """
    
    regressor = RandomForestRegressor(n_estimators = 20, random_state = 457)
    regressor.fit(X_train, y_train)
    
    # Predicts test set
    y_prediction_2 = regressor.predict(X_test)
    
    # Reports Score
    score_2 = r2_score(y_test, y_prediction_2)
    print('R square =', score_2)
    
    return regressor