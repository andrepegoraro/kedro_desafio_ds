"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.0
"""

def batch_predict(model_artifact, dataset, encoder):
    """ 
    This function takes a pre-trained moddel and it predicts 
    an unknown variable inside the dataset
    """

    predictions = model_artifact.predict(dataset)

    final_predictions = dataset
    final_predictions['slowness_in_traffic'] = predictions

    return final_predictions